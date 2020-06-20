from rest_framework import views, generics, status
from rest_framework.response import Response
from apps.api.offers.models import Offer

# from django.http import Http404


class Voting(views.APIView):
    """
    Базовый класс голосов
    """

    def post(self, request):
        user = request.user
        object_vote = self.kwargs.get("pk")
        if object_vote:
            vote = self.model.objects.create(
                object_vote=object_vote, user_vote=user
            )
            vote.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class OfferVoting(Voting):
    """
    Класс голосов за предложения
    """

    model = Offer
