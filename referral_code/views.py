from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from referral_code.models import ReferralCode
from referral_code.permissions import IsReferralCodeOwner
from referral_code.serializers import ReferralSerializer, ReferralCodeSerializer
from referral_code.services import generate_ref_code
from users.models import User


class ReferralCodeCreateAPIView(generics.CreateAPIView):
    """Create a new referral code"""
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        if not self.queryset.filter(user_owner=user, is_active=True).exists():
            ref_code = ReferralCode.objects.create(
                user_owner=self.request.user,
                name=request.data.get('name'),
                lifetime=request.data.get('lifetime'),
                code=generate_ref_code(),
            )
            ref_code.save()
            user.is_referrer = True
            user.save()
            return Response(self.serializer_class(ref_code).data, status=status.HTTP_201_CREATED)
        return Response({'message': 'You have active code'}, status=status.HTTP_400_BAD_REQUEST)


class ReferralCodeDelete(generics.DestroyAPIView):
    """Delete an existing referral code"""
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralSerializer
    permission_classes = [IsAuthenticated, IsReferralCodeOwner]


class ReferralCodeGetAPIView(APIView):
    """Get active referral codes for a given user email"""
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralCodeSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)

            try:
                code = ReferralCode.objects.get(user_owner=user, is_active=True)
            except ReferralCode.DoesNotExist:
                return Response('Code not found', status=status.HTTP_404_NOT_FOUND)

            serializer = ReferralCodeSerializer(code)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe(request, *args, **kwargs):
    """Subscribe to referral codes"""
    if request.method == 'POST':
        code_number = request.data.get('code')
        try:
            code = ReferralCode.objects.get(code=code_number, is_active=True)
        except ReferralCode.DoesNotExist:
            return Response({'message': 'Code not found'}, status=status.HTTP_404_NOT_FOUND)

        user = request.user
        if code.user_owner == user:
            return Response({'message': 'You own referral code'}, status=status.HTTP_403_FORBIDDEN)
        user.subscriber = code.user_owner
        user.save()
        return Response({'message': f"Subscribed to referral code {code.name}"}, status=status.HTTP_200_OK)

