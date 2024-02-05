from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"unit", UnitViewSet, basename="course_crud")
router.register(r"lesson", LessonViewSet, basename="lesson_crud")
router.register(
    r"strategy/course", StrategyCourseViewSet, basename="6 sessistrategy crush course"
)
router.register(
    r"strategy/lesson",
    StrategyLessonViewSet,
    basename="6 sessistrategy crush course lesson",
)


urlpatterns = [
    path("", include(router.urls)),
    path("lesson/<int:unit_id>/", LessonAPIView.as_view()),
    path("unit/<int:unit_id>/", UnitDetailView.as_view()),
    path("unit/list/<int:unit_id>/", UnitListView.as_view()),

    path("download/<int:pk>/", DownloadDocumentView.as_view(), name="download-file"),



    path(
        "questions/create/lesson/",
        QuestionListCreateView.as_view(),
        name="question-admin-list-create-lesson",
    ),
    path(
        "questions/rud/lesson/<int:pk>/",
        QuestionRUDView.as_view(),
        name="question-admin-rud-lesson",
    ),
    path(
        "questions/list/lesson/",
        QuestionListView.as_view(),
        name="question-user-list-lesson",
    ),
    path(
        "questions/detail/lesson/<int:pk>/",
        QuestionDetailView.as_view(),
        name="question-user-detail-lesson",
    ),
]
