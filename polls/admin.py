from django.contrib import admin
from .models import Question, Choice

class ChoicInline(admin.TabularInline):
    model = Choice
    extra = 3 #관련된 선택 사항을 위한 슬롯 세 개를 extra로 지정

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoicInline] #Question 안에 Choice를 보이게 함
    list_display = ('question_text', 'pub_date', 'was_published_recently') #객체의 변경 목록 페이지에서 열로 표시 할 필드 이름들의 튜플
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin) #Question 모델을 adimin에 등록
admin.site.register(Choice) #Choice 모델을 adimin에 등록

