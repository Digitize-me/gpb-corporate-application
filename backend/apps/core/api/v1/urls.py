from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("auth/", include("apps.api.auth.v1")),
    path("offers/", include("apps.api.offers.v1")),
    path("voting/", include("apps.api.voting.v1")),
]
