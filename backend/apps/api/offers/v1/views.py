from rest_framework import generics
from .serializers import OfferSerializer, TagSerializer, CategorySerializer
from ..models import Offer, Tag, Category


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
