# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/3/25 0:30'

import pymysql
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
    sheet = data.sheets('distribute')
    nRowlist = [116, 59, 6, 6, 15, 18, 19, 24, 8, 10] # 10个国家机构列在xlsx的行数
    # 从第1行遍历到第nRows-1行,tqdm()使用进度条
    ColNum = 0  # 列数
    for nRows in nRowlist:
        for RowNum in tqdm(range(1, nRows)):
            aff = sheet.cell(RowNum, ColNum).value        # 读取单元格(机构)信息
            country = sheet.cell(0, ColNum).value         # 读取单元格(国家)信息
            count = sheet.cell(RowNum, ColNum+1).value    # 读取单元格(频数)信息
            connectMySQL(aff, country, count)
        ColNum += 2

def connectMySQL(aff, country, count):
    pass


if __name__ == '__main__':
    xlsx_Path = 'C:\\Users\\Administrator\\Desktop\\data.xlsx'