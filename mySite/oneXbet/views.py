from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from oneXbet.forms import RegisterUserForm


# Create your views here.

def handler404(request, exception):
    return render(request, '404page.html', status=404)


def handler500(request, exception):
    return render(request, template_name='404page.html', status=500)


def index(request):
    return render(request, 'index.html')


# def login(request):
#     return render(request, 'login.html')


class RegisterUser(CreateView):
    # if request.method == "POST":
    #     form = NewUserForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         messages.success(request, "Registration successful.")
    #         return redirect("main:homepage")
    #     messages.error(request, "Unsuccessful registration. Invalid information.")
    # form = NewUserForm()
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')


class LoginUserForm(LoginView):
    template_name = 'login.html'


@login_required
def custom_logout(request):
    messages.add_message(request, messages.INFO, 'Logged out successfully!')
    logout(request)
    return redirect('home')
