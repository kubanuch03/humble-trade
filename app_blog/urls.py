from django.urls import path
from .views import *


app_name = "blog"
urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path(
        "posts/<int:pk>/",
        PostRetrieveUpdateDestroyView.as_view(),
        name="post-retrieve-update-destroy",
    ),
    path("post_lst/", PostListListCreateView.as_view(), name="post-lst-list-create"),
    path(
        "post_lst/<int:pk>/",
        PostListRetrieveUpdateDestroyView.as_view(),
        name="post-lst-retrieve-update-destroy",
    ),
    path("modules/", ModuleListCreateView.as_view(), name="module-lst-create"),
    path(
        "modules/<int:pk>/",
        ModuleRetrieveUpdateDestroyView.as_view(),
        name="module-retrieve-update-destroy",
    ),
    path("hashtags/", HashtagListCreateView.as_view(), name="hashtag-list-create"),
    path(
        "hashtags/<int:pk>/",
        HashtagRetrieveUpdateDestroyView.as_view(),
        name="hashtag-rud",
    ),
]
