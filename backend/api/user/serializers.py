from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'is_staff', 'password', 'phone', 'is_active', 'is_superuser')
