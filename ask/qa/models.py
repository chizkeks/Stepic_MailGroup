from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class QuestionManager(models.Manager):
    def new(self):
        new_questions = Question.objects.order_by('-added_at')
        return new_questions
    def popular(self):
        pop_questions = Question.objects.order_by('-rating')
        return pop_questions

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, related_name="post_author")
    likes = models.ManyToManyField(User, related_name='likes')

    def get_url(self):
        return reverse('question', kwargs={'question_id': self.id})

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

#class Likes(models.Model):
  #  question = models.ForeignKey(
   #     Question,
   #     related_name="question_likes"
  #  )
 #   user = models.ForeignKey(
 #       User,
 #       related_name="users_likes"
 #   )
# Create your models here.
