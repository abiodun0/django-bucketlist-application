from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from userprofile.forms import RegisterForm, LoginForm,ProfileForm
from bucketlists.forms import BucketListForm
from items.forms import ItemForm

# Create your views here.

class IndexView(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(
                '/dashboard',
                context_instance=RequestContext(request)
            )
        return super(IndexView, self).dispatch(request, *args, **kwargs)

class LoginRequiredMixin(object):
    # View mixin which requires that the user is authenticated.

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class IndexBaseView(IndexView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexBaseView, self).get_context_data(**kwargs)
        context['loginform'] = LoginForm(auto_id=False)
        return context

    def post(self, request, *args, **kwargs):

        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Successfully Logged In')
                    return redirect(
                        '/dashboard',
                        context_instance=RequestContext(request)
                    )
            else:
                messages.error(request, 'Username and password incorrect')
                return redirect(
                    '/',
                    context_instance=RequestContext(request)
                )
        else:
            context = super(IndexBaseView, self).get_context_data(**kwargs)
            context['loginform'] = form
            return render(request, self.template_name, context)


class SignUpView(IndexBaseView):
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context['registerform'] = RegisterForm(auto_id=False)
        return context

    def post(self, request, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            login(request, new_user)
            messages.success(request, 'Welcome, you can start creating your bucketlist collection by clicking on the icon above')
            return redirect(
                '/dashboard',
                context_instance=RequestContext(request)
            )
        else:
            print form.errors

            context = super(SignUpView, self).get_context_data(**kwargs)
            context['form_errors'] = form.errors
            context['registerform'] = form
            return render(request, self.template_name, context)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['new_item'] = ItemForm(auto_id=False)
        return context

    def get(self, request, **kwargs):
        page = request.GET.get('page')
        paginator = Paginator(request.user.bucketlists.all(), 6)
        try:
            bucketlists = paginator.page(page)
        except PageNotAnInteger:
            bucketlists = paginator.page(1)
        except EmptyPage:
            bucketlists = paginator.page(paginator.num_pages)

        context = {
            'bucketlists': bucketlists,
            'new_item': ItemForm(auto_id=False),
            'new_bucketlist': BucketListForm(auto_id=False)
        }

        return render(request, self.template_name, context)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    form_class = ProfileForm


    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profileform'] = self.form_class(initial={
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'email': self.request.user.email
            })
        return context

    def post(self, request, **kwargs):
        form = self.form_class(data=request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated')

            return redirect(
                request.META.get('HTTP_REFERER'),
                context_instance=RequestContext(request)
                )
        else:
            messages.error(request, 'There was an error with the fields you entered')

            context = super(ProfileView, self).get_context_data(**kwargs)
            context['profileform'] = self.form_class(initial={
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'email': self.request.user.email
            })
            return render(request, self.template_name, context)

