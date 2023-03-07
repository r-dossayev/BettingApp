import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class MyAppUser(models.Model):
    def __unicode__(self):
        return self.user.username

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    money = models.PositiveIntegerField(blank=True, default=5000)
    phone = models.CharField(max_length=135, blank=True)


class League(models.Model):
    name = models.CharField(max_length=50)
    poster = models.ImageField(upload_to="leaguesImages/", null=True)
    country = models.CharField(max_length=100, null=True)
    url = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('league', kwargs={'slug': self.url})

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=50)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    description = models.TextField('description')
    poster = models.ImageField(upload_to="clubsPoster/", null=True, blank=True)
    point = models.PositiveSmallIntegerField(default=0)
    wins = models.PositiveSmallIntegerField(default=0)
    draws = models.PositiveSmallIntegerField(default=0)
    loses = models.PositiveSmallIntegerField(default=0)
    url = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('myurl', kwargs={'id': self.id, 'name': self.name})


class Player(models.Model):
    name = models.CharField(max_length=90)
    surname = models.CharField(max_length=90)
    birth = models.DateField(blank=True)
    club = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL)
    description = models.TextField('description')
    image = models.ImageField(upload_to="playersImage/", blank=True)
    url = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Game(SoftDeleteModel):
    club1 = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL, related_name="club1_id")
    club2 = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL)
    start_time = models.TimeField(blank=True)
    result1 = models.PositiveSmallIntegerField(null=True, blank=True)
    result2 = models.PositiveSmallIntegerField(null=True, blank=True)
    url = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url

    def save(self, force_insert=False, **kwargs):
        if self.pk:

            team_1 = Club.objects.get(pk=self.club1.pk)
            team_2 = Club.objects.get(pk=self.club2.pk)
            sum1 = team_1.point
            sum2 = team_2.point
            count1 = team_1.draws
            count2 = team_1.wins
            count3 = team_1.loses
            count4 = team_2.draws
            count5 = team_2.wins
            count6 = team_2.loses
            userBetting_1 = Betting.objects.filter(club=team_1).all()
            print('11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
            print(userBetting_1[0])
            userBetting_2 = Betting.objects.filter(club=team_2).all()
            if self.result1 > self.result2:
                if userBetting_1:
                    for bet in userBetting_1:
                        betMoney = bet.money
                        user_1 = MyAppUser.objects.get(user=bet.user)
                        print( '22222222222222222222222222222')
                        userMoney = user_1.money
                        user_1.money = betMoney + userMoney
                        user_1.save()
                        bet.user = None
                        bet.save()
                if userBetting_2:
                    for bet in userBetting_2:
                        betMoney = bet.money
                        user_1 = MyAppUser.objects.get(user=bet.user)
                        print('22222222222222222222222222222')
                        userMoney = user_1.money
                        user_1.money = betMoney - userMoney
                        user_1.save(user_1)
                        bet.user = None
                        bet.save()
                curClub = Club.objects.get(pk=self.club1.pk)
                curClub.point = sum1 + 3
                curClub.save()
                curTeam = Club.objects.get(self=self.club1)
                curTeam.wins = count2 + 1
                curTeam.save()
                curTeam2 = Club.objects.get(self=self.club2)
                curTeam2.loses = count6 + 1
                curTeam2.save()
            elif self.result1 < self.result2:
                curClub = Club.objects.get(pk=self.club2.pk)
                curClub.point = sum2 + 3
                curClub.save()
                curTeam = Club.objects.get(self=self.club2)
                curTeam.wins = count5 + 1
                curTeam.save()
                curTeam2 = Club.objects.get(self=self.club1)
                curTeam2.loses = count3 + 1
                curTeam2.save()
                if userBetting_2:
                    for bet in userBetting_2:
                        betMoney = bet.money
                        user_2 = MyAppUser.objects.get(user=bet.user)
                        userMoney = user_2.money
                        user_2.money = betMoney + userMoney
                        user_2.save()
                        bet.user = None
                        bet.save()
                if userBetting_1:
                    for bet in userBetting_1:
                        betMoney = bet.money
                        user_2 = MyAppUser.objects.get(user=bet.user)
                        userMoney = user_2.money
                        user_2.money = betMoney - userMoney
                        user_2.save()
                        bet.user = None
                        bet.save()
            else:
                curClub = Club.objects.get(pk=self.club1.pk)
                curClub.point = sum2 + 1
                curClub.save()
                curClub2 = Club.objects.get(pk=self.club2.pk)
                curClub2.point = sum2 + 1
                curClub2.save()
        else:
            print(datetime.time)

        return self.save_base(**kwargs)


class Betting(models.Model):
    game = models.ForeignKey(Game, null=True, on_delete=models.SET_NULL)
    club = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, unique=False)
    draw = models.BooleanField(default=False, blank=True)
    money = models.PositiveIntegerField(blank=True)
    url = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# def upd(club_pk, newPoint):
#     curClub = Club.objects.get(pk=club_pk)
#     curClub.point = newPoint
#     curClub.save()
