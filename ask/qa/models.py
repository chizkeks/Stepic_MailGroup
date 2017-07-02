from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.TextField() #заголовок вопроса
    text = models.TextField() #полный текст вопроса
    added_at = models.DateTimeField(blank = True, auto_now_add=True) #дата добавления вопроса
    rating = models.IntegerField(default = 0) #рейтинг вопроса (число)
    author = models.TextField() #автор вопроса
    likes = models.ManyToManyField(
        User,
        through="Likes") #список пользователей, поставивших "лайк"
    objects = QuestionManager()

class Answer (models.Model):
    text = models.TextField() #текст ответа
    added_at = models.DateTimeField(blank = True, auto_now_add=True) #дата добавления ответа
    question = models.TextField();
    author = models.TextField() #автор вопроса

class Likes(models.Model):
    question = models.ForeignKey(
        Question,
        related_name="question_likes"
    )
    user = models.ForeignKey(
        User,
        related_name="users_likes"
    )

class QuestionManager (models.Manager):
    def new(self):
        pass
    def popular(self):
        pass
# Create your models here.
