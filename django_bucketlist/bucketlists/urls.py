"""Controls the model for the bucketlist app"""
from django.conf import settings
from django.conf.urls import url
from bucketlists import views

urlpatterns = [
    url(r'^bucketlists/', views.BucketListView.as_view(), name='bucketlists'),
    url(r'^bucketlist/(?P<id>[0-9]+)$',
        views.BucketListEditView.as_view(), name='edit_bucketlist'),
    url(r'^bucketlist-delete/(?P<id>[0-9]+)$',
        views.BucketListDeleteView.as_view(), name='delete_bucketlist'),
    url(r'^bucketlist/(?P<id>[0-9]+)/items$',
        views.BucketListAddItemView.as_view(), name='add_item'),

]
