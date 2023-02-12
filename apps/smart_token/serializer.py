"""
@ Author:   gy
@ Date :    2022/8/8
"""
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SmartTokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['token'] = str(refresh.access_token)
        data['expTimestamp'] = refresh.access_token.payload['exp']
        del data['access']
        data['name'] = self.user.username
        return data