from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.template import RequestContext, loader
from .models import Item

# Create your views here.
class ItemDoneView(TemplateView):
    def post(self, request, **kwargs):
        item_id = kwargs['id']
        item = Item.objects.filter(id=item_id).first()
        if item.done is True:
            item.done = False
        else:
            item.done = True
        item.save()
        return redirect(
            '/dashboard',
            context_instance=RequestContext(request)
        )