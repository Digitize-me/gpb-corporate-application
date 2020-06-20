from rest_framework import views
from .serializers import (
    EventSerializer,
    TagEventSerializer,
    CategoryEventSerializer,
)
from ..models import Event, TagEvent, CategoryEvent


class EventListCreate(generics.ListCreateAPIView):
    """
    Предложения
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        return serializer.save()


class CategoryEventListCreate(generics.ListCreateAPIView):
    """
    Категории
    """

    queryset = CategoryEvent.objects.all()
    serializer_class = CategoryEventSerializer

    def perform_create(self, serializer):
        return serializer.save()


class CategoryEventRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """
    Категории
    """

    queryset = CategoryEvent.objects.all()
    serializer_class = CategoryEventSerializer


class TagEventListCreate(generics.ListCreateAPIView):
    """
    Теги
    """

    queryset = TagEvent.objects.all()
    serializer_class = TagEventSerializer

    def perform_create(self, serializer):
        return serializer.save()


class TagEventRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """
    Теги
    """

    queryset = TagEvent.objects.all()
    serializer_class = TagEventSerializer
