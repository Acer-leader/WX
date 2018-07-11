from django.db import models
from time import timezone
import datetime

# Create your models here.
class Question(models.Model):

    question_text = models.CharField(max_length=200)
    '''
    添加该方法使得对象的名称变为应该有的字段
    '''
    def __str__(self):
        return self.question_text
    pub_date = models.DateTimeField('date published')
    #was_published_recently = datetime.datetime.now() - datetime.timedelta(days=1)
class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    poll = models .ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
