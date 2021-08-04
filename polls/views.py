from polls.models import Question
from django.http import response
from django.http.response import HttpResponse
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404 #단축기능 제공

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context) # render를 사용하여 HttpResponse와 request를 사용 안 함.
    #context = {'latest_question_list': latest_question_list,} # temlplate에 데이터를 전달
    #output = ', '.join([q.question_text for q in latest_question_list]) # Question 데이터 중에서 출판일자를 정렬하여 5개까지만 가져오고 그것을 콤마로 연결

# 새로운 index()뷰 하나를 호출했을 때,
# 시스템에 저장된 최소한의 5개의 투표 질문이 콤마로 분리되어 발행일에 따라 출력

def detail(request, question_id):
    #1
    #return HttpResponse("You're looking at question %s." % question_id)

    #2
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})

    #3
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
def results(request, question_id):
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

#클라이언트로부터 request를 받으면 response를 돌려줌