from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.middleware.csrf import get_token
from django.core.mail import send_mail
import random

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    @swagger_auto_schema(responses={201: "User registered successfully"})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class VerifyOTPView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'otp': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={200: "OTP verified", 400: "Invalid OTP"}
    )
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        user = CustomUser.objects.filter(email=email, otp=otp).first()
        if user:
            user.is_verified = True
            user.otp = None
            user.save()
            return Response({'message': 'OTP verified'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer, responses={200: "Login successful", 400: "Invalid credentials"})
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
            if user:
                login(request, user)
                response = JsonResponse({'message': 'Login successful'})
                response.set_cookie('auth_token', user.auth_token.key, httponly=True, secure=True)
                return response
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(responses={200: UserSerializer})
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class LogoutView(APIView):
    @swagger_auto_schema(responses={200: "Logged out"})
    def post(self, request):
        logout(request)
        response = JsonResponse({'message': 'Logged out'})
        response.delete_cookie('auth_token')
        return response

class CSRFTokenView(APIView):
    @swagger_auto_schema(responses={200: "CSRF token generated"})
    def get(self, request):
        return JsonResponse({'csrfToken': get_token(request)})

# Simple frontend view

def frontend_view(request):
    return render(request, 'index.html')
