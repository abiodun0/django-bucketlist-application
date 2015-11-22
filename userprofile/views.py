from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView
from django.shortcuts import render

from userprofile.forms import RegisterForm

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
        return context

class SignUpView(TemplateView):
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context['registerform'] = RegisterForm(auto_id=False)
        return context