from rest_framework import serializers
from .models import *

from rest_framework import serializers
from django.db.models import Max

from drf_spectacular.utils import extend_schema_field


class TraderCourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=True)
    class Meta:
        model = Unit
        fields = ['id','title','image']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            "id",
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
        fields = ['id','unit','title','user','image','url',]

    @extend_schema_field(str)
    def get_post_title(self, obj):
        return obj.post.title if obj.post else None
    
    def create(self, validated_data):
        print("Validated data:", validated_data)
        user_data = validated_data.pop("user", None)

        lesson  = Lesson.objects.create(**validated_data)
        print("Created lesson:", lesson)

        if user_data:
            lesson .user.set(user_data)

        return lesson

        

    def update(self, instance, validated_data):
        users_data = validated_data.pop("user", None)


        if users_data:
            instance.user.set(users_data)

   

     
  

        instance.save()
        return instance


class StrategyCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategyCourse
        fields = ['id','title','image']


class StrategyLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategyLesson
        fields =  ['id','title','course','instructor','image']