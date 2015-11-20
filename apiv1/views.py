from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response("Yellow")


class BucketList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        return Response("Blue")
