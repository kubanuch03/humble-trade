from rest_framework import generics
from .models import Post, Post_list, Module, Hashtag
from .serializers import (
    PostSerializer,
    PostListSerializer,
    ModuleSerializer,
    HashtagSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import CustomPostPagination
from .permissions import IsModeratorOrReadOnly

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import NotFound
from rest_framework import status

from drf_spectacular.utils import extend_schema

from transliterate import slugify


class PostListCreateView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsModeratorOrReadOnly, permissions.IsAuthenticated]



    @extend_schema(
        summary="List a  blog post list",
        description="List a  blog post list",
        request=PostSerializer,
        responses={200: PostSerializer},
        operation_id="blog_post_list_v1",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new blog post list",
        description="Create a new blog post list",
        request=PostSerializer,
        responses={201: PostSerializer},
        operation_id="blog_post_create_v1",
    )
    def create(self, request, *args, **kwargs):
        title = request.data.get('title', '')
        slug = slugify(title)

        if Post.objects.filter(slug=slug).exists():
            return Response({'error': 'Title с таким заголовком уже существует Выберите другое название'}, status=status.HTTP_400_BAD_REQUEST)

        request.data['slug'] = slug
        return super().create(request, *args, **kwargs)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsModeratorOrReadOnly]

    @extend_schema(
        summary="Retrieve, update, or delete a post",
        description="Retrieve, update, or delete a post",
        request=PostSerializer,
        responses={200: PostSerializer},
        operation_id="blog_post_rud_v1",
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT) #


class PostListListCreateView(generics.ListCreateAPIView):
    filter_backends = [SearchFilter]
    queryset = Post_list.objects.all()
    search_fields = ["hashtags__name"]
    serializer_class = PostListSerializer
    pagination_class = CustomPostPagination

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        query = self.request.query_params.get("search", None)
        if query:
            # Добавляем фильтрацию по названию хэштега
            queryset = queryset.filter(hashtags__name__icontains=query)
        return queryset

    @extend_schema(
        summary="Post_List List  a blog post list",
        description="Post_List List a  blog post list",
        request=PostListSerializer,
        responses={200: PostListSerializer},
        operation_id="list_blog_post_lst_v1",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary=" Post_lst Create a new blog post lst",
        description="Post_lst Create a new blog post lst",
        request=PostListSerializer,
        responses={201: PostListSerializer},
        operation_id="create_blog_post_lst_v1",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_list.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsModeratorOrReadOnly]

    @extend_schema(
        summary=" Post_lst RUD a  blog post lst",
        description="Post_lst RUD a  blog post lst",
        request=PostListSerializer,
        responses={200: PostListSerializer},
        operation_id="rud_blog_post_lst_v1",
    )
    def post(self, request):
        return Response("Success")


class ModuleListCreateView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsModeratorOrReadOnly, permissions.IsAuthenticated]

    @extend_schema(
        summary="List a  blog module",
        description="List a  blog module",
        request=ModuleSerializer,
        responses={200: ModuleSerializer},
        operation_id="blog_module_list_v1",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new blog module",
        description="Create a new blog module",
        request=ModuleSerializer,
        responses={201: ModuleSerializer},
        operation_id="blog_module_create_v1",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ModuleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsModeratorOrReadOnly]

    @extend_schema(
        summary="RUD a new blog module",
        description="RUD a new blog module",
        request=ModuleSerializer,
        responses={201: ModuleSerializer},
        operation_id="blog_module_post_v1",
    )
    def post(self, request):
        return Response("Success")


class HashtagListCreateView(generics.ListCreateAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]


class HashtagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer

    @extend_schema(
        summary="put Hashtag",
        description="put Hashtag",
        request=HashtagSerializer,
        responses={200: HashtagSerializer},
        operation_id="blog_hashtag_admin_put_v1",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        summary="patch Hashtag",
        description="patch Hashtag",
        request=HashtagSerializer,
        responses={200: HashtagSerializer},
        operation_id="blog_hashtag_admin_patch_v1",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="delete Hashtag",
        description="delete Hashtag",
        request=HashtagSerializer,
        responses={200: HashtagSerializer},
        operation_id="blog_hashtag_admin_delete_v1",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)