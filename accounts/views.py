from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import SignupSerializer
# Create your views here.

class Signup(APIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = SignupSerializer(data = data)
        if serializer.is_valid():
            user = serializer.save()
            Token.objects.create(user = user)

            return Response(serializer.data, status = 201)

        return Response(serializer.errors, status = 400)

#xreate your login class here
