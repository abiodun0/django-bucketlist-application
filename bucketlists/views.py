from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext, loader

from userprofile.forms import RegisterForm, LoginForm
from bucketlists.models import BucketList
from bucketlists.forms import BucketListForm
from items.forms import ItemForm


class BucketListView(TemplateView):

    def post(self, request, **kwargs):
        form = BucketListForm(request.POST)
        bucketlist = form.save(commit=False)
        bucketlist.owner = request.user
        bucketlist.save()
        return redirect(
            '/dashboard',
            context_instance=RequestContext(request)
        )
    pass

class BucketListEditView(TemplateView):

    def post(self, request, **kwargs):
        bucketlist_id = kwargs['id']
        bucketlist = BucketList.objects.filter(id=bucketlist_id).first()
        bucketlist.name = request.POST['name']
        bucketlist.description = request.POST['description']
        if 'color' in request.POST:
            bucketlist.color = request.POST['color']

        bucketlist.save()
        return redirect(
            '/dashboard',
            context_instance=RequestContext(request)
        )
    pass

class BucketListAddItemView(TemplateView):
    def post(self, request, **kwargs):
        bucketlist_id = kwargs['id']
        bucketlist = BucketList.objects.filter(id=bucketlist_id).first()
        form = ItemForm(request.POST)
        item = form.save(commit=False)
        item.bucketlist = bucketlist
        item.done = False
        item.save()
        return redirect(
            '/dashboard',
            context_instance=RequestContext(request)
        )

class BucketListDeleteView(TemplateView):
    def post(self, request, **kwargs):
        bucketlist_id = kwargs['id']
        bucketlist = BucketList.objects.filter(id=bucketlist_id).first()
        bucketlist.delete()
        return redirect(
            '/dashboard',
            context_instance=RequestContext(request)
        )

