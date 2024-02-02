from rest_framework import generics
from .serializers import LoginSerializer, RegisterSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from rest_framework.response import Response


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, many=False)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            if user is not None and user.is_active:
                login(request, user)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)    
        return Response(serializer.errors, status=400)    

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data, many=False)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = User.objects.create(username=username, password=password, is_active=True)
            if user is not None:
                login(request, user)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)    
        return Response(serializer.errors, status=400)    


class LogoutView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(
            {
                'detail':'successfully logged out'
            },
            status=200)
