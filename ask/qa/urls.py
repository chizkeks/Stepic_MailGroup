from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.fresh_questions, name='new_questions'),
    url(r'^question/(?P<pk>\d+)/', views.question, name='question_details'),
    url(r'^popular/', views.popular, name='popular'),
    url(r'^ask/', views.test, name='question_ask'),
    url(r'^answer/', views.test, name='question_answer'),
    url(r'^signup/',views.test, name='signup'),
    url(r'^login/', views.test, name='login'),
    url(r'^logout/', views.test, name='logout'),
    url(r'^new/', views.test, name='new'),
]
