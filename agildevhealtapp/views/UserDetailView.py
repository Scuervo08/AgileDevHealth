from ast import Return
from urllib import response
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from agildevhealtapp import serializers
from agildevhealtapp.models.user import User
from agildevhealtapp.serializers.UserSerializer import UserSerializer
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'head']


    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)

    def post (self, request, *args, **kwargs):
        self.http_method_names.append('GET')
        serializers =UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response (serializers.data,status=status.HTTP_201_CREATED)
        return Response (serializers.errors, status=status.HTTP_400_BAD_REQUEST)