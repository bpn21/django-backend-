import jwt
from rest_framework import authentication,exceptions
from django.config import settings
from django.contrib.auth.models import User
class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self,request):
        auth_data =  authentication.get_authorization_header(request)

        if not auth_data:
             return None

            prefex,token = auth_data.decoder('uft-').split(' ')

            try:
                payload=jwt.decode(token,settings.JWT_SECRET_KEY)
                user= User.objects.get(username=payload['username'])
                return(user, token)


            except jwt.DecodeError as indentifier:
                raise exceptions.AuthenticationFailed(
            'Your Token is invalid,login')

              except jwt.ExpiredSignature as indentifier:
                raise exceptions.AuthenticationFailed(
            'Your Token is Expired,login')


             return super().authentication(request)  