from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=500)
    is_active = models.BooleanField()

    def __str__(self):
        return self.question


class Answer(models.Model):
    fk_question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name='Question')
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.answer
