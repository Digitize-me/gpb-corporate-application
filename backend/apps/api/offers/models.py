from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.api.reference.models import TagAbstract, CategoryAbstract


class CategoryOffer(CategoryAbstract):
    """
    Модель категорий
    """

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория (предложений)"
        verbose_name_plural = "Категории (предложений)"


class Offer(models.Model):
    """
    Модель предложений или идей сотрудников
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
    category = models.ForeignKey(
        CategoryOffer,
        related_name="category",
        verbose_name=_("Категория"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    idea_short = models.CharField(
        max_length=255, verbose_name=_("Краткое описание (идея проекта)")
    )
    idea = models.TextField(verbose_name=_("Подробное описание"))
    img = models.ImageField(
        blank=True, null=True, verbose_name=_("Изображение")
    )

    def __str__(self):
        return self.idea_short

    class Meta:
        verbose_name = _("Прдложение")
        verbose_name_plural = _("Прдложения")


class TagOffer(TagAbstract):
    """
    Модель тегов
    """

    tags = models.ManyToManyField(
        Offer,
        null=True,
        blank=True,
        verbose_name=_("Теги"),
        related_name="offers",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег (предложений)"
        verbose_name_plural = "Теги (предложений)"
