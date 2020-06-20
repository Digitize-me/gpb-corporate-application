from rest_framework import generics
from .serializers import (
    OfferSerializer,
    TagOfferSerializer,
    CategoryOfferSerializer,
)
from ..models import Offer, TagOffer, CategoryOffer


class OfferListCreate(generics.ListCreateAPIView):
    """
    Предложения
    """

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def perform_create(self, serializer):
        return serializer.save()


# class OfferRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     """
#     Предложения
#     """

#     queryset = Offer.objects.all()
#     serializer_class = OfferSerializer


class CategoryOfferListCreate(generics.ListCreateAPIView):
    """
    Категории
    """

    queryset = CategoryOffer.objects.all()
    serializer_class = CategoryOfferSerializer

    def perform_create(self, serializer):
        return serializer.save()


class CategoryOfferRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """
    Категории
    """

    queryset = CategoryOffer.objects.all()
    serializer_class = CategoryOfferSerializer


class TagOfferListCreate(generics.ListCreateAPIView):
    """
    Теги
    """

    queryset = TagOffer.objects.all()
    serializer_class = TagOfferSerializer

    def perform_create(self, serializer):
        return serializer.save()


class TagOfferRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """
    Теги
    """

    queryset = TagOffer.objects.all()
    serializer_class = TagOfferSerializer
