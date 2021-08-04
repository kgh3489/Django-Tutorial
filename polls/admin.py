from django.contrib import admin
from .models import Question, Choice

admin.site.register(Question) #Question 모델을 adimin에 등록
admin.site.register(Choice) #Choice 모델을 adimin에 등록

