from django.db import models

# Create your models here.


class TagAbstract(models.Model):
    """
    Модель тегов
    """

    name = models.CharField(max_length=50, verbose_name=("Название тега"))

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class CategoryAbstract(models.Model):
    """
    Модель категорий
    """

    name = models.CharField(max_length=50, verbose_name=("Название категории"))

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        verbose_name = "Категория предложения"
        verbose_name_plural = "Категории предложений"
