from django import forms
from polls.models import Question, Choice


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'text', 'votes', 'is_true']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'pub_date']

