# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from nlpweb.nlpmain import main
import json


# Create your views here.

def savefile(file):

    with open(file.name, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return

def getfile(request):
    file = request.FILES.get('file')
    print(file.name)
    # print(file.read())
    # print(file.read().decode("UTF-8"))
    savefile(file)

    file=open(file.name,'r',encoding='utf-8')
    data=file.read()
    file.close()
    # print(data)

    # for line in file.chunks():
    #     print(line.decode("UTF-8"))
    text = main.ENLP(data)  # 返回的数据
    print(text)
    response = {}
    response['text'] = text
    httpResponse = HttpResponse(json.dumps(response), content_type="application/json")
    httpResponse["Access-Control-Allow-Origin"] = "*"
    return httpResponse


def download_file(request):
    httpResponse = FileResponse(open('temp.txt','r',encoding='utf-8').read())
    httpResponse["Access-Control-Allow-Origin"] = "*"
    httpResponse['Content-Type'] = 'application/octet-stream'
    httpResponse['Content-Disposition'] = 'attachment;filename="text.doc"'
    return httpResponse


def save_file(request):
    text = request.POST.get('text')
    text=text.replace("<br>","").strip()
    text=bytes(text, encoding = "utf-8")
    response = {}
    file = open('temp.txt', 'wb')
    file.write(text)
    file.close()
    httpResponse = HttpResponse(json.dumps({'code': '200'}))
    httpResponse["Access-Control-Allow-Origin"] = "*"
    return httpResponse
