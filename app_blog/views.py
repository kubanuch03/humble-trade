from rest_framework import generics
from .models import Post, Post_list, Module, Hashtag
from .serializers import (
    PostSerializer,
    PostListSerializer,
    ModuleSerializer,
    HashtagSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from .paginations import CustomPostPagination

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import status

from drf_spectacular.utils import extend_schema

from transliterate import slugify




#======  Post   ===============================================
#User
class PostListView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]



    @extend_schema(
        summary="List a  blog post list",
        description="List a  blog post list",
        request=PostSerializer,
        responses={200: PostSerializer},
        operation_id="blog_post_list_v1",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


#Admin
class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser]

    # @extend_schema(
    #     summary="Create a new blog post list",
    #     description="Create a new blog post list",
    #     request=PostSerializer,
    #     responses={201: PostSerializer},
    #     operation_id="blog_post_create_v1",
    # )
    # def create(self, request, *args, **kwargs):
    #     title = request.data.get('title',).strip()
    #     print(title)
    #     if not title:
    #         return JsonResponse({'error': 'Title не может быть пустым'}, status=status.HTTP_400_BAD_REQUEST)

    #     slug = slugify(title)
    #     if Post.objects.filter(slug=slug).exists():
    #         return JsonResponse({'error': 'Post с таким заголовком уже существует. Пожалуйста, выберите другой заголовок.'}, status=status.HTTP_400_BAD_REQUEST)

    #     request.data['slug'] = slug
    #     return super().create(request, *args, **kwargs)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser]

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

#=== Post List ================================================================
#User
class PostListListView(generics.ListAPIView):
    filter_backends = [SearchFilter]
    queryset = Post_list.objects.all()
    search_fields = ["hashtags__name"]
    serializer_class = PostListSerializer
    pagination_class = CustomPostPagination
    permission_classes = [permissions.IsAuthenticated,]

    
    def get_queryset(self):
        user = self.request.user  # Получаем текущего пользователя
        return Post_list.objects.filter(user=user)
        
    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        query = self.request.query_params.get("search", None)
        if query:
            # Добавляем фильтрацию по названию хэштега
            queryset = queryset.filter(hashtags__name__icontains=query)
        return queryset
    

class PostListDetailView(generics.RetrieveAPIView):
    queryset = Post_list.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAuthenticated]


    
#Admin
class PostListCreateView(generics.CreateAPIView):
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAdminUser]


    @extend_schema(
        summary=" admin Post_lst Create a new blog post lst",
        description="admin Post_lst Create a new blog post lst",
        request=PostListSerializer,
        responses={201: PostListSerializer},
        operation_id="admin_create_blog_post_lst_v1",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_list.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAdminUser]

   




# ===== Module ================================================================
#User
    
class ModuleListView(generics.ListAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    filter_backends = [SearchFilter]
    permission_classes = [permissions.IsAuthenticated]


class ModuleDetailView(generics.RetrieveAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]


#Admin
class ModuleCreateView(generics.CreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAdminUser]

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
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        summary="RUD a new blog module",
        description="RUD a new blog module",
        request=ModuleSerializer,
        responses={201: ModuleSerializer},
        operation_id="blog_module_post_v1",
    )
    def post(self, request):
        return Response("Success")



# ==== Hashtag ===============================================================
#User
class HashtagListView(generics.ListCreateAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]
    permission_classes = [permissions.IsAuthenticated]


class HashtagDetailView(generics.RetrieveAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    permission_classes = [permissions.IsAuthenticated]



#Admin
class HashtagListCreateView(generics.ListCreateAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]
    permission_classes = [permissions.IsAdminUser]

class HashtagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    permission_classes = [permissions.IsAdminUser]

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