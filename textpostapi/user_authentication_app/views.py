from django.shortcuts import render
from rest_framework import generics, status
from .serializers import SignupSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.response import Response




# Create your views here.


class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({ "status":status.HTTP_200_OK,'refresh': str(refresh), 'access': str(refresh.access_token)})
            
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

