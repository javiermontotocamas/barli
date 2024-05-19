from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import AdminProfile, UserProfile, Bar, Table, find_user_or_bar_and_role_by_django_user_id , Advertisement, Booking

# Clase para meter claims personalizados en el token jwt, agregamos username y rol
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        entity, role = find_user_or_bar_and_role_by_django_user_id(user.id)
        token['role'] = role
        token['entity_id'] = entity.id
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = AdminProfile
        fields = ['id', 'user']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'fullname', 'phone', 'birthdate']

    def create(self, validated_data):
        user_auth_data = validated_data.pop('user')
        user = User.objects.create_user(user_auth_data['username'], email=user_auth_data['email'], password=user_auth_data['password'])
        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile


class BarSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Bar
        fields = ['id', 'user', 'name', 'description', 'phone', 'address', 'latitude', 'longitude']


    def create(self, validated_data):
        user_auth_data = validated_data.pop('user')
        user = User.objects.create_user(user_auth_data['username'], email=user_auth_data['email'], password=user_auth_data['password'])
        bar_profile = Bar.objects.create(user=user, **validated_data)
        return bar_profile


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'bar', 'number', 'status', 'seats', 'outdoor']


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'bar', 'product_name', 'reduction']

class BookingSerializer(serializers.ModelSerializer):
    bar = BarSerializer(source='table.bar', read_only=True, required=False)
    class Meta:
        model = Booking
        fields = ['id', 'user', 'table', 'initial_datetime', 'end_datetime', 'completed','bar']
