# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/3/25 0:30'

import pymysql.connections
import xlrd
from tqdm import tqdm

def xlsx2mysql(xlsx_Path):
    '''
    从xlsx读取数据存储到mysql中
    :param xlsx_Path: xlsx在本地的路径
    '''
    # 1.打开所在工作簿
    data = xlrd.open_workbook(xlsx_Path)
    # 2.获取工作簿中的sheet
    sheet = data.sheets()[4]
    nRowlist = [116, 59, 6, 6, 15, 18, 19, 24, 8, 10] # 10个国家机构列在xlsx的行数
    # 从第1行遍历到第nRows-1行,tqdm()使用进度条
    ColNum = 0  # 列数
    for nRows in nRowlist:
        for RowNum in tqdm(range(1, nRows)):
            aff = sheet.cell(RowNum, ColNum).value        # 读取单元格(机构)信息
            country = sheet.cell(0, ColNum).value         # 读取单元格(国家)信息
            count = sheet.cell(RowNum, ColNum+1).value    # 读取单元格(频数)信息
            db = connectMySQL() # 连接数据库
            insertValue(db, 'statistic_affdistribute', aff, country, count) # 插入数据
        ColNum += 2

def connectMySQL():
    '''
    连接MySQL数据库
    :return db: 数据库
    '''
    host = 'localhost'
    user = 'root'
    password = 'root'
    database = 'datamingingpaper'
    # 连接数据库
    db = pymysql.connect(host, user, password, database)
    return db

def insertValue(db, tableName, aff, country, count):
    '''
    向MySQL插入数据
    :param db: 数据库
    :param tableName: 表名
    :param aff: 机构
    :param country: 国家
    :param count: 发表频数
    '''
    # 方法获取操作游标
    cursor = db.cursor()
    # 编辑SQL语句
    SQL = "INSERT INTO {0}(affiliation, country, count)" \
          "VALUES ('{1}', '{2}', '{3}')".format(tableName, aff, country, count)
    try:
        # 执行sql语句
        cursor.execute(SQL)
        # 提交到数据库执行
        db.commit()
    except:
        db.rollback()  # 异常则回滚
    # 关闭数据库连接
    db.close()

def selectCountry(db, tableName, country):
    '''
    依据国家查询到对应数据
    :param db: 数据库
    :param tableName: 表名
    :param country: 国家
    :return resultDict: 字典结果集
    '''
    # 方法获取操作游标
    cursor = db.cursor()
    # 编辑SQL语句
    SQL = "SELECT id,affiliation,count FROM {0} WHERE country='{1}'".format(tableName, country)
    try:
        # 执行sql语句
        cursor.execute(SQL)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 创建一个空结果字典，用以把元组转换为字典
        resultDict = {}
        for result in results:
            emptyDict = {}
            key = result[0]  # id
            emptyDict['affiliation'] = result[1]  # 机构名称
            emptyDict['count'] = result[2]  # 发表频数
            resultDict[key] = emptyDict
        print(resultDict)
    except:
        print("查找不到数据.")
    # 关闭数据库连接
    db.close()
    return resultDict



if __name__ == '__main__':
    xlsx_Path = 'C:\\Users\\Administrator\\Desktop\\data.xlsx'
    # xlsx2mysql(xlsx_Path)


