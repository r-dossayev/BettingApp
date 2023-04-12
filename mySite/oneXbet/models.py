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
    money = models.PositiveIntegerField(blank=True, default=5000, null=True)
    phone = models.CharField(max_length=135, blank=True, null=True)
    avatarImg = models.ImageField(upload_to="userAvatar/", blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    socialAccount = models.CharField(max_length=250, blank=True, null=True)


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

    class Meta:
        get_latest_by = "point"
        ordering = ["point"]
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


def saveService(sum2, count5, count3, pk2, pk1):
    curClub = Club.objects.get(pk=pk2)
    curClub.point = sum2 + 3
    curClub.save()
    curTeam = Club.objects.get(pk=pk2)
    curTeam.wins = count5 + 1
    curTeam.save()
    curTeam2 = Club.objects.get(pk=pk1)
    curTeam2.loses = count3 + 1
    curTeam2.save()


class Game(SoftDeleteModel):
    league = models.ForeignKey(League, null=True, on_delete=models.CASCADE, blank=True)
    club1 = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL, related_name="club1_id")
    club2 = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL)
    start_time = models.TimeField(blank=True)
    result1 = models.PositiveSmallIntegerField(null=True, blank=True)
    result2 = models.PositiveSmallIntegerField(null=True, blank=True)
    url = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('game', kwargs={'slug': self.league.url, 'gameSlug': self.url})

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
            userBetting_2 = Betting.objects.filter(club=team_2).all()
            if self.result1 is not None and self.result2 is not None:
                if self.result1 > self.result2:
                    if userBetting_1:
                        for bet in userBetting_1:
                            betMoney = bet.money
                            user_1 = MyAppUser.objects.get(user_id=bet.user_id)
                            userMoney = user_1.money
                            user_1.money = (betMoney * 2) + userMoney
                            user_1.save()
                            bet.user = None
                            bet.save()
                    if userBetting_2:
                        for bet in userBetting_2:
                            bet.user = None
                            bet.save()
                    saveService(sum1, count2, count6, pk1=self.club2.pk, pk2=self.club1.pk)
                elif self.result1 < self.result2:
                    saveService(sum2, count5, count3, pk1=self.club1.pk, pk2=self.club2.pk)
                    if userBetting_2:
                        for bet in userBetting_2:
                            betMoney = bet.money
                            user_2 = MyAppUser.objects.get(user_id=bet.user_id)
                            userMoney = user_2.money
                            user_2.money = (betMoney * 2) + userMoney
                            user_2.save()
                            bet.user = None
                            bet.save()
                    if userBetting_1:
                        for bet in userBetting_1:
                            bet.user = None
                            bet.save()
                else:
                    curClub = Club.objects.get(pk=self.club1.pk)
                    curClub.point = sum1 + 1
                    curClub.draws = count1 + 1
                    curClub.save()
                    curClub2 = Club.objects.get(pk=self.club2.pk)
                    curClub2.point = sum2 + 1
                    curClub2.draws = count4 + 1
                    curClub2.save()

        return self.save_base(**kwargs)


class Betting(models.Model):
    game = models.ForeignKey(Game, null=True, on_delete=models.SET_NULL)
    club = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, unique=False)
    money = models.PositiveIntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
