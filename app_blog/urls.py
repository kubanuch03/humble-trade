from django.urls import path
from .views import *


app_name = "blog"
urlpatterns = [
    #posts
    path("posts/list/", PostListView.as_view(), name="post-list"),
    path("posts/detail/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("posts/rud/<int:pk>/",PostRetrieveUpdateDestroyView.as_view(),name="post-rud",),

    #post list
    path("post_lst/list/", PostListListView.as_view(), name="post-lst-list"),
    path("post_lst/detail/<int:pk>/",PostListDetailView.as_view(),name="post-lst-detail",),
    path("post_lst/create/", PostListCreateView.as_view(), name="post-lst-create"),
    path("post_lst/rud/<int:pk>/", PostListRetrieveUpdateDestroyView.as_view(), name="post-lst-rud"),

    #module
    path("modules/list/", ModuleListView.as_view(), name="module-lst"),
    path("modules/detail/<int:pk>/",ModuleDetailView.as_view(),name="module-detail",),
    path("modules/create/", ModuleCreateView.as_view(), name="module-create"),
    path("modules/rud/<int:pk>/",ModuleRetrieveUpdateDestroyView.as_view(),name="module-rud",),

    #hashtag
    path("hashtags/list/", HashtagListView.as_view(), name="hashtag-list"),
    path("hashtags/detail/<int:pk>/", HashtagDetailView.as_view(), name="hashtag-detail"),
    path("hashtags/create/", HashtagListCreateView.as_view(), name="hashtag-create"),
    path("hashtags/rud/<int:pk>/",HashtagRetrieveUpdateDestroyView.as_view(),name="hashtag-rud",),
]