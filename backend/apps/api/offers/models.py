from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.api.reference.models import Tag, Category


# Категория проекта/мероприятия (Продукты и услуги, Развитие технологий, Обслуживание в офисах продаж) выбор из таблицы одного
# Тема (название)
# Идея проекта/мероприятия (2-3 предложения, которые будут отображаться на главной карточке) краткое описание
# Хештеги проекта/мероприятия которое будет формироваться из выбора выпадающих вариков (Пример: темаКвиз- вид отдыхаотдых пассивный- вид игринтеллектуальные игры- колво участников20+ человек) таблица много
# Более подробная инфа о проекте/мероприятии (5-10 предложений, отображаются по свайпу вниз) подробная информация
# Примерная стоимость проекта/мероприятия затраты или нет затрат
# Добавить фотку проекта/мероприятия


class Offer(models.Model):
    """
    Модель предложений или идей сотрудников
    """

    is_published = models.BooleanField(
        default=False, verbose_name=_("Публикация")
    )
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
        Category,
        verbose_name=_("Категория"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(Tag, verbose_name=_("Теги"),)
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
