from django.conf.urls import url, include
from django.conf.urls import include
from rest_framework.authtoken import views as restviews
from rest_framework.urlpatterns import format_suffix_patterns
from apiv1 import views

urlpatterns = [
    url(r'^auth/login/', restviews.obtain_auth_token),
    url(r'^profile/$', views.ProfileView.as_view()),
    url(r'^bucketlists/$', views.BucketLists.as_view()),
    url(r'^bucketlist/(?P<id>[0-9]+)/$', views.BucketListView.as_view()),
    url(r'^bucketlist/(?P<id>[0-9]+)/items/$', views.BucketListItemsView.as_view()),
    url(r'^bucketlist/(?P<id>[0-9]+)/items/(?P<item_id>[0-9]+)/$', views.BucketListItemView.as_view()),

    
]
