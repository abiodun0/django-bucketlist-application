"""This handles the Bucketlist Item Actions"""

from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib import messages
from django.views.generic import View

from .models import Item
from userprofile.views import url_redirect

# Create your views here.


class ItemDeleteView(View):

    """This deletes the item"""

    def post(self, request, **kwargs):
        item_id = kwargs['id']
        item = Item.objects.filter(id=item_id).first()
        item.delete()
        messages.success(request, 'Successfully deleted')
        return url_redirect(request)


class ItemDoneView(View):

    """marks a bucketlist item as done or not done"""

    def post(self, request, **kwargs):
        item_id = kwargs['id']
        item = Item.objects.filter(id=item_id).first()
        if item.done is True:
            item.done = False
            messages.success(request, item.name + ' Marked as not done')

        else:
            item.done = True
            messages.success(request, item.name + ' Marked as done')

        item.save()
        return url_redirect(request)


class ItemEditView(View):

    """Edits the description and name of an item"""

    def post(self, request, **kwargs):
        item_id = kwargs['id']
        item = Item.objects.filter(id=item_id).first()
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()
        messages.success(request, item.name + ' Successfully updated')
        return url_redirect(request)
