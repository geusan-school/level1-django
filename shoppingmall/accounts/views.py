from django.contrib.auth import login as django_login, authenticate
from accounts.models import User
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['post'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        raise AuthenticationFailed
    django_login(request=request, user=user)
    return Response({ "msg": "로그인 되었음" })


@api_view(['post'])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    try:
        User.objects.create_user(username=username, password=password)
        return Response({"msg": "회원가입 되었음"})
    except:
        raise ValidationError("겹치는 이름입니다")
