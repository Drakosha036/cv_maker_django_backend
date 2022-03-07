from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from .models import Softskill

# Create your views here.


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    code, message = Softskill.create(request.data)
    print(code)
    if code == 200:
        return Response({'message' : message}, status= HTTP_200_OK)
    else:
        return Response({'message': message}, status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def getSoftskill(request):
    print(request.query_params)
    if request.query_params.get("name"):
        code, response = Softskill.getSoftskill(request.query_params.get("name"))
    else:
        code, response = Softskill.getAllSoftskill()
    return Response({'message': str(response)}, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def getAllSoftskill(request):
    code, response = Softskill.getAllSoftskill()
    return Response({'message': str(response)}, status=HTTP_200_OK)