from rest_framework import serializers
from ..models import Offer, TagOffer, CategoryOffer


class CategoryOfferSerializer(serializers.ModelSerializer):
    """
    Сериализатор категорий
    """

    class Meta:
        model = CategoryOffer
        fields = "__all__"


class TagOfferSerializer(serializers.ModelSerializer):
    """
    Сериализатор тегов
    """

    class Meta:
        model = TagOffer
        fields = "__all__"


class OfferSerializer(serializers.ModelSerializer):
    """
    Сериализатор предложений
    """

    tags = TagOfferSerializer(required=False)

    class Meta:
        model = Offer
        fields = ["tags"]
