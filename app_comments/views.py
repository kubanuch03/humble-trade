from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django.shortcuts import render
from .models import CommentCourse, CommentDocument
from .serializers import CommentCourseSerializer, CommentDocumentSerializer
from rest_framework import generics
from drf_spectacular.utils import extend_schema
import logging
from app_clients.models import Client

logger = logging.getLogger(__name__)



#======== Course Comment ===================================================
class CommentsListCreateView(generics.ListCreateAPIView):
    queryset = CommentCourse.objects.all()
    serializer_class = CommentCourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    


class CommentsRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentCourse.objects.all()
    serializer_class = CommentCourseSerializer
    permission_classes = [permissions.IsAdminUser]
    





#======== Course Comment ===================================================


class CommentsDocumentViewSet(ModelViewSet):
    queryset = CommentDocument.objects.all()
    serializer_class = CommentDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]





class CommentsDocumentAPIView(generics.ListAPIView):
    serializer_class = CommentDocumentSerializer
    swagger_fake_view = True

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        try:
            document_id = self.kwargs["document_id"]
            return CommentDocument.objects.filter(post_id=document_id)
        except CommentDocument.DoesNotExist:
            return CommentDocument.objects.none()
        except Exception as e:
            logger.error(f"Error in CommentsDocumentAPIView: {e}")
            return CommentDocument.objects.none()

    queryset = CommentDocument.objects.none()


class CommentsCourseAPIView(generics.ListAPIView):
    serializer_class = CommentCourseSerializer
    swagger_fake_view = True
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        try:
            course_id = self.kwargs["course_id"]
            return CommentCourse.objects.filter(post_id=course_id)
        except CommentCourse.DoesNotExist:
            return CommentCourse.objects.none()
        except Exception as e:
            logger.error(f"Error in CommentsCourseAPIView: {e}")
            return CommentCourse.objects.none()

    queryset = CommentCourse.objects.none()
