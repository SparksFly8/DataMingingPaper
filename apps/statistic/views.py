from django.shortcuts import render
from django.views.generic.base import View


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


