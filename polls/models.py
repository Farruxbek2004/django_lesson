from django.db import models
from django.urls import reverse


class Question(models.Model):
    text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('data published', null=True)

    def __str__(self):
        return self.text

    # def get_absolute_url(self):
    #     return reverse('polls:question_detail', args=[str(self.id)])
    #

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text} - {self.is_true}'
