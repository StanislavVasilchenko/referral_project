from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from referral_code.models import ReferralCode
from referral_code.serializers import ReferralSerializer


class ReferralCodeCreateAPIView(generics.CreateAPIView):
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if not self.queryset.filter(user_owner=request.user, is_active=True).exists():
            ref_code = ReferralCode.objects.create(
                user_owner=self.request.user,
                name=request.data.get('name'),
                lifetime=request.data.get('lifetime')
            )
            ref_code.save()
            return Response(self.serializer_class(ref_code).data, status=status.HTTP_201_CREATED)
        return Response({'message': 'You have active code'}, status=status.HTTP_400_BAD_REQUEST)
