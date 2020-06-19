from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OffersConfig(AppConfig):
    """Default app config"""

    name = "apps.api.offers"
    verbose_name = _("Offers")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
