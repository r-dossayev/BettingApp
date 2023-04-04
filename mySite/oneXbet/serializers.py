from rest_framework import serializers

from oneXbet.models import League


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('name', 'poster', 'country', 'created_at', 'club_set')
