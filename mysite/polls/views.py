from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.utils import timezone
# Create your views here.


# def index(request):
    # 获取question全部对象，进行排序选取最新5个问题
    # latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    # 将对象以字典形式传输
    # context = {'latest_question_list': latest_question_list}
    # 使用render(request, 模板, 参数)
    # return render(request, 'polls/index.html', context)

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     return Question.objects.order_by('-pub_date')[:3]

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

# def detail(request, question_id):
    # 通过问题id得到question对象
    # question = get_object_or_404(Question, pk=question_id)
    # 传输给模板
    # return render(request, 'polls/detail.html', {'question': question})
class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())




def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {'question': question,'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



# def results(request, question_id):

    # question = get_object_or_404(Question, pk=question_id)
    #
    # return render(request, 'polls/results.html', {'question': question})
class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'




