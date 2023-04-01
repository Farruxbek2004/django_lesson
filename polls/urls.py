from django.urls import path
from polls.views import homepage, questions_list, question_detail


urlpatterns = [
    path('', homepage, name='homepage'),
    path('questions/', questions_list, name='questions_list'),
    path('questions/<int:question_id>/', question_detail, name='question_detail')
]