from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question,Choice
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
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
# 首页展示所有问题
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
    'latest_question_list' : latest_question_list
    }
    return HttpResponse(template.render(context,request))


# 查看所有问题
def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request,'polls/detail.html',{'question':question})

# 查看投票结果
def result(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question,})

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
