from django.urls import path
from django.conf.urls import include
from .views import (
    EventListCreate,
    TagEventListCreate,
    TagEventRetrieveUpdate,
    CategoryEventListCreate,
    CategoryEventRetrieveUpdate,
)

app_name = "events"

urlpatterns = [
    path("", EventListCreate.as_view(), name="index"),
    path(
        "tags/",
        include(
            [
                path("", TagEventListCreate.as_view()),
                path("<int:pk>/", TagEventRetrieveUpdate.as_view()),
            ]
        ),
    ),
    path(
        "categories/",
        include(
            [
                path("", CategoryEventListCreate.as_view()),
                path("<int:pk>/", CategoryEventRetrieveUpdate.as_view()),
            ]
        ),
    ),
]
