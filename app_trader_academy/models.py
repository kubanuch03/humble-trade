from django.db import models
from app_clients.models import Client
from django.contrib.postgres.fields import JSONField


class Unit(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='trader_academy/unit/',blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title}"


class Lesson(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="trader_academy/lesson/")
    instructor = models.ForeignKey(Client, on_delete=models.PROTECT,blank=True,null=True)
    url = models.URLField()
    question = models.ForeignKey(
        "Question", on_delete=models.CASCADE, related_name="questions"
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
    instructor = models.ForeignKey(Client, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.title}"


class Question(models.Model):
    question = models.CharField(max_length=255)
    correct_answer = models.IntegerField(default="1")
    # lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')

    def __str__(self) -> str:
        return f"{self.question}"


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="options"
    )
    answer_text = models.CharField(max_length=255)
    answer_number = models.PositiveIntegerField(default=1)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.answer_text}"
