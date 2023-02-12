from django.db import models


class League(models.Model):
    name = models.CharField(max_length=50)
    url = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# wedfg

class Club(models.Model):
    name = models.CharField(max_length=50)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    description = models.TextField('description')
    poster = models.ImageField(upload_to="clubsPoster/", null=True)
    url = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


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


class Game(models.Model):
    club1 = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL, related_name="club1_id")
    club2 = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL)
    start_time = models.TimeField(blank=True)
    result1 = models.PositiveSmallIntegerField(default=0)
    result2 = models.PositiveSmallIntegerField(default=0)
    url = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Betting(models.Model):
    game = models.ForeignKey(Game,  null=True, on_delete=models.SET_NULL)
    club = models.ForeignKey(Club, null=True,  on_delete=models.SET_NULL)
    draw = models.BooleanField(default=False, blank=True)
    money = models.PositiveIntegerField(blank=True)
    url = models.SlugField(max_length=160, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
