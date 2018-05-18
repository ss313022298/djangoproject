from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



def detail(request, question_id):
    return HttpResponse('this is detail %s'%question_id)


