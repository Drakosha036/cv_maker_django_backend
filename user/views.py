from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from .models import Users


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("email")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = Users.login(username,password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)






@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def helloworld(request):
    print(request.user)
    print(request.user.password)
    code,response = Users.get(request.user)
    return Response({'message': str(response)},
                    status=HTTP_200_OK)




@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    
    
    code,message = Users.create(request.data)
    print(code)
    if code == 200:
        return Response({'message': message},
                        status=HTTP_200_OK)
    else:
        return Response({'message': message},
                        status=HTTP_400_BAD_REQUEST) 