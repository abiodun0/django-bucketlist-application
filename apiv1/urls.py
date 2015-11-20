from django.conf.urls import url, include
from django.conf.urls import include
from rest_framework.authtoken import views as restviews
from rest_framework.urlpatterns import format_suffix_patterns
from apiv1 import views

urlpatterns = [
    url(r'^get_api_token/', restviews.obtain_auth_token),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^profile/$', views.ProfileView.as_view()),
    url(r'^bucketlists/$', views.BucketList.as_view()),
]
