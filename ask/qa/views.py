from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage
from .models import Question, QuestionManager
from django.core.urlresolvers import reverse

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator

def fresh_questions(request):
    nq = QuestionManager.new()
    page, paginator = paginate(request, nq)
    paginator.baseurl = reverse('new_questions') + '?page='

    return render(request, 'qa/new.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def popular(request):
    pq = QuestionManager.popular()
    page, paginator = paginate(request, pq)
    paginator.baseurl = reverse('popular') + '?page='

    return render(request, 'qa/popular.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def question(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    a = q.answer_set.all()
    #a = Answer.objects.filter(question=question_id).order_by('-added_at')
    return render(request, 'qa/question.html', {
        'question': q,
        'answers': a,
    })
