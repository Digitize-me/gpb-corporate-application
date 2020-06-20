from django.urls import path
from django.conf.urls import include
from .views import (
    TagListCreate,
    TagRetrieveUpdate,
    CategoryListCreate,
    CategoryRetrieveUpdate,
)

app_name = "offers"

urlpatterns = [
    # path("", .as_view()),
    # path("<int:pk>/", .as_view()),
    path(
        "tags/",
        include(
            [
                path("", TagListCreate.as_view()),
                path("<int:pk>/", TagRetrieveUpdate.as_view()),
            ]
        ),
    ),
    path(
        "categories/",
        include(
            [
                path("", CategoryListCreate.as_view()),
                path("<int:pk>/", CategoryRetrieveUpdate.as_view()),
            ]
        ),
    ),
]
