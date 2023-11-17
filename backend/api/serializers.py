from rest_framework import serializers
from .models import UserProfile, Bar
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'fullname', 'phone', 'email', 'birthdate']

    def create(self, validated_data):
        user_auth_data = validated_data.pop('user')
        user = User.objects.create_user(user_auth_data['username'], email=validated_data['email'], password=user_auth_data['password'])
        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile
