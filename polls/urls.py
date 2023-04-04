from django.urls import path

from polls.views import (
    homepage,
    questions_list,
    question_detail,
    question_vote,
    choice_new,
    question_new,
    BlogDeleteView
)

app_name = 'polls'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('questions/', questions_list, name='questions_list'),
    path('questions/<int:question_id>/', question_detail, name='question_detail'),
    path('questions/<int:question_id>/vote/', question_vote, name='question_vote'),
    path('questions/new/', choice_new, name='choice_new'),
    path('questions/add/', question_new, name='question_new'),
    path('questions/<int:question_id>/delete/', BlogDeleteView.as_view(), name='question_delete'),

]
