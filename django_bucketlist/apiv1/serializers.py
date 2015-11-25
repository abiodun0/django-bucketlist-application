from rest_framework import serializers
from django.contrib.auth.models import User
from bucketlists.models import BucketList
from items.models import Item


class UserSerializer(serializers.ModelSerializer):
    bucketlists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=BucketList.objects.all())

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bucketlists')

    def create(self, data):
        user = User(
            email=data['email'],
            username=data['username']
        )
        user.set_password(data['password'])
        user.save()
        return user


class BucketListSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Item.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BucketList
        fields = ('description', 'name', 'date_created', 'date_modified','items', 'owner')



class ItemSerializer(serializers.ModelSerializer):
    bucketlist = serializers.ReadOnlyField(source='bucketlist.name')

    class Meta:
        model = Item
        fields = ('name', 'description', 'done',
                  'date_added', 'date_modified', 'bucketlist')

