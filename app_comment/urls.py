from django.urls import path
from .views import *

urlpatterns = [
    path(
        "post_lists/<int:post_list_id>/comments/",
        CommentListCreateView.as_view(),
        name="comment-list-create",
    ),
    path("post_lists/rud/comments/<int:pk>/",CommentRUDView.as_view(),name="comment-rud",),
    path("post_lists/detail/<int:pk>/",CommentDetailView.as_view(),name="comment-detail",),

]
