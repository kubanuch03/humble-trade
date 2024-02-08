from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser



#User

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_list_id = self.kwargs["post_list_id"]
        return Comment.objects.filter(post_list__id=post_list_id)

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated and hasattr(user, 'client'):
            serializer.save(user=user.client)
        else:
            raise ValueError("Invalid user or missing associated Client.")


class CommentDetailView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]




#Admin
class CommentRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]
