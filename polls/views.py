from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
#这是用来实验的
def do_wang(request):
    #print('这是主页知道吗')
    return HttpResponse('这是个参数')
def do_app(request):
    return HttpResponse('我是刘银涛')
#计算字数以及字数出现的频率
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

#投票环节
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
    'latest_question_list' : latest_question_list
    }
    return HttpResponse(template.render(context,request))

from django.http import Http404
# '''
def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request,'polls/detail.html',{'question':question})
    #return HttpResponse("You are looking at question %s." % question_id)
def result(request,question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)