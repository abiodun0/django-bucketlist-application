from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from bucketlists.models import BucketList
from items.models import Item
from apiv1.serializers import UserSerializer, BucketListSerializer, ItemSerializer


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = request.user
        serialized = UserSerializer(users)
        return Response(serialized.data)


class BucketList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        bucketlists = request.user.bucketlists
        serialized = BucketListSerializer(bucketlists,many=True)
        return Response(serialized.data)

