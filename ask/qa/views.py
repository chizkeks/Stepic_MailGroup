from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage
from .models import Question, Answer
from django.core.urlresolvers import reverse
from .forms import AnswerForm, AskForm



# Create your views here.

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
    nq = Question.objects.all().order_by('-id')
    page, paginator = paginate(request, nq)
    paginator.baseurl = reverse('new_questions') + '?page='

    return render(request, 'qa/new.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def popular(request):
    pq = Question.objects.order_by('-rating')
    page, paginator = paginate(request, pq)
    paginator.baseurl = reverse('popular') + '?page='

    return render(request, 'qa/popular.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def questions(request, qid):
    q = get_object_or_404(Question, id=qid)
    a = q.answer_set.all()
    #a = Answer.objects.filter(question=question_id).order_by('-added_at')
    form = AnswerForm(initial = {'question': qid})
    return render(request, 'qa/question.html', {
        'question': q,
        'answers': a,
        'form': form,
    })

def ask_q(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask_q.html', {'form': form})

def answer_q(request):
      if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = answer.get_url()
            return HttpResponseRedirect(url)
      return HttpResponseRedirect('/')
