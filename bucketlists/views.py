from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from userprofile.forms import RegisterForm, LoginForm
from bucketlists.models import BucketList
from bucketlists.forms import BucketListForm
from items.forms import ItemForm
from userprofile.views import DashboardView


class BucketListView(DashboardView):
    template_name = 'bucketlist.html'

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
    template_name = 'bucketlist.html'

    def get_context_data(self, **kwargs):
        bucketlist_id = kwargs['id']
        context = super(BucketListEditView, self).get_context_data(**kwargs)
        return context
        

    def get(self, request, **kwargs):
        bucketlist_id = kwargs['id']
        page = request.GET.get('page')
        bucketlist = BucketList.objects.filter(id=bucketlist_id).first()
        paginator = Paginator(bucketlist.items.all(), 6)
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

