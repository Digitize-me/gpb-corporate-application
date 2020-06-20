from rest_framework import serializers
from ..models import Event, TagEvent, CategoryEvent


class CategoryEventSerializer(serializers.ModelSerializer):
    """
    Сериализатор категорий
    """

    class Meta:
        model = CategoryEvent
        fields = "__all__"


class TagEventSerializer(serializers.ModelSerializer):
    """
    Сериализатор тегов
    """

    class Meta:
        model = TagEvent
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    """
    Сериализатор предложений
    """

    tags = TagEventSerializer(many=True)
    category = CategoryEventSerializer(many=True)

    class Meta:
        model = Event
        fields = "__all__"
