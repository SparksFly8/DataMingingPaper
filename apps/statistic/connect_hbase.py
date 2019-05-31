# -*- coding: utf-8 -*-
__author__ = 'shiliang'
__date__ = '2019/3/1 23:48'

import math

from thrift.transport import TSocket,TTransport
from thrift.protocol import TBinaryProtocol
from hbase.ttypes import ColumnDescriptor
from hbase import Hbase
from hbase.ttypes import Mutation
from tqdm import tqdm
import xlrd

def connectHBase():
    '''
    连接远程HBase
    :return: 连接HBase的客户端实例
    '''
    # thrift默认端口是9090
    socket = TSocket.TSocket('10.0.86.245',9090) # 10.0.86.245是master结点ip
    socket.setTimeout(5000)
    transport = TTransport.TBufferedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Hbase.Client(protocol)
    socket.open()
    return client

def ListTables(client):
    '''
    列出所有表
    '''
    print(client.getTableNames())

def createTable(client, tableName, *colFamilys):
    '''
    创建新表
    :param client: 连接HBase的客户端实例
    :param tableName: 表名
    :param *colFamilys: 任意个数的列簇名
    '''
    colFamilyList = []
    # 根据可变参数定义列族
    for colFamily in colFamilys:
        col = ColumnDescriptor(name=str(colFamily))
        colFamilyList.append(col)
    # 创建表
    client.createTable(tableName,colFamilyList)
    print('建表成功！')

def deleteTable(client, tableName):
    '''
    删除表
    '''
    if client.isTableEnabled(tableName):
        client.disableTable(tableName)  # 删除表前需要先设置该表不可用
    client.deleteTable(tableName)
    print('删除表{}成功！'.format(tableName))

def deleteTable(client, tableName):
    '''
    删除表
    :param client: 连接HBase的客户端实例
    :param tableName: 表名
    :return:
    '''
    if client.isTableEnabled(tableName):
        client.disableTable(tableName)
    client.deleteTable(tableName)
    print('删除表'+tableName+'成功.')

def insertRow(client, tableName, rowName, colFamily, columnName, value):
    '''
    在指定表指定行指定列簇插入/更新列值
    '''
    mutations = [Mutation(column='{0}:{1}'.format(colFamily, columnName), value=str(value).encode('utf-8').decode('utf-8'))]
    client.mutateRow(tableName, rowName, mutations)
    # print('在{0}表{1}列簇{2}列插入{3}数据成功.'.format(tableName, colFamily, columnName, value))

def scannerGetSelect(client, tableName, columns, startRow, stopRow=None, rowsCnt=7000):
    '''
    依次扫描HBase指定表的每行数据(根据起始行，扫描到表的最后一行或指定行的前一行)
    :param client: 连接HBase的客户端实例
    :param tableName: 表名
    :param columns: 一个包含(一个或多个列簇下对应列名的)列表
    :param startRow: 起始扫描行
    :param stopRow:  停止扫描行(默认为空)
    :param rowsCnt:  需要扫描的行数
    :return MutilRowsDict: 返回一个包含多行数据的字典，以每行行键定位是哪一行
    '''
    # 如果stopRow为空，则使用scannerOpen方法扫描到表最后一行
    if stopRow is None:
        scannerId = client.scannerOpen(tableName, startRow, columns)
    # 如果stopRow不为空，则使用scannerOpenWithStop方法扫描到表的stopRow行
    else:
        scannerId = client.scannerOpenWithStop(tableName, startRow, stopRow, columns)
    results = client.scannerGetList(scannerId, rowsCnt)
    # 如果查询结果不为空，则传入行键值或列值参数正确
    if results:
        MutilRowsDict = {}
        for result in results:
            RowDict = {}          # 一个包含一行所有列簇:列值字典的字典
            colFamilyDict = {}    # 一个包含当前列簇下所有的列值的字典
            preColFamily = None      # 记录前一次循环的列簇值，为空表示遍历该列簇的第一个列值起
            cnt = 0                  # 循环计数器
            for key, TCell_value in result.columns.items():
                cnt += 1
                # 获取该行行键
                rowKey = result.row
                # 由于key值是'列簇:列名'形式,所以需要通过split函数以':'把列名分割出来
                colFamily_colName = key.split(':') # 一个含有1.列簇2.列名的列表
                colFamily = colFamily_colName[0]  # 列簇
                colName = colFamily_colName[1]    # 列名
                # 如果本次列簇为空或和上次循环的列簇相同，则每个列值归属为colFamilyDict字典中并更新上一次列簇的记录
                if (preColFamily is None) or preColFamily == colFamily:
                    colFamilyDict[colName] = TCell_value.value
                    preColFamily = colFamily  # 记录上一次列簇名
                # 如果本次列簇和上次循环的列簇不相同，则把含有列值的colFamilyDict归属为RowDict字典中并清空colFamilyDict字典和preColFamily记录
                else:
                    RowDict[preColFamily] = colFamilyDict
                    colFamilyDict = {}
                    colFamilyDict[colName] = TCell_value.value
                    preColFamily = None
                # 若是最后一次迭代，则把含有列值的colFamilyDict归属为RowDict字典中
                if cnt == len(result.columns.items()):
                    RowDict[colFamily] = colFamilyDict
            # 把当前含有多个列值信息的行的字典和改行行键存储在MutilRowsDict中
            MutilRowsDict[rowKey] = RowDict
        return MutilRowsDict
    # 如果查询结果为空，则传入行键值或列值参数错误，返回空列表
    else:
        return []


def xlsx2HBase(client, xlsx_Path, sheetNum, tableName, colFamily_per, year):
    '''
    xlsx数据上传到HBase中
    :param client: 连接HBase的客户端实例
    :param xlsx_Path: xlsx文件所在地址
    :param sheetNum: sheet序号
    :param tableName: 表名
    :param colFamily_per: 论文信息列簇
    :param colFamily_cre: 作者列簇
    :param colFamily_aff: 机构列簇
    :param colFamily_try: 国家列簇
    :param year: 年份
    '''
    # 1.打开所在工作簿
    data = xlrd.open_workbook(xlsx_Path)
    # 2.获取工作簿中的sheet
    sheet = data.sheets()[sheetNum]
    # 3.获取当前sheet的行数(含表头)
    nRows = sheet.nrows
    # 从第1行遍历到第nRows-1行,tqdm()使用进度条
    for RowNum in tqdm(range(1,nRows)):
    # for RowNum in tqdm(range(1,10)):
        rowName = year+'{:0>4d}'.format(RowNum) # 根据年份和行值拼接成字符串形成rowKey
        for ColNum in range(0,3):               # 从第0列遍历到第2列
            value = sheet.cell(RowNum, ColNum).value   # 单元格信息
            # 对于发表频数，只保留整数
            if ColNum == 2:
                value = int(value)
            header = sheet.cell(0, ColNum).value       # 每列的表头信息
            insertRow(client, tableName, rowName, colFamily_per, header, value)
            # print('第'+rowName+'行'+header+'列插入数据成功.')

# def xlsx2HBase(client, xlsx_Path, sheetNum, tableName, colFamily1, colFamily2, year):
#     '''
#     xlsx数据上传到HBase中
#     :param client: 连接HBase的客户端实例
#     :param xlsx_Path: xlsx文件所在地址
#     :param sheetNum: sheet序号
#     :param tableName: 表名
#     :param colFamily1: 列簇1
#     :param colFamily2: 列簇2
#     :param year: 年份
#     '''
#     # 1.打开所在工作簿
#     data = xlrd.open_workbook(xlsx_Path)
#     # 2.获取工作簿中的sheet
#     sheet = data.sheets()[sheetNum]
#     # 3.获取当前sheet的行数(含表头)
#     nRows = sheet.nrows
#     # 从第1行遍历到第nRows-1行,tqdm()使用进度条
#     for RowNum in tqdm(range(1,nRows)):
#         rowName = year+'{:0>4d}'.format(RowNum) # 根据年份和行值拼接成字符串形成rowKey
#         for ColNum in range(2,5):               # 从第2列遍历到第4列
#             value = sheet.cell(RowNum, ColNum).value  # 单元格信息
#             if str(value) == '0' or str(value) == '0.0':
#                 continue
#             header = sheet.cell(0, ColNum).value  # 每列的表头信息
#             insertRow(client, tableName, rowName, colFamily_per, header, value)
#             # print('第'+rowName+'行'+header+'列插入数据成功.')
#         for ColNum in range(5,39):  # 从第5列遍历到第46列
#             value = sheet.cell(RowNum, ColNum).value   # 单元格信息
#             if str(value) == '0' or str(value) == '0.0':
#                 continue
#             header = sheet.cell(0, ColNum).value  # 每列的表头信息
#             insertRow(client, tableName, rowName, colFamily2, header, value)
#             # print('第'+rowName+'行'+header+'列插入数据成功.')


if __name__ == '__main__':
    # tableName = '2018AAAI' # 数据库表名
    # tableName = 'trash' # 数据库表名
    # tableName = 'p5_AAAI_aff_all' # 数据库表名
    tableName = 'p5_AAAI_author_all' # 数据库表名
    colFamily_per = 'paper'          # 论文信息列簇
    colFamily_cre = 'creator'        # 作者列簇
    colFamily_aff = 'affiliation'    # 机构列簇
    colFamily_try = 'country'        # 国家列簇
    colFamily_aut1st = 'info'          # 论文信息列簇
    # colFamily_aut1st = 'author_1st'          # 论文信息列簇
    colFamily_autAll = 'author_all'        # 作者列簇
    colFamily_aff1st = 'aff_1st'        # 机构列簇
    colFamily_affAll = 'aff_all'        # 国家列簇
    xlsx_Path = r'C:\Users\Administrator\Desktop\2014-2017.xlsx'
    # xlsx_Path = r'C:\Users\Administrator\Desktop\statistic_data.xlsx'
    sheetNum = 12
    # year = '2018'
    year = 'p5_'
    # 连接HBase数据库，返回客户端实例
    client = connectHBase()
    # xlsx数据上传到HBase中
    # xlsx2HBase(client, xlsx_Path, sheetNum, tableName, colFamily_aut1st, year)
    # 创建表
    # createTable(client, tableName, 'info')
    # createTable(client, tableName, colFamily_per, colFamily_cre, colFamily_aff, colFamily_try)
    # 插入或更新列值
    # insertRow(client, tableName, '20180936', 'creator_info', 'affiliation2', 'Ecole Polytechnique Fédérale de Lausanne (EPFL)')
    # 删除整表
    # deleteTable(client, tableName)
    # 依次扫描HBase指定表的每行数据(根据起始行，扫描到表的最后一行或指定行的前一行)
    # MutilRowsDict = scannerGetSelect(client, tableName, ['creator_info:affiliation2'], '20180936')
    # MutilRowsDict = scannerGetSelect(client, tableName, ['paper:title','creator'], '20180291', '20180291')
    # print(MutilRowsDict)
    # 列出所有表名
    ListTables(client)
