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
会议论文统览View(2014~2018)
'''
class allSessionView(View):
    def get(self, request):
        # 连接HBase数据库，返回客户端实例
        client = connectHBase()
        titleCreDict2018 = scannerGetSelect(client, '2018AAAI', ['paper:title','creator'], '20180001')
        titleCreDict2017 = scannerGetSelect(client, '2017AAAI', ['paper:title','creator'], '20170001')
        titleCreDict2016 = scannerGetSelect(client, '2016AAAI', ['paper:title','creator'], '20160001')
        titleCreDict2015 = scannerGetSelect(client, '2015AAAI', ['paper:title','creator'], '20150001')
        titleCreDict2014 = scannerGetSelect(client, '2014AAAI', ['paper:title','creator'], '20140001')
        return render(request, 'allSession.html', {
            'titleCreDict2018': titleCreDict2018,
            'titleCreDict2017': titleCreDict2017,
            'titleCreDict2016': titleCreDict2016,
            'titleCreDict2015': titleCreDict2015,
            'titleCreDict2014': titleCreDict2014,
        })

'''
论文详情页面View
'''
class sessionDetailView(View):
    def get(self, request, rowKey):
        tableName = rowKey[:4]+'AAAI'  # 根据行键前四位合成数据库表名
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
        # 连接HBase数据库，返回客户端实例
        client = connectHBase()
        author_1stDict2018 = scannerGetSelect(client, '2018AAAI_author_1st', ['info'], '20180001')
        author_allDict2018 = scannerGetSelect(client, '2018AAAI_author_all', ['info'], '20180001')
        author_1stDict_p3 = scannerGetSelect(client, 'p3_AAAI_author_1st', ['info'], 'p3_0001')
        author_allDict_p3 = scannerGetSelect(client, 'p3_AAAI_author_all', ['info'], 'p3_0001')
        author_1stDict_p5 = scannerGetSelect(client, 'p5_AAAI_author_1st', ['info'], 'p5_0001')
        author_allDict_p5 = scannerGetSelect(client, 'p5_AAAI_author_all', ['info'], 'p5_0001')
        return render(request, 'author_rank.html', {
            'author_1stDict2018': author_1stDict2018,
            'author_allDict2018': author_allDict2018,
            'author_1stDict_p3': author_1stDict_p3,
            'author_allDict_p3': author_allDict_p3,
            'author_1stDict_p5': author_1stDict_p5,
            'author_allDict_p5': author_allDict_p5,
        })

'''
机构统计View
'''
class affRankView(View):
    def get(self, request):
        # 连接HBase数据库，返回客户端实例
        client = connectHBase()
        aff_1stDict2018 = scannerGetSelect(client, '2018AAAI_aff_1st', ['info'], '20180001')
        aff_allDict2018 = scannerGetSelect(client, '2018AAAI_aff_all', ['info'], '20180001')
        aff_1stDict_p3 = scannerGetSelect(client, 'p3_AAAI_aff_1st', ['info'], 'p3_0001')
        aff_allDict_p3 = scannerGetSelect(client, 'p3_AAAI_aff_all', ['info'], 'p3_0001')
        aff_1stDict_p5 = scannerGetSelect(client, 'p5_AAAI_aff_1st', ['info'], 'p5_0001')
        aff_allDict_p5 = scannerGetSelect(client, 'p5_AAAI_aff_all', ['info'], 'p5_0001')
        return render(request, 'aff_rank.html', {
            'aff_1stDict2018': aff_1stDict2018,
            'aff_allDict2018': aff_allDict2018,
            'aff_1stDict_p3': aff_1stDict_p3,
            'aff_allDict_p3': aff_allDict_p3,
            'aff_1stDict_p5': aff_1stDict_p5,
            'aff_allDict_p5': aff_allDict_p5,
        })

'''
作者关系图谱View
'''
class authorMapView(View):
    def get(self, request):
        return render(request, 'authorMap.html', {})
