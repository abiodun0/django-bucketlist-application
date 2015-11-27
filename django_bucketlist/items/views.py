from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib import messages
from django.views.generic import View

from .models import Item

# Create your views here.


class ItemDeleteView(View):

    def post(self, request, **kwargs):
        item_id = kwargs['id']
        item = Item.objects.filter(id=item_id).first()
        item.delete()
        messages.success(request, 'Successfully deleted')
        return redirect(
            '/',
            context_instance=RequestContext(request)
        )


class ItemDoneView(View):

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
        return redirect(
            request.META.get('HTTP_REFERER'),
            context_instance=RequestContext(request)
        )


class ItemEditView(View):

    def post(self, request, **kwargs):
        item_id = kwargs['id']
        item = Item.objects.filter(id=item_id).first()
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()
        messages.success(request, item.name + ' Successfully updated')
        return redirect(
            request.META.get('HTTP_REFERER'),
            context_instance=RequestContext(request)
        )
