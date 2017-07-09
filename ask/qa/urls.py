from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^login/.*$', include('qa.urls')),
    url(r'^signup/.*$', include('qa.urls')),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question_text, name='question'),
    url(r'^ask/.*$', include('qa.urls')),
    url(r'^popular/.*$', views.popular_questions),
    url(r'^new/.*$', views.new_questions),
]