from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


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

    path('lesson/list/', LessonListApiView.as_view(),name='trader-lesson-list'),
    path('lesson/create/', LessonCreateApiView.as_view(),name='trader-lesson-create'),
    path('lesson/rud/<int:pk>/', LessonRUDApiView.as_view(),name='trader-lesson-rud'),

    path("unit/create/", UnitCreateView.as_view(),name='unit-create'),
    path("unit/list/", UnitListView.as_view()),
    path("unit/rud/<int:pk>/", UnitRUDView.as_view(),name='unit-rud'),

    path("download/<int:pk>/", DownloadDocumentView.as_view(), name="download-file"),
    path('unit/lessons/<int:unit_id>/', UnitLessonsListView.as_view(), name='unit_lessons'),



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