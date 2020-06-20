from django.db import models
from django.contrib.auth import get_user_model
from apps.api.offers.models import Offer
from django.utils.translation import gettext_lazy as _


class Voting(models.Model):
    """
    Абстрактная модель голосов
    """

    date_created = models.DateField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    user_vote = models.ForeignKey(
        get_user_model(),
        verbose_name=_("Голосующий"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.date_created

    class Meta:
        abstract = True
        verbose_name = _("Голос")
        verbose_name_plural = _("Голоса")


class OfferVoting(Voting):
    """
    Модель голосов за предложения
    """

    object_vote = models.ForeignKey(
        Offer,
        verbose_name=_("Объект голосования"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.date_created

    class Meta:
        unique_together = ["user_vote", "object_vote"]
        verbose_name = _("Голос (предложения)")
        verbose_name_plural = _("Голоса (предложения)")
