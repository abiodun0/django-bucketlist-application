from django.conf import settings
from django.conf.urls import url
from userprofile import views

urlpatterns = [
    url(r'^$', views.IndexBaseView.as_view(), name='index'),
    url(r'^signup$', views.SignUpView.as_view(), name='signup'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
]
