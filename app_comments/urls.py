from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
# router.register(
#     r"video/library/course",
#     CommentsCourseViewSet,
#     basename="comments-video-library-course",
# )
router.register(
    r"resourse/center/document",
    CommentsDocumentViewSet,
    basename="comments-resourse-center-documents",
)

urlpatterns = [
    path("", include(router.urls)),
    path("video/library/create/list/comment/",CommentsListCreateView.as_view()),
    path("video/library/rud/comment/<int:pk>/",CommentsRUDView.as_view()),


    path("document/comments/<int:document_id>/",CommentsDocumentAPIView.as_view(),name="comment_defined_documents",),
    
    path("course/comments/<int:course_id>/",CommentsCourseAPIView.as_view(),name="comment_defined_course",),
]
