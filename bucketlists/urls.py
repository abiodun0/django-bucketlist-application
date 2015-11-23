from django.conf import settings
from django.conf.urls import url
from bucketlists import views

urlpatterns = [
    url(r'^bucketlists/', views.BucketListView.as_view(), name='bucketlists'),
    url(r'^bucketlists/(?P<id>[0-9]+)$', views.BucketListView.as_view(), name='edit_bucketlist'),
   
]
