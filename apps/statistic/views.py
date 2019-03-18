from django.shortcuts import render
from django.views.generic.base import View

from .connect_hbase import connectHBase, scannerGetSelect

'''
机构国家分布View
'''
class affDistributeView(View):
    def get(self, request):
        return render(request, 'AffDistribute.html', {})

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
