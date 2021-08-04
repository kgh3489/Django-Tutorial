import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.question_text #cmd에서 문자로 출력

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) #현재 시간 - 하루 전 시간

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text #cmd에서 문자로 출력
        
    #Choice 테이블이 Question테이블을 참조