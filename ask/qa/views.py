from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from .models import Question, QuestionManager, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions(request):
    lquestions = QuestionManager.new()
    paginator, page = paginate(request, lquestions)
    return render (request, 'qa/new_questions.html', {
      'questions': page,
      'paginator': paginator,
    })

def popular_questions(request):
    pquestions = QuestionManager.popular()
    paginator, page = paginate(request, pquestions)
    return render (request, 'qa/popular_questions.html', {
      'questions': page,
      'paginator': paginator,
    })

def question_text(request):
    qid = int(request.GET.get('page', 1))
    q = get_object_or_404(Question, id=qid)
    a = Answer.objects.filter(question=qid).order_by('-added_at')
    return render(request, 'qa/question.html', {'question': q, 'answers': a, })


def paginate(request, sqs):
    # get limit
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    # if limit is too high, normalize it
    if limit > 100:
        limit = 10
    paginator = Paginator(sqs, limit)
    # get current page
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(sqs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page