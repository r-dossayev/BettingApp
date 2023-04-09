from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, FormView
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from oneXbet.forms import *
from oneXbet.models import League, Game, MyAppUser, Club
from oneXbet.serializers import LeagueSerializer, ClubSerializer, RegisterSerializer


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
    return render(request, 'oneXbet/football/table.html', context)  # default table html


def games(request, slug):
    leagueA = League.objects.get(url=slug)
    currentLeagueGames = Game.objects.filter(league=leagueA).filter(is_deleted=False)

    context = {'games': currentLeagueGames, 'league': League.objects.get(url=slug)}
    return render(request, 'oneXbet/football/games.html', context)
    # league games page


def game(request, slug, gameSlug):
    context = {'game': Game.objects.get(url=gameSlug), 'league': League.objects.get(url=slug)}
    if request.method == "POST":
        currentUser = MyAppUser.objects.get(user_id=request.user.pk)
        if request.POST["win"] and request.POST["money"]:
            betMoney = int(request.POST["money"])
            currentTeamId = int(request.POST["win"])
            if currentUser.money >= betMoney:
                newBetting = Betting()
                newBetting.user = request.user
                newBetting.money = betMoney
                newBetting.game = Game.objects.get(url=gameSlug)
                newBetting.club = None if currentTeamId == 0 else Club.objects.get(pk=currentTeamId)
                # self betting club = null, and bet to draw or success win one club betting
                newBetting.save()
                currentUser.money = currentUser.money - betMoney
                currentUser.save()
            else:
                messages.warning(request, "no money")
                return redirect('profile')
        else:
            messages.warning(request, "not required fields")
            return render(request, 'oneXbet/football/game.html', context)
    return render(request, 'oneXbet/football/game.html', context)


def registerUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            myNewUser = MyAppUser()
            myNewUser.user = user
            myNewUser.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterUserForm()
    context = {"form": form}
    return render(request, 'register.html', context)
    # form_class = RegisterUserForm
    # template_name = 'register.html'
    # success_url = reverse_lazy('home')


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


def profileView(request):
    newUser = MyAppUser.objects.get(user_id=request.user.pk)
    form = UserUpdateForm(instance=newUser)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=newUser)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = UserUpdateForm(instance=newUser)
    context = {"form": form, "myUser": newUser}
    return render(request, template_name="oneXbet/profile.html", context=context)


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


# API controller

class FootballLeaguesViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class LeagueClubsViewSet(viewsets.ModelViewSet):
    # queryset = Club.objects.all()
    # queryset = League.objects.get(pk=2).club_set
    serializer_class = ClubSerializer

    def get_queryset(self):
        url = self.kwargs.get('url')
        # pk = self.kwargs.get('pk',self.kwargs.get('id'))
        try:
            return League.objects.get(url=url).club_set
        except:
            return League.objects.get(pk=1).club_set


class RegisterViewAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# @api_view(["POST"])
# def adminLogin(request):
#     print("Ssssssssssssssssssssssssssss")
#     if (request.method == "POST"):
#         username = request.data["username"]
#         password = request.data["password"]
#         print("Ssssssssssssssssssssssssssss")
#         authenticated_user = authenticate(request, username=username, password=password)
#         print("Ssssssssssssssssssssssssssss")
#         if authenticated_user != None:
#
#             if (authenticated_user.is_authenticated and authenticated_user.is_superuser):
#                 login(request, authenticated_user)
#                 return Response({"Message": "User is Authenticated. "})
#             else:
#                 return Response({"message": "User is not authenticated. "})
#         else:
#             return Response({"Message": "Either User is not registered or password does not match"})
#     print("Ssssssssssssssssssssssssssss")
