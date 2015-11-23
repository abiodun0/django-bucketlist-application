from django.conf import settings
from django.conf.urls import url
from userprofile import views

urlpatterns = [
    url(r'^$', views.IndexBaseView.as_view(), name='index'),
    url(r'^signup$', views.SignUpView.as_view(), name='signup'),
    url(r'^dashboard$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^profile$', views.DashboardView.as_view(), name='profile'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
]
