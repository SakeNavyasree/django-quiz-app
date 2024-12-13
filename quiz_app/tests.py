from django.test import TestCase
from django.urls import reverse
from .models import Question, QuizSession

class QuizAppViewTestCase(TestCase):
    def setUp(self):
        self.question = Question.objects.create(
            question_text="What is the capital of France?",
            option_a="Paris",
            option_b="London",
            option_c="Rome",
            option_d="Berlin",
            correct_option="A"
        )

    def test_start_quiz(self):
        """Test the start_quiz view."""
        response = self.client.get(reverse('quiz:start_quiz'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Start Quiz')

    def test_get_question(self):
        """Test the get_question view."""
        session = QuizSession.objects.create()
        response = self.client.get(reverse('quiz:get_question', args=[session.session_id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'What is the capital of France?')

    def test_submit_answer(self):
        """Test the submit_answer view."""
        session = QuizSession.objects.create()
        question_id = self.question.id
        response = self.client.post(reverse('quiz:submit_answer', args=[session.session_id]), {
            'question_id': question_id,
            'answer': 'A'
        })
        self.assertEqual(response.status_code, 302)  

    def test_quiz_results(self):
        """Test the quiz_results view."""
        session = QuizSession.objects.create()
        session.total_questions = 1
        session.correct_answers = 1
        session.incorrect_answers = 0
        session.save()

        response = self.client.get(reverse('quiz:quiz_results', args=[session.session_id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Total Questions: 1')
        self.assertContains(response, 'Correct Answers: 1')
