from django.conf import settings
from django.conf.urls import url
from items import views

urlpatterns = [
    url(r'^/done/(?P<id>[0-9]+)$',
        views.ItemDoneView.as_view(), name='item_done'),
    url(r'^/delete/(?P<id>[0-9]+)$',
        views.ItemDeleteView.as_view(), name='item_delete'),
    url(r'^/edit/(?P<id>[0-9]+)$',
        views.ItemEditView.as_view(), name='item_edit'),

]
