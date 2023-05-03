import array

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from oneXbet.models import League, Club, MyAppUser


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        read_only_fields = ('created_at',)
        fields = ('id', 'name', 'poster', 'country', 'url', 'created_at')


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        read_only_fields = ('created_at',)
        fields = ('id', 'name', 'description', 'poster', 'url', 'created_at', 'point', 'draws', 'loses', 'wins')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True,
                                      validators=[validate_password])
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    def validate(self, attrs):
        if attrs.get('password1') != attrs.get('password2'):
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password1'])
        user.save()
        myNewUser = MyAppUser()
        myNewUser.user = user
        myNewUser.save()
        return user


class AuthMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyAppUser
        fields = "__all__"


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'last_name', 'first_name']
