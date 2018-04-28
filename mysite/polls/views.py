from django.shortcuts import get_object_or_404, render
from django.http import Http404

from django.http import HttpResponse
# from django.template import loader

from .models import Question


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return JsonResponse({'test':1})
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = { 'latest_question_list': latest_question_list, }
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. Django provides a shortcut. Here’s the detail() view
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
