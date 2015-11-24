from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.template import RequestContext, loader
from .models import Item

# Create your views here.

        
class ItemDeleteView(View):

    def post(self, request, **kwargs):
        item_id = kwargs['id']
        item = Item.objects.filter(id=item_id).first()
        item.delete()
        return redirect(
            request.META.get('HTTP_REFERER'),
            context_instance=RequestContext(request)
            )

class ItemDoneView(View):
    def post(self, request, **kwargs):
        item_id = kwargs['id']
        item = Item.objects.filter(id=item_id).first()
        if item.done is True:
            item.done = False
        else:
            item.done = True
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
        item.done = bool(request.POST['done'])
        item.save()
        return redirect(
            request.META.get('HTTP_REFERER'),
            context_instance=RequestContext(request)
            )
