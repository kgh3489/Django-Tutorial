from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #클라이언트가 polls를 호출하면 views.index라는 view를 호출
    #views.py에서 index의 request인 Hello world를 반환
    path('', views.index, name='index'),
    #path마다 동일 과정
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
] 
#<int:question_id>/vote/ 는 장고 url패턴. 이 패턴대로 입력되면 그에 해당되는 view를 호출
#views.py의 파라미터(question_id)와 동일해야됨!