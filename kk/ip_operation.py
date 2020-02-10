from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import redirect, render
from django.template import Template, loader, Context

import requests as ipr
import random
import json


def admin(request):
    f = open('kk/ip.txt', 'r')
    datas = []
    for line in f.readlines():
        datas.append(json.loads(line))
    return render(request, 'fip.html', locals())


def ip_create():
    extranet_ip = ipr.get('http://ip.cip.cc/').text
    random_ip = '{}.{}.{}.{}'.format(random.randint(1, 255),
                                     random.randint(0, 255),
                                     random.randint(0, 255),
                                     random.randint(0, 255))
    if random_ip != extranet_ip:
        return random_ip


def ip_add(req):
    n = int(req.GET['ip_num'])
    flag = 0
    while flag < n:
        ip_dict = {}
        ip_dict['src'] = ip_create()
        ip_dict['dest'] = ip_create()
        with open("kk/ip.txt", 'a') as t:
            t.write(json.dumps(ip_dict) + '\n')
        flag += 1

    return render(req, "fip.html")


def ip_delete(req):
    del_ip = req.GET['del_ip']
    del_ip = del_ip.replace('\'', '\"')
    lines = [l for l in open("kk/ip.txt", "r") if l.find(del_ip) != 0]
    fd = open("kk/ip.txt", "w")
    fd.writelines(lines)
    return render(req, "fip.html")


def ip_edit(req):
    pass

def ip_select(req):
    ip_name = req.GET['ip_name']
    f = open("kk/ip.txt", "r")
    for line in f.readlines():
        if ip_name in line:
            print('hanyou')
            ip_json=json.loads(line)
        
    return render(req,"fip.html",locals())