from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import datetime


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
        print(self.club2.name + "QQQQQQQQQQQQQQQQQQQQ")
        if self.pk:
            print("qqqqqqqqqqqqq1111111111111")
            print(datetime.datetime.now().strftime("%H:%M:%S"))
        else:
            print(datetime.time)
            sTime = self.start_time
            if sTime == datetime.time:
                self.result2 = 12

        return self.save_base(**kwargs)


class Betting(models.Model):
    game = models.ForeignKey(Game, null=True, on_delete=models.SET_NULL)
    club = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    draw = models.BooleanField(default=False, blank=True)
    money = models.PositiveIntegerField(blank=True)
    url = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
