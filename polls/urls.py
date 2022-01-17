from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
#<int:question_id>/vote/ 는 장고 url패턴. 이 패턴대로 입력되면 그에 해당되는 view를 호출
#views.py의 파라미터(question_id)와 동일해야됨!