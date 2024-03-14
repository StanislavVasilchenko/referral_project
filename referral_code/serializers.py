from rest_framework import serializers

from referral_code.models import ReferralCode


class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCode
        exclude = ['id', 'user_owner']


class ReferralCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCode
        fields = ('code',)
