from blog.models import Post
from .serializers import PostSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


class ApiPostList(ListAPIView):
    queryset = Post.objects.filter(status=1)
    serializer_class = PostSerializer


class ApiPostDetail(RetrieveAPIView):
    queryset = Post.objects.filter(status=1)
    serializer_class = PostSerializer
