from django.urls import path
from django.conf.urls import include
from .views import (
    OfferListCreate,
    TagOfferListCreate,
    TagOfferRetrieveUpdate,
    CategoryOfferListCreate,
    CategoryOfferRetrieveUpdate,
)

app_name = "offers"

urlpatterns = [
    path("", OfferListCreate.as_view()),
    path(
        "tags/",
        include(
            [
                path("", TagOfferListCreate.as_view()),
                path("<int:pk>/", TagOfferRetrieveUpdate.as_view()),
            ]
        ),
    ),
    path(
        "categories/",
        include(
            [
                path("", CategoryOfferListCreate.as_view()),
                path("<int:pk>/", CategoryOfferRetrieveUpdate.as_view()),
            ]
        ),
    ),
]
