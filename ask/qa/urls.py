from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^login/.*$', views.test),
    url(r'^signup/.*$', views.test),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question_text, name='question'),
    url(r'^ask/.*$', views.test),
    url(r'^popular/.*$', views.popular_questions),
    url(r'^new/.*$', views.new_questions),
]