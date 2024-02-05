from rest_framework import serializers
from .models import *

from rest_framework import serializers
from django.db.models import Max


class TraderCourseSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    class Meta:
        model = Unit
        fields = ['title','image']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            "answer_number",
            "answer_text",
        ]

    def create(self, validated_data):
        question = self.context["view"].kwargs["question"]
        validated_data["is_correct"] = validated_data.get("is_correct", False)
        return Answer.objects.create(question=question, **validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    options = AnswerSerializer(many=True)
    correct_answer = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Question
        fields = "__all__"

    # вывод correct answer
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["correct_answer"] = instance.correct_answer
        return representation

    def create(self, validated_data):
        options_data = validated_data.pop("options")
        correct_answer = validated_data.pop("correct_answer", None)

        # Создаем вопрос
        question = Question.objects.create(**validated_data)

        # Создаем ответы для вопроса
        for i, option_data in enumerate(options_data, start=1):
            is_correct = i == correct_answer
            Answer.objects.create(
                question=question, is_correct=is_correct, answer_number=i, **option_data
            )

        # Устанавливаем правильный ответ
        if correct_answer:
            question.correct_answer = correct_answer
            question.save()

        return question


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class StrategyCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategyCourse
        fields = "__all__"


class StrategyLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategyLesson
        fields = "__all__"
