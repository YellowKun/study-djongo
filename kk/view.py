from django.http import HttpResponse,JsonResponse,FileResponse
from django.shortcuts import redirect,render
from django.template import Template,loader,Context


import requests as ipr
import random


# def ip(requests):
#     r = ipr.get('http://ip.cip.cc/')
#     ip=r.text
    
#     return HttpResponse(ip)

def form(request):
    return render(request,'fip.html')
 
# 接收请求数据
def fip(request):  
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        ip = []
        ipc = ipr.get('http://ip.cip.cc/').text
        ipq = int(request.GET['q'])
        for i in range(ipq):

            ip.append(str(i+1)+":"+ipc+" -> "+'{}.{}.{}.{}'.format(random.randint(1,255),random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            
        message = ip
    else:
        message = ["你输入了空值！"]
    return render(request,'fip.html',locals())


