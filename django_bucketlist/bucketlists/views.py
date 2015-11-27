"""The bucketlist collection Action views"""

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from bucketlists.models import BucketList
from bucketlists.forms import BucketListForm
from items.forms import ItemForm
from userprofile.views import DashboardView


class BucketListView(DashboardView):

    """Creates a new bucketlist"""
    def post(self, request, **kwargs):
        form = BucketListForm(request.POST)
        bucketlist = form.save(commit=False)
        bucketlist.owner = request.user
        bucketlist.save()
        messages.success(request, bucketlist.name + ' Successfully created')
        url = request.META.get('HTTP_REFERER') if request.META.get('HTTP_REFERER') is not None else '/dashboard'
        return redirect(
            url,
            context_instance=RequestContext(request)
        )


class BucketListEditView(TemplateView):
    """Edits a particular bucketlist"""
    template_name = 'bucketlist.html'

    def get(self, request, **kwargs):
        #Gets all the item for a particular bucketlist
        bucketlist_id = kwargs['id']
        page = request.GET.get('page')
        q = request.GET.get('q', "")
        bucketlist = BucketList.objects.filter(id=bucketlist_id).first()
        paginator = Paginator(bucketlist.items.filter(name__contains=q), 6)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context = {}
        context['items'] = items
        context['bucketlist'] = bucketlist
        context['new_item'] = ItemForm(auto_id=False)
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        #edits the bucketlist name , description or theme
        bucketlist_id = kwargs['id']
        bucketlist = BucketList.objects.filter(id=bucketlist_id).first()
        bucketlist.name = request.POST['name']
        bucketlist.description = request.POST['description']
        if 'color' in request.POST:
            bucketlist.color = request.POST['color']

        bucketlist.save()
        messages.success(request, bucketlist.name + ' updated')
        url = request.META.get('HTTP_REFERER') if request.META.get('HTTP_REFERER') is not None else '/dashboard'
        return redirect(
            url,
            context_instance=RequestContext(request)
        )


class BucketListAddItemView(TemplateView):
    """Adds an item to a bucketlist collection"""

    def post(self, request, **kwargs):
        bucketlist_id = kwargs['id']
        bucketlist = BucketList.objects.filter(id=bucketlist_id).first()
        form = ItemForm(request.POST)
        item = form.save(commit=False)
        item.bucketlist = bucketlist
        item.done = False
        item.save()
        messages.success(request, item.name + ' Added to ' + bucketlist.name)
        return redirect(
            request.META.get('HTTP_REFERER'),
            context_instance=RequestContext(request)
        )


class BucketListDeleteView(TemplateView):
    """ Deletes a bucketlist item """

    def post(self, request, **kwargs):
        bucketlist_id = kwargs['id']
        bucketlist = BucketList.objects.filter(id=bucketlist_id).first()
        bucketlist.delete()
        messages.success(request, 'Successfully Deleted')
        url = request.META.get('HTTP_REFERER') if request.META.get('HTTP_REFERER') is not None else '/dashboard'
        return redirect(
            url,
            context_instance=RequestContext(request)
        )
