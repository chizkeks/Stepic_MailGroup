from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
import ask.qa.models as md

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions(request):
    lquestions = md.QuestionManager.new()
    paginator, page = paginate(request, lquestions)
    paginator.baseurl = '/?page='
    return render (request,'templates/new_questions.html', {
      'questions': page.object_list,
      'paginator': paginator, 'page': page,
    })

def popular_questions(request):
    pquestions = md.QuestionManager.popular()
    paginator, page = paginate(request, pquestions)
    paginator.baseurl = '/popular/?page='
    return render (request,'templates/popular_questions.html', {
      'questions': page.object_list,
      'paginator': paginator, 'page': page,
    })

def question_text(request, question_id):

    """POST and GET methods needed"""
    q = get_object_or_404(md.Question, id=question_id)
    a = q.answer_set
    #a = Answer.objects.filter(question=question_id).order_by('-added_at')
    return render(request, 'qa/question.html',  {
      'questions': page.object_list,
      'paginator': paginator, 'page': page,
    })



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