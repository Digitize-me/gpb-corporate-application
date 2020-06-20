from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.api.reference.models import TagAbstract, CategoryAbstract


class TagEvent(TagAbstract):
    """
    Модель тегов
    """

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег (мероприятий)"
        verbose_name_plural = "Теги (мероприятий)"


class CategoryEvent(CategoryAbstract):
    """
    Модель категорий
    """

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория (мероприятий)"
        verbose_name_plural = "Категории (мероприятий)"


class Event(models.Model):
    """
    Модель мероприятий
    """

    date_created = models.DateField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    creator = models.ForeignKey(
        get_user_model(),
        verbose_name=_("Создатель"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    idea_short = models.CharField(
        max_length=255, verbose_name=_("Краткое мероприятия")
    )
    idea = models.TextField(verbose_name=_("Подробное описание"))
    date_of_the_event = models.DateField(verbose_name=_("Дата проведения"))
    category = models.ForeignKey(
        CategoryEvent,
        verbose_name=_("Категория"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="category",
    )
    tags = models.ManyToManyField(
        TagEvent, null=True, blank=True, verbose_name=_("Теги"),
    )
    img = models.ImageField(
        blank=True, null=True, verbose_name=_("Изображение")
    )

    def __str__(self):
        return self.idea_short

    class Meta:
        verbose_name = _("Мероприятие")
        verbose_name_plural = _("Мероприятия")
