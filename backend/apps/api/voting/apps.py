from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VotingConfig(AppConfig):
    """Default app config"""

    name = "apps.api.voting"
    verbose_name = _("Voting")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
