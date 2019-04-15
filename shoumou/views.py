from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    params = {
        'title':'Hello/Index',
        'msg':'これは、サンプルで作ったページです。',
        'goto':'next',
        }
    
    return render(request, 'index.html', params)

def next(request):
    params = {
        'title':'Hello/Next',
        'msg':'もう一つのページです。',
        'goto':'index',
        }
    
    return render(request, 'index.html', params)
