from django.urls import path
from .views import OfferVoting, EventVoting

app_name = "voting"

urlpatterns = [
    path("offer/<int:pk>", OfferVoting.as_view()),
    path("event/<int:pk>", EventVoting.as_view()),
]
