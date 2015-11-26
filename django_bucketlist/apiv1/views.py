from django.http import Http404
from django.shortcuts import get_object_or_404
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
        user = request.user
        serialized = UserSerializer(user)
        return Response(serialized.data)

    def post(self, request):
        user = UserSerializer()
        response_user = user.create(data=request.data)
        serialzed_response = UserSerializer(response_user)
        return Response(serialzed_response.data)


class BucketLists(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        bucketlists = request.user.bucketlists
        serialized = BucketListSerializer(bucketlists, many=True)
        return Response(serialized.data)

    def post(self, request, format=None):

        serializer = BucketListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BucketListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        bucketlist_id = kwargs['id']
        bucketlist = get_object_or_404(BucketList, id=bucketlist_id)
        items = bucketlist.items
        serialized = ItemSerializer(items, many=True)
        return Response(serialized.data)

    def put(self, request, format=None, **kwargs):
        bucketlist_id = kwargs['id']
        bucketlist = get_object_or_404(BucketList, id=bucketlist_id)
        serializer = BucketListSerializer(bucketlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        bucketlist_id = kwargs['id']
        bucketlist = get_object_or_404(BucketList, id=bucketlist_id)
        bucketlist.delete()
        return Response("Successfully Deleted")


class BucketListItemsView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None, **kwargs):
        bucketlist_id = kwargs['id']
        bucketlist = get_object_or_404(BucketList, id=bucketlist_id)

        serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(bucketlist=bucketlist)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BucketListItemView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, format=None, **kwargs):
        item_id = kwargs['item_id']
        item = get_object_or_404(Item, id=item_id)

        serializer = ItemSerializer(item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        item_id = kwargs['item_id']
        item = get_object_or_404(Item, id=item_id)
        item.delete()
        return Response("Successfully Deleted")
