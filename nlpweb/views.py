from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
import json


# Create your views here.

def getfile(request):
    file = request.FILES.get('file')
    print(file.name)
    for line in str(file.read()).split('\n'):
        print(line)
    text = 'default'  # 返回的数据
    response = {}
    response['text'] = text
    httpResponse = HttpResponse(json.dumps(response), content_type="application/json")
    httpResponse["Access-Control-Allow-Origin"] = "*"
    return httpResponse


def download_file(request):
    httpResponse = FileResponse(open('temp.txt').read())
    httpResponse["Access-Control-Allow-Origin"] = "*"
    httpResponse['Content-Type'] = 'application/octet-stream'
    httpResponse['Content-Disposition'] = 'attachment;filename="text.txt"'
    return httpResponse


def save_file(request):
    text = request.POST.get('text')
    print(text.strip())
    response = {}
    file = open('temp.txt', 'w')
    file.write(text.strip())
    file.close()
    httpResponse = HttpResponse(json.dumps({'code': '200'}))
    httpResponse["Access-Control-Allow-Origin"] = "*"
    return httpResponse
