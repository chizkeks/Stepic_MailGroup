from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class QuestionManager(models.Manager):
    def new(self):
        new_questions = Question.objects.all().order_by('-id')
        return new_questions

    def popular(self):
        pop_questions = Question.objects.order_by('-rating')
        return pop_questions

class Question(models.Model):
    title = models.TextField()
    text = models.TextField(max_length=255)
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.TextField()
    likes = models.ManyToManyField(
        User, related_name="likes", blank=True)
    objects = QuestionManager()

    def get_url(self):
        return reverse('question_details', kwargs={'id': self.id})

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('question', kwargs={'question_id': self.question.id})

    def __unicode__(self):
        return "Answer by {0} to question {1}: {2}...".\
            format(self.author.username, self.question.id, self.text[:50])
# Create your models here.
