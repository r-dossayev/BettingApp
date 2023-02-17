from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from oneXbet.forms import RegisterUserForm


# Create your views here.

def handler404(request, exception):
    return render(request, '404page.html', status=404)


def handler500(exception):
    return render(template_name='404page.html', status=500)


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


class RegisterUser(CreateView):

    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Регистрация")
    #     return dict(list(context.items()) + list(c_def.items()))
