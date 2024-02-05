from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework import generics
from .models import *
from .pagination import CustomPageNumberPagination, SingleItemPagination
from .serializers import (
    CategorySerializer,
    VideoCourseSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response
import logging


logger = logging.getLogger(__name__)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPageNumberPagination
    lookup_field = "pk"

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        courses = Courses.objects.filter(category=instance)
        category_data = CategorySerializer(instance).data 
        course_data = VideoCourseSerializer(courses, many=True).data

        response_data = {
            "category": {
                "id": instance.id, 
                "title": category_data['title'],
                "image": category_data['image'],
                "description": category_data['description']
            },
            "course": course_data
        }

        return Response(response_data)





"================================================================================="


class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Courses.objects.all().order_by("created_at")
    serializer_class = VideoCourseSerializer
    pagination_class = SingleItemPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    @action(
        methods=['get'],
        detail=True,
        serializer_class=VideoCourseSerializer,
        permission_classes=[permissions.IsAuthenticated],
    )
    def one_page(self, request, *args, **kwargs):
        self.pagination_class.page_size = 1
        return self.list(request, *args, **kwargs)


class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all().order_by("created_at")
    serializer_class = VideoCourseSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser, ]


class CourseListView(generics.ListAPIView):
    queryset = Courses.objects.all().order_by("created_at")
    serializer_class = VideoCourseSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [permissions.IsAuthenticated, ]