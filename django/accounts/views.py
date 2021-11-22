from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):

    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST) 
    if len(password) < 8:
        return Response({'error': '비밀번호를 8자리 이상 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST) 
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    serializer= UserSerializer(user)
    return Response(serializer.data)
