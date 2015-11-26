from django.conf.urls import url
from rest_framework.authtoken import views as restviews
from apiv1 import views

urlpatterns = [
    url(r'^auth/login/', restviews.obtain_auth_token,name="api_login"),
    url(r'^profile/$', views.ProfileView.as_view(), name="api_profile"),
    url(r'^bucketlists/$', views.BucketLists.as_view(),name="api_bucketlist"),
    url(r'^bucketlist/(?P<id>[0-9]+)/$', views.BucketListView.as_view(), name="api_edit_bucketlist"),
    url(r'^bucketlist/(?P<id>[0-9]+)/items/$',
        views.BucketListItemsView.as_view(),name="api_bucketlist_items"),
    url(r'^bucketlist/(?P<id>[0-9]+)/items/(?P<item_id>[0-9]+)/$',
        views.BucketListItemView.as_view(),name="api_edit_bucketlist_items"),


]
