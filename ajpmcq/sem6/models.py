from django.db import models

class Question(models.Model):
    question_id = models.CharField(max_length=20, unique=True)
    question_text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.question_id}: {self.question_text}"


