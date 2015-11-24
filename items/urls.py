from django.conf import settings
from django.conf.urls import url
from items import views

urlpatterns = [
    url(r'^(?P<id>[0-9]+)$', views.ItemDoneView.as_view(), name='item_done'),
    url(r'^(?P<id>[0-9]+)$',
        views.ItemDeleteView.as_view(), name='item_delete'),
    url(r'^(?P<id>[0-9]+)$', views.ItemEditView.as_view(), name='item_edit'),

]
