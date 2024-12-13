from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('quiz/start/', views.start_quiz, name='start_quiz'),
    path('quiz/<str:session_id>/question/', views.get_question, name='get_question'),
    path('quiz/<str:session_id>/submit/', views.submit_answer, name='submit_answer'),
    path('quiz/<str:session_id>/results/', views.quiz_results, name='quiz_results'),
]
