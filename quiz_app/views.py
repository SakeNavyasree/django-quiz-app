from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question, QuizSession
import random

# Start a new quiz session
def start_quiz(request):
    session = QuizSession.objects.create()
    return render(request, 'quiz_app/start_quiz.html', {'session_id': session.session_id})

# Get a random question for the quiz
def get_question(request, session_id):
    try:
        session = QuizSession.objects.get(session_id=session_id)
    except QuizSession.DoesNotExist:
        return JsonResponse({"error": "Session not found."}, status=404)

    # Get a random question
    question = random.choice(Question.objects.all())
    return render(request, 'quiz_app/question.html', {
        'session_id': session.session_id,
        'question_text': question.question_text,
        'options': {
            "A": question.option_a,
            "B": question.option_b,
            "C": question.option_c,
            "D": question.option_d
        },
        'question_id': question.id
    })

# Submit answer to a question
def submit_answer(request, session_id):
    if request.method == 'POST':
        data = request.POST
        question_id = data.get('question_id')
        answer = data.get('answer')

        try:
            question = Question.objects.get(id=question_id)
            session = QuizSession.objects.get(session_id=session_id)
        except (Question.DoesNotExist, QuizSession.DoesNotExist):
            return JsonResponse({"error": "Invalid question or session."}, status=400)

        # Update the quiz session
        if answer == question.correct_option:
            session.correct_answers += 1
        else:
            session.incorrect_answers += 1
        
        session.total_questions += 1
        session.save()
        
        return redirect('quiz:quiz_results', session_id=session.session_id)


# Display quiz results
def quiz_results(request, session_id):
    try:
        session = QuizSession.objects.get(session_id=session_id)
    except QuizSession.DoesNotExist:
        return JsonResponse({"error": "Session not found."}, status=404)

    return render(request, 'quiz_app/results.html', {
        "total_questions": session.total_questions,
        "correct_answers": session.correct_answers,
        "incorrect_answers": session.incorrect_answers
    })
