from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR
from polls.forms import QuestionFrom
from polls.models import Question, Choice


def homepage(request):
    # return HttpResponse('<h1>Hello Django from <span style= "color:red">P10</span></h1>')
    return render(request, 'home.html')


def question_list(request):
    # questions = Question.objects.filter(text__contains='O')
    # response = ''
    # for index, question in enumerate(questions):
    #     response += f'{index + 1}. {question.text}<br>'
    # return HttpResponse(f'Question list here.<br>{response}')
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'polls/question.html', context=context)


def question_detail(request, question_id):
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404
    # else:
    #     return HttpResponse(f'Question text: {question.text}<br> pub_date: {question.pub_date}')
    # question = get_object_or_404(Question, id=question_id)
    # return HttpResponse(f'Question text: {question.text}<br> pub_date: {question.pub_date}')
    questions = get_object_or_404(Question, id=question_id)
    choices = Choice.objects.filter(question=questions)
    context = {
        'questions': questions,
        'choices': choices
    }
    return render(request, 'polls/question_detail.html', context=context)


def question_vote(request, question_id):
    if 'choice' in request.POST:
        choice = request.POST['choice']
    else:
        choice = False
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
            return HttpResponse('Your choice is correct')
        else:
            messages.add_message(request, ERROR, 'Your choice in incorrent.')
            return HttpResponse('Your choice in incorrent.')


def question_add(request):
    form = QuestionFrom(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('polls:questions_list')
    return render(request, 'polls/add_question.html', {'form': form})
