# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/3/6 16:46'

from django.urls import path, include, re_path
from .views import affDistributeView, acceptRateView, allSessionView, sessionDetailView, wordCloudView, authorRankView, affRankView, authorMapView, topicModelView

app_name = 'statistic'

urlpatterns = [
    path('affDistribute/', affDistributeView.as_view(), name='affDistribute'),
    path('acceptRate/', acceptRateView.as_view(), name='acceptRate'),
    path('allSession/', allSessionView.as_view(), name='allSession'),
    path('wordcloud/', wordCloudView.as_view(), name='wordcloud'),
    path('authorRank/', authorRankView.as_view(), name='authorRank'),
    path('affRank/', affRankView.as_view(), name='affRank'),
    path('authorMap/', authorMapView.as_view(), name='authorMap'),
    path('topicModel/', topicModelView.as_view(), name='topicModel'),
    re_path('sessionDetail/(?P<rowKey>.*)/', sessionDetailView.as_view(), name='sessionDetail'),
]
