from rest_framework import serializers
from django.contrib.auth.models import User
from bucketlists.models import BucketList
from items.models import Item


class UserSerializer(serializers.ModelSerializer):
    """ Defines the User api representation """
    bucketlists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=BucketList.objects.all())

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bucketlists')
    #Overites the create method of the modle serializeer     
    def create(self, data):
        user = User(
            email=data['email'],
            username=data['username']
        )
        user.set_password(data['password'])
        user.save()
        return user


class BucketListSerializer(serializers.ModelSerializer):
    """ Defines the Bucketlist collections serializer """
    items = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Item.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BucketList
        fields = ('description', 'name', 'date_created',
                  'date_modified', 'items', 'owner')


class ItemSerializer(serializers.ModelSerializer):
    """ Defines the Bucketlist Item serializer """
    bucketlist = serializers.ReadOnlyField(source='bucketlist.name')

    class Meta:
        model = Item
        fields = ('name', 'description', 'done',
                  'date_added', 'date_modified', 'bucketlist')
