from django.db import models
from app_clients.models import Client
from django.contrib.postgres.fields import JSONField


class Unit(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='trader_academy/unit/',)

    def __str__(self) -> str:
        return f"{self.title}"


class Lesson(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    user = models.ManyToManyField(Client)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="trader_academy/lesson/")
    url = models.URLField()
    
    question = models.ForeignKey(
       "Question", on_delete=models.CASCADE, related_name="questions",null=True,blank=True
    )

    def __str__(self) -> str:
        return f"{self.id}"


class StrategyCourse(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()

    def __str__(self) -> str:
        return f"{self.id}"


class StrategyLesson(models.Model):
    course = models.ForeignKey(StrategyCourse, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="strategy_lesson/lesson/")
    instructor = models.ForeignKey(Client, on_delete=models.PROTECT, blank=True,null=True)

    def __str__(self) -> str:
        return f"{self.title}"


class Question(models.Model):
    question = models.CharField(max_length=255, null=True, blank=True)
    correct_answer = models.IntegerField(default="1", null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')

    def __str__(self) -> str:
        return f"{self.question}"


class Answer(models.Model):
    question = models.ForeignKey(
       Question, on_delete=models.CASCADE, related_name="options",blank=True,null=True
    )
    answer_text = models.CharField(max_length=255, null=True, blank=True)
    answer_number = models.PositiveIntegerField(default=1, null=True, blank=True)
    is_correct = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.answer_text}"