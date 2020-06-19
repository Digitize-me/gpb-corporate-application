from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EventsConfig(AppConfig):
    """Default app config"""

    name = "apps.api.events"
    verbose_name = _("Events")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
