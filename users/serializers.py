from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class UserDetailSerializer(serializers.ModelSerializer):
    subscribers = SerializerMethodField()

    def get_subscribers(self, obj):
        return UserSerializer(User.objects.filter(subscriber_id=obj.id), many=True).data

    class Meta:
        model = User
        fields = ('id', 'subscribers')
