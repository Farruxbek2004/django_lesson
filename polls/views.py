from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from polls.forms import QuestionForm, ChoiceForm
from polls.models import Question, Choice


def homepage(request):
    return render(request, 'home.html')


def questions_list(request):
    questions = Question.objects.all()

    context = {
        "questions": questions
    }

    return render(request, 'polls/question.html', context=context)


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    context = {
        "question": question,
    }

    return render(request, 'polls/question_detail.html', context=context)


def question_vote(request, question_id):
    choice = request.POST['choice']
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choices.get(pk=choice)
    except Choice.DoesNotExist:
        raise Http404("Choice doesn't exist.")
    else:
        selected_choice.votes += 1
        selected_choice.save()
        if selected_choice.is_true:
            messages.add_message(request, SUCCESS, 'Your choice is correct.')
            return HttpResponse('Your choice is correct.')
        else:
            messages.add_message(request, ERROR, 'Your choice is incorrect.')
            return HttpResponse('Your choice is incorrect.')
    # return redirect("polls:questions_list")


def choice_new(request):
    form = ChoiceForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("polls:questions_list")
    return render(request, 'choices_new.html', {"form": form})


def question_new(request):
    form = QuestionForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("polls:questions_list")
    return render(request, 'question_new.html', {"form": form})


class BlogDeleteView(DeleteView):
    model = Question
    template_name = 'delete.html'
    success_url = reverse_lazy('polls:homepage')
