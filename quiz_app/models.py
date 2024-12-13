from django.db import models
import uuid

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255, default="Default Option")
    option_b = models.CharField(max_length=255, default="Default Option")
    option_c = models.CharField(max_length=255, default="Default Option")
    option_d = models.CharField(max_length=255, default="Default Option")
    correct_option = models.CharField(max_length=1)

    def __str__(self):
        return self.question_text

class QuizSession(models.Model):
    session_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)

    def __str__(self):
        return f"Session {self.session_id}"
