from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import permissions, generics
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from django.views import View
from .models import Lesson
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Unit, Lesson, StrategyCourse, StrategyLesson, Question, Answer
from .seriallizer import (
    TraderCourseSerializer,
    LessonSerializer,
    StrategyCourseSerializer,
    StrategyLessonSerializer,
    QuestionSerializer,
)
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.views import View
import logging

logger = logging.getLogger(__name__)

from drf_spectacular.utils import extend_schema


# =================QUIZ==================================================
# User
class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Question List",
        description="Question List",
        request=QuestionSerializer,
        responses={200: QuestionSerializer},
        operation_id="question_user_list",
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Question Detail",
        description="Question Detail",
        request=QuestionSerializer,
        responses={200: QuestionSerializer},
        operation_id="question_detail",
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# Admin
class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]




class QuestionRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        summary="Question Admin Update",
        description="Question Admin Update",
        request=QuestionSerializer,
        responses={200: QuestionSerializer},
        operation_id="question_admin_rud_put",
    )
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @extend_schema(
        summary="Question Admin Delete",
        description="Question Admin Delete",
        request=QuestionSerializer,
        responses={200: QuestionSerializer},
        operation_id="question_admin_rud_delete",
    )
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @extend_schema(
        summary="Question Admin Detail",
        description="Question Admin Detail",
        request=QuestionSerializer,
        responses={200: QuestionSerializer},
        operation_id="question_admin_rud_detail",
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# ===================================================================


class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = TraderCourseSerializer
    permission_classes = [
        IsAdminUser,
    ]


class UnitListView(RetrieveAPIView):
    queryset = Unit.objects.all()
    serializer_class = TraderCourseSerializer
    permission_classes = [
        IsAuthenticated,
    ]


class UnitDetailView(ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = TraderCourseSerializer
    permission_classes = [
        IsAuthenticated,
    ]


class UnitLessonsView(View):
    def get(self, request, unit_id, *args, **kwargs):
        try:
            lessons = Lesson.objects.filter(unit_id=unit_id)
            lesson_data = []
            for lesson in lessons:
                lesson_data.append({
                    'title': lesson.title,
                    'image_url': lesson.image.url,
                    'instructor_username': lesson.instructor.username if lesson.instructor else None,
                    'url': lesson.url,
                })
            return JsonResponse({'lessons': lesson_data})
        except Unit.DoesNotExist:
            return JsonResponse({'error': 'Unit does not exist'}, status=404)

"============Unit=========================================="


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [
        IsAdminUser,
    ]


class LessonAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    swagger_fake_view = True

    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        try:
            unit_id = self.kwargs["unit_id"]
            return Lesson.objects.filter(unit_id=unit_id)
        except Lesson.DoesNotExist:
            return Lesson.objects.none()
        except Exception as e:
            logger.error(f"Error in LessonAPIView : {e}")
            return Lesson.objects.none()

    queryset = Lesson.objects.none()


"=============Lesson========================================="


class StrategyLessonViewSet(ModelViewSet):
    queryset = StrategyLesson.objects.all()
    serializer_class = StrategyLessonSerializer


class StrategyLessonListView(ListAPIView):
    queryset = StrategyLesson.objects.all()
    serializer_class = StrategyLessonSerializer
    permission_classes = [
        IsAuthenticated,
    ]


"================StrategyLesson==================================="


class StrategyCourseViewSet(ModelViewSet):
    queryset = StrategyCourse.objects.all()
    serializer_class = StrategyCourseSerializer


class StrategyCourseListView(ListAPIView):
    queryset = StrategyCourse.objects.all()
    serializer_class = StrategyCourseSerializer
    permission_classes = [
        IsAuthenticated,
    ]


"================StrategyCourse==================================="


class DownloadDocumentView(View):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        document = get_object_or_404(StrategyLesson, pk=pk)
        if not document.lesson:
            raise Http404("Файл не найден")
        response = FileResponse(document.lesson, as_attachment=True)
        response["Content-Disposition"] = f"attachment; filename={document.lesson.name}"
        return response
