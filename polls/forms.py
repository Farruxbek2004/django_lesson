from django import forms
from django.urls import reverse_lazy

from polls.models import Question

class QuestionFrom(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'pub_date']

class QuestionDeleteView(forms.ModelForm):
    class Meta:
        model = Question
        template_name = 'post_delete.html'
        success_url = reverse_lazy('home')