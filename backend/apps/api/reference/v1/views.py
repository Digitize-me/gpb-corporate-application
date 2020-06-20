from rest_framework import views, generics
from .serializers import TagSerializer, CategorySerializer
from ..models import (
    Tag,
    Category,
)


class CategoryListCreate(generics.ListCreateAPIView):
    """
    Категории
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        return serializer.save()


class CategoryRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """
    Категории
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListCreate(generics.ListCreateAPIView):
    """
    Теги
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def perform_create(self, serializer):
        return serializer.save()


class TagRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """
    Теги
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
