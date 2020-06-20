from rest_framework import serializers
from ..models import (
    Offer,
    Tag,
    Category,
)


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор категорий
    """

    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    """
    Сериализатор тегов
    """

    class Meta:
        model = Tag
        fields = "__all__"


class OfferSerializer(serializers.ModelSerializer):
    """
    Сериализатор предложений
    """

    class Meta:
        model = Offer
        fields = "__all__"
