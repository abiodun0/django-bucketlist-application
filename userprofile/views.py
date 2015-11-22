from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext, loader

from userprofile.forms import RegisterForm, LoginForm

# Create your views here.


class LoginRequiredMixin(object):
    # View mixin which requires that the user is authenticated.

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)



class IndexBaseView(TemplateView):
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
                    messages.add_message(
                        request, messages.SUCCESS, 'Logged in Successfully!')
                    return redirect(
                        '/home',
                        context_instance=RequestContext(request)
                    )
            else:
                messages.add_message(
                    request, messages.ERROR, 'Incorrect username or password!')
                return redirect(
                    '/',
                    context_instance=RequestContext(request)
                )
        else:
            context = super(LoginView, self).get_context_data(**kwargs)
            context['loginform'] = form
            return render(request, self.template_name, context)


class SignUpView(TemplateView):
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

            return redirect(
                '/user/' + self.request.user.username + '/profile/',
                context_instance=RequestContext(request)
            )
        else:
            print form.errors

            context = super(SignUpView, self).get_context_data(**kwargs)
            context['form_errors'] = form.errors
            context['registerform'] = form
            return render(request, self.template_name, context)