from rest_framework import viewsets
from rest_framework.response import Response

from blog.models import Category,Post
from blog.serializers import CategorySerializer,PostSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()    

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()