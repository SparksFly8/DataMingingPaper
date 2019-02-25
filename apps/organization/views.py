from django.shortcuts import render
from django.views.generic import View

'''
课程机构列表View
'''
class OrgView(View):
    def get(self, request):
        return render(request, 'org-list.html', {})