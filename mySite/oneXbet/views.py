from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
# from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView

from oneXbet.forms import *
from oneXbet.models import League, Game


def handler404(request, exception):
    return render(request, '404page.html', status=404)


def handler500(exception):
    return redirect(handler404)


def index(request):
    return render(request, 'index.html')


def football(request):
    context = {"leagues": League.objects.all()}
    return render(request, template_name="oneXbet/football/football.html", context=context)


def league(request, slug):
    context = {'league': League.objects.get(url=slug)}
    print(context.get('league').url)
    return render(request, 'oneXbet/football/table.html', context)  # default table html


def games(request, slug):
    leagueA = League.objects.get(url=slug)
    currentLeagueGames = Game.objects.filter(league=leagueA).filter(is_deleted=False)

    context = {'games': currentLeagueGames, 'league': League.objects.get(url=slug)}
    return render(request, 'oneXbet/football/games.html', context)
    # league games page


def game(request, slug, gameSlug):
    context = {'game': Game.objects.get(url=gameSlug),'league': League.objects.get(url=slug)}
    return render(request, 'oneXbet/football/game.html', context)


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


class BettingPage(CreateView):
    form_class = BettingForm
    template_name = 'oneXbet/betting.html'

    def form_valid(self, form=form_class):
        betting = form.save(commit=False)
        betting.user = self.request.user
        betting.save()
        messages.add_message(self.request, messages.INFO, 'betting created successfully!')
        return redirect(reverse('home'))


class LoginUserForm(LoginView):
    template_name = 'login.html'


@login_required
def custom_logout(request):
    messages.add_message(request, messages.WARNING, 'Logged out successfully!')
    logout(request)
    return redirect('home')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'oneXbet/contact.html'
    success_url = 'home'

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

    # def get_context_data(self, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['title'] = Book.objects.all()
    #     return context
