# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/4/9 21:12'

import requests
from lxml import etree
from tqdm import tqdm
import pandas as pd
import xlrd
import time
import re
import multiprocessing
from multiprocessing import Pool

# 全局变量
# headers = {
#     'Cookie': 'OCSSID=sfg10a19had6hfavkctd32otf6',
#     # 'Cookie': 'v=8ULm8Hr%<k:l5rrfgm?a; Qs_lvt…ts=PUbGvneL,qrbGvneL,L6cGvneL',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
#                   '(KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
#     # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
# }
oneSheetList = []  # 一张整表的元数据列表

def getURLlist(openFile, sheetNum, colx, start_rowx):
    '''
    获取excel指定sheet指定列指定范围行的数据
    :param openFile: excel路径
    :param sheetNum: sheet序号
    :param colx: 获取指定列数
    :param start_rowx: 起始行数
    :return urls: 一个包含所有URL的列表
    '''
    # 打开工作簿
    data = xlrd.open_workbook(openFile)
    # 选定sheet
    table = data.sheets()[sheetNum]
    # 获取excel表的指定列,start_rowx=1表示从第2行开始(从0计数)
    urls = table.col_values(colx=colx, start_rowx=start_rowx)
    return urls

def cleanStr(string):
    '''
    清洗字符串,如去除HTML标签等
    :param string: 待清洗字符串
    :return clean_str: 清洗后的较干净字符串
    '''
    # 1.使用strip函数清洗去除每个字符串的首尾\n和\t,此处也可写成\t\n
    clean_str = string.strip('\n\t')
    # 2.使用正则清洗掉HTML标签<>、/**/中的内容
    clean_str = re.compile(r'\<.*?\>|\/\*.*?\*\/').sub('', clean_str)
    return clean_str

def getOneURLMetaData(number, url):
    '''
    使用多进程获取多个URL的元数据
    :param url: url链接(字符串类型)
    :return oneURLList: 一个URL的所有元数据的列表
    '''
    resp = requests.get(url)
    html = resp.content
    # 解析数据
    xml = etree.HTML(html)
    content = xml.xpath('//*[@id="content"]/table/tr/td/text()')
    # 格式化数据
    oneURLList = []      # 存储一个URL包含所有元数据的列表
    creatorList = []  # 当前URL所有作者、机构和国家信息列表,默认为'0'
    title = ''           # 当前URL标题
    abstract = ''        # 当前URL摘要
    keywords = '0'       # 当前URL关键字
    for index, text in enumerate(content):
        # '\xa0'是一行的首元素和尾元素,表示一行的开头或结尾
        if text == '\xa0':
            # 1.判断是否是'Title'行
            if content[index+2] == 'Title':
                title = content[index + 4]            # 保存Title
                title = cleanStr(title)               # 清洗title
                continue
            if content[index+3] == 'Abstract':
                abstract = content[index + 4]         # 保存Abstract
                continue
            if content[index+3] == 'Keyword(s)':
                # 如果Keyword(s)不为空则填,为空则默认字符'0'
                if content[index+4] != '\xa0':
                    keywords = content[index + 4]     # 保存Keyword(s)
                    keywords = cleanStr(keywords)     # 清洗keywords
                continue
            if content[index+2] == 'Creator':
                clean_creator = cleanStr(content[index + 4])
                lst = clean_creator.split('; ')     # 使用切片函数以"; "把字符串分割成三份，返回一个列表
                for num, info in enumerate(lst):  # 因存在官网元数据少录入情况,故对于少录入数据项默认为'0'
                    # 如果是官网数据录入错误,超过三个数据,则直接跳出循环
                    if num > 2:
                        break
                    creatorList.append(info)  # 作者名字、机构、国家
                    # 如果是官网数据录入错误, 少于三个数据, 则最最后一个元素补'0'
                    if len(lst) < 3 and num == 1:
                        creatorList.append('0')  # 作者名字、机构、国家
                continue
    oneURLList.append(number)
    oneURLList.append(title)
    oneURLList.append(abstract)
    oneURLList.append(keywords)
    oneURLList.append(creatorList)
    # 存储oneURLList的最后一个元素
    creatorList = oneURLList[-1]
    # 删除oneURLList的最后一个元素,切片取列表中的[0,-1)
    oneURLList = oneURLList[:-1]
    # 将creator列表拆开一个一个添加到oneURLList后
    for info in creatorList:
        oneURLList.append(info)
    print('已完成第' + str(number) + '个url的爬取+解析+清洗')
    return oneURLList

def getMetaData(urls, topCount=None):
    '''
    获取所有url的元数据列表,返回一个列表
    :param urls: URL列表
    :param topCount: URL列表中前几个URL的个数(可选参数)
    '''
    urlsList = []
    if topCount is None:
        urlsList = urls
    else:
        for i in range(topCount):
            urlsList.append(urls[i])
    print('当前环境CPU核数是：%d核' % multiprocessing.cpu_count())
    p = Pool(10)  # 进程池
    for number, url in enumerate(urlsList):
        oneSheetList.append(p.apply_async(getOneURLMetaData, args=(number+1, url)))
    p.close()
    p.join()  # 运行完所有子进程才能顺序运行后续程序
    for index, result in enumerate(oneSheetList):
        oneSheetList[index] = result.get()


def list2excel(saveFile, oneSheetList, startrow, startcol=2, sheet_name='Sheet1'):
    '''
    列表写入到excel中的指定行和指定列中
    :param saveFile: 存储excel文件路径
    :param oneSheetList: 一个存储一个Sheet元数据的列表
    :param startrow: 该url位于excel表格中的行数
    :param startcol: 写入excel表格中的起始列
    :param sheet_name: 写入的sheet页名称
    :return:
    '''
    df = pd.DataFrame(oneSheetList)
    # df = df.T  # 矩阵转置,变成行向量
    # na_rep缺省值填充参数;index=False去掉行索引;header=False去掉表头
    df.to_excel(saveFile, sheet_name=sheet_name, startrow=startrow, startcol=startcol,
                  index=False, header=False)
    print('数据写入excel成功.')


if __name__ == '__main__':
    openFile = r'/root/Desktop/2014-2017.xlsx'
    saveFile = r'/root/Desktop/2014(多进程代码).xlsx'
    # 从excel中获取url,返回一个列表
    urls = getURLlist(openFile, sheetNum=3, colx=1, start_rowx=1)
    # 通过多进程获取所有URL中的元数据,存储在oneSheetList列表中
    start = time.time()
    getMetaData(urls)
    print('多进程总爬取+解析耗时：%.5f秒' % float(time.time() - start))
    # 最后对嵌套列表的列表oneSheetList进行排序,key输入的是函数,item[0]表示列表的第1个元素
    oneSheetList.sort(key=lambda item: item[0], reverse=False)
    # # 存储到excel中
    list2excel(saveFile, oneSheetList, startrow=0, startcol=0, sheet_name='Sheet1')
