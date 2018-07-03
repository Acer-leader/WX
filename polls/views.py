from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def do_wang(request):
    #print('这是主页知道吗')
    return HttpResponse('这是个参数')
def do_app(request):
    return HttpResponse('我是刘银涛')
def do_home(request):
    return render(request,'home.html')
def do_count(request):
    usre_area = request.GET['text']
    total_count = len(request.GET['text'])
    word_count = {}
    for word in usre_area:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
        sorted_word= sorted(word_count.items(),key=lambda w:w[1],reverse=True)
    return render(request,'count.html',{'count':total_count,'text':usre_area,'word':word_count,'sorted':sorted_word})
def  do_double(request):
    return render(request,'double.html')