from django import forms

from polls.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'pub_date']


# class QuestionDeleteView(forms.ModelForm):
#     class Meta:
#         model = Question
#         template_name = 'delete.html'
#         success_url = reverse_lazy('home')
