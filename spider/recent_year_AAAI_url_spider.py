from lxml import etree
import requests
import pandas as pd
import time

'''
获取AAAI近几年主页的所有论文的URL
'''
url_home17 = 'https://aaai.org/ocs/index.php/AAAI/AAAI17/schedConf/presentations'
url_home16 = 'https://aaai.org/ocs/index.php/AAAI/AAAI16/schedConf/presentations'
url_home15 = 'https://aaai.org/ocs/index.php/AAAI/AAAI15/schedConf/presentations'
url_home14 = 'https://aaai.org/ocs/index.php/AAAI/AAAI14/schedConf/presentations'
start = time.time()
r_home17 = requests.get(url_home17)
print('请求并获取2017主页花费时间：'+str(time.time()-start)+'s')
html17 = r_home17.content
url_sets17 =[]
url_sets17 = etree.HTML(html17).xpath('//*[@id="content"]/table/tr[1]/td[1]/a/@href')
print(url_sets17)
print(len(url_sets17))
df = pd.DataFrame(url_sets17)
df.to_excel('C:\\Users\\Administrator\\Desktop\\2017url.xlsx',sheet_name='Sheet1',na_rep=0,startrow=0,startcol=0,index=False,header=False) #na_rep缺省值填充

# 2016
r_home16 = requests.get(url_home16)
print('请求并获取2016主页花费时间：'+str(time.time()-start)+'s')
html16 = r_home16.content
url_sets16 =[]
url_sets16 = etree.HTML(html16).xpath('//*[@id="content"]/table/tr[1]/td[1]/a/@href')
print(url_sets16)
print(len(url_sets16))
df = pd.DataFrame(url_sets16)
df.to_excel('C:\\Users\\Administrator\\Desktop\\2016url.xlsx',sheet_name='Sheet1',na_rep=0,startrow=0,startcol=0,index=False,header=False) #na_rep缺省值填充

# 2015
r_home15 = requests.get(url_home15)
print('请求并获取2015主页花费时间：'+str(time.time()-start)+'s')
html15 = r_home15.content
url_sets15 =[]
url_sets15 = etree.HTML(html15).xpath('//*[@id="content"]/table/tr[1]/td[1]/a/@href')
print(url_sets15)
print(len(url_sets15))
df = pd.DataFrame(url_sets15)
df.to_excel('C:\\Users\\Administrator\\Desktop\\2015url.xlsx',sheet_name='Sheet1',na_rep=0,startrow=0,startcol=0,index=False,header=False) #na_rep缺省值填充

# 2014
r_home14 = requests.get(url_home14)
print('请求并获取2014主页花费时间：'+str(time.time()-start)+'s')
html14 = r_home14.content
url_sets14 =[]
url_sets14 = etree.HTML(html14).xpath('//*[@id="content"]/table/tr[1]/td[1]/a/@href')
print(url_sets14)
print(len(url_sets14))
df = pd.DataFrame(url_sets14)
df.to_excel('C:\\Users\\Administrator\\Desktop\\2014url.xlsx',sheet_name='Sheet1',na_rep=0,startrow=0,startcol=0,index=False,header=False) #na_rep缺省值填充