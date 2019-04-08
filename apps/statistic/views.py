from django.shortcuts import render
from django.views.generic.base import View

from .connect_hbase import connectHBase, scannerGetSelect
from .xlsx2mysql2django import connectMySQL, selectCountry
from .models import AffDistribute

'''
机构国家分布View
'''
class affDistributeView(View):
    def get(self, request):
        USDict = AffDistribute.objects.all().filter(country='United States')
        ChinaDict = AffDistribute.objects.all().filter(country='China')
        SingaporeDict = AffDistribute.objects.all().filter(country='Singapore')
        HKDict = AffDistribute.objects.all().filter(country='Hong Kong')
        AustraliaDict = AffDistribute.objects.all().filter(country='Australia')
        UKDict = AffDistribute.objects.all().filter(country='United Kingdom')
        JapanDict = AffDistribute.objects.all().filter(country='Japan')
        GermanyDict = AffDistribute.objects.all().filter(country='Germany')
        IndiaDict = AffDistribute.objects.all().filter(country='India')
        CanadaDict = AffDistribute.objects.all().filter(country='Canada')
        return render(request, 'AffDistribute.html', {
            'USDict':USDict,
            'ChinaDict':ChinaDict,
            'SingaporeDict':SingaporeDict,
            'HKDict':HKDict,
            'AustraliaDict':AustraliaDict,
            'UKDict':UKDict,
            'JapanDict':JapanDict,
            'GermanyDict':GermanyDict,
            'IndiaDict':IndiaDict,
            'CanadaDict':CanadaDict,
        })

'''
会议论文接受率View
'''
class acceptRateView(View):
    def get(self, request):
        return render(request, 'accept_rate.html', {})

'''
会议论文统览View
'''
class allSessionView(View):
    def get(self, request):
        tableName = '2018AAAI'  # 数据库表名
        startRow = '20180001'
        # 连接HBase数据库，返回客户端实例
        client = connectHBase()
        titleCreatorDict = scannerGetSelect(client, tableName, ['paper:title','creator'], startRow)
        return render(request, 'allSession.html', {
            'titleCreatorDict': titleCreatorDict,
        })

'''
论文详情页面View
'''
class sessionDetailView(View):
    def get(self, request, rowKey):
        tableName = '2018AAAI'  # 数据库表名
        startRow = endRow = rowKey
        # 连接HBase数据库，返回客户端实例
        client = connectHBase()
        rowDict = scannerGetSelect(client, tableName, ['creator','affiliation','country','paper'], startRow, endRow)
        # 由于hbase获取数据按照内在索引有小到大排序，故暂无法顺序获取，索引号可由debug查到
        for row_key,rowValueDict in rowDict.items():  # 获取rowKey对应的字典
            creatorList = [] # 对应1.affiliation、2.country和3.creator三个值的多个作者的列表
            for i in range(0, rowValueDict['creator'].__len__()):
                creatorList.append([])
            for colName,colValue in rowValueDict.items():
                if colName == 'paper':
                    continue
                cnt = 0  # creatorDict索引
                for colNameNum,colValueNum in colValue.items():
                    creatorList[cnt].append(colValueNum)
                    cnt += 1

            return render(request, 'paper_info.html', {
                'paperDict': rowValueDict['paper'],
                'creatorList': creatorList,
                'rowkey': row_key,  # 日后可能会用到的参数
            })

'''
词云图View
'''
class wordCloudView(View):
    def get(self, request):
        return render(request, 'wordcloud.html', {})

'''
作者统计View
'''
class authorRankView(View):
    def get(self, request):
        tableName_aut_1st = '2018AAAI_author_1st'  # 数据库表名
        tableName_aut_all = '2018AAAI_author_all'  # 数据库表名
        startRow = '20180001'
        # 连接HBase数据库，返回客户端实例
        client = connectHBase()
        author_1stDict = scannerGetSelect(client, tableName_aut_1st, ['info'], startRow)
        author_allDict = scannerGetSelect(client, tableName_aut_all, ['info'], startRow)
        return render(request, 'author_rank.html', {
            'author_1stDict': author_1stDict,
            'author_allDict': author_allDict,
        })

'''
机构统计View
'''
class affRankView(View):
    def get(self, request):
        tableName_aff_1st = '2018AAAI_aff_1st'  # 数据库表名
        tableName_aff_all = '2018AAAI_aff_all'  # 数据库表名
        startRow = '20180001'
        # 连接HBase数据库，返回客户端实例
        client = connectHBase()
        aff_1stDict = scannerGetSelect(client, tableName_aff_1st, ['info'], startRow)
        aff_allDict = scannerGetSelect(client, tableName_aff_all, ['info'], startRow)
        return render(request, 'aff_rank.html', {
            'aff_1stDict': aff_1stDict,
            'aff_allDict': aff_allDict,
        })

'''
作者关系图谱View
'''
class authorMapView(View):
    def get(self, request):
        return render(request, 'authorMap.html', {})
