from django.conf import settings
from django.conf.urls import url
from bucketlists import views

urlpatterns = [
    url(r'^bucketlists$', views.BucketListView.as_view(), name='bucketlists'),
   
]
