# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
import random

def display_question(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_option_id = request.POST.get('option_id')
        question = get_object_or_404(Question, question_id=question_id)
        correct_option_id = question.answer

        is_correct = selected_option_id == correct_option_id

        if is_correct:
            return redirect('sem6:answer', question_id=question_id)
        else:
            context = {
                'question': question,
                'correct_option_id': correct_option_id,
                'is_correct': is_correct,
            }
            return render(request, 'sem6/answer.html', context)
    else:
        random_question = random.choice(Question.objects.all())
        context = {
            'question': random_question,
        }
        return render(request, 'sem6/question.html', context)

def display_answer(request, question_id):
    question = get_object_or_404(Question, question_id=question_id)
    return render(request, 'sem6/answer.html', {'question': question})