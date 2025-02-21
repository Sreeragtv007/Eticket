from rest_framework import serializers
from .models import Customuser
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CustomuserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customuser
        fields = '__all__'

    def validate(self, attrs):
        print(attrs)
        return attrs

    def create(self, validated_data):
        user = validated_data.pop('user')
        user = User.objects.create_user(**user)
        customuser = Customuser.objects.create(user=user, **validated_data)
        return customuser
