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
