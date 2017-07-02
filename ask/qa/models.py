from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        pass
    def popular(self):
        pass

class Question(models.Model):
    title = models.TextField()
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.TextField()
    likes = models.ManyToManyField(
        User,
        through="Likes")
    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    question = models.TextField()
    author = models.TextField()
class Likes(models.Model):
    question = models.ForeignKey(
        Question,
        related_name="question_likes"
    )
    user = models.ForeignKey(
        User,
        related_name="users_likes"
    )
# Create your models here.
