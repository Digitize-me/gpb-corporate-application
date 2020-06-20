from django.urls import path
from .views import OfferVoting

app_name = "voting"

urlpatterns = [
    path("offer/<int:pk>", OfferVoting.as_view()),
]
