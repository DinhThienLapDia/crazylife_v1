from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import (TokenAuthentication,
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import json
from  core.models import  UserProfile
from django.contrib.auth.models import User

from django.core.validators import validate_email
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
 
from allauth.socialaccount import providers
from allauth.socialaccount.models import SocialLogin, SocialToken, SocialApp
from allauth.socialaccount.providers.facebook.views import fb_complete_login
from allauth.socialaccount.helpers import complete_social_login
#from geld.auth import EverybodyCanAuthentication


class AccountSignup(APIView):
    #authentication_classes = (SessionAuthentication, TokenAuthentication)
    #permission_classes = (IsAuthenticated,)
    #renderer_classes = (JSONRenderer,)
    def post(self, request, format=None):
        """ sign up new account. """
        if not ("email" in request.data and "password" in request.data and "username" in request.data):
            return Response("error missing params", status=status.HTTP_400_BAD_REQUEST)

        usernameinput = str(request.data['username'])
        emailinput = str(request.data['email'])
        passwordinput = str(request.data['password'])
        print usernameinput, emailinput, passwordinput
        valid_email = True
        try:
            validate_email(emailinput)
            valid_email = True
        except :
            valid_email = False
        if ((len(usernameinput) < 3)  or (len(passwordinput) < 3) or not valid_email):
            return Response("Invalid param input", status=status.HTTP_400_BAD_REQUEST)

        if (User.objects.filter(username = usernameinput).exists() or User.objects.filter(email = emailinput).exists()):
            return Response({'status':"user existed" }, status=status.HTTP_200_OK)

        else:
            newuser = User.objects.create_user(username=usernameinput,email=emailinput,password=passwordinput)
            UserProfile.objects.create(user=newuser)
            return Response({'status':"success"}, status=status.HTTP_200_OK)
        

class AccountSignin(APIView):
    def post(self, request, format=None):
        """ sign up new account. """
        if not ("email" in request.data and "password" in request.data):
            return Response("error missing params", status=status.HTTP_400_BAD_REQUEST)

        
        emailinput = str(request.data['email'])
        passwordinput = str(request.data['password'])
        print emailinput, passwordinput
        valid_email = True
        try:
            validate_email(emailinput)
            valid_email = True
        except :
            valid_email = False
        if ((len(passwordinput) < 3) or not valid_email):
            return Response("Invalid param input", status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.get(email=emailinput).check_password(passwordinput):
            return Response({'status':"success" }, status=status.HTTP_200_OK)

        else:
            
            return Response({'status':"incorrect"}, status=status.HTTP_200_OK)


class FacebookSignin(APIView):
   # permission_classes = (AllowAny,)
    
    # this is a public api!!!
   # authentication_classes = (EverybodyCanAuthentication,)
             
    def dispatch(self, *args, **kwargs):
        return super(FacebookSignin, self).dispatch(*args, **kwargs)
    
    def post(self, request):        
        data = JSONParser().parse(request)
        access_token = data.get('access_token', '')    
        
        try:
            app = SocialApp.objects.get(provider="facebook")
            token = SocialToken(app=app, token=access_token)
                            
            # check token against facebook                  
            login = fb_complete_login(app, token)
            login.token = token
            login.state = SocialLogin.state_from_request(request)
        
            # add or update the user into users table
            ret = complete_social_login(request, login)
 
            # if we get here we've succeeded
            return Response(status=200, data={
                'success': True,
                'username': request.user.username,
                'user_id': request.user.pk,
            })
            
        except:
 
            return Response(status=401 ,data={
                'success': False,
                'reason': "Bad Access Token",
            })


class ListAction(APIView):
    pass

class GetNotifications(APIView):
    pass

class GetMyAction(APIView):
    pass

class LikeAction(APIView):
    pass

class Comment(APIView):
    pass

class SendInvitation(APIView):
    pass

class AcceptInvitation(APIView):
    pass
