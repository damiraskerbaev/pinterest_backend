from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import *

from .serializers import UserSerializer
from .models import User

@api_view(['GET', 'POST'])
def user(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )
    
@api_view(['GET', 'PUT', 'PATCH'])
def user_detail(request, pk):

    try:
        user=User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(
            status=HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_406_NOT_ACCEPTABLE
        )
    
    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_406_NOT_ACCEPTABLE
        )
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(
            'Deleted succesfully',
            status=HTTP_202_ACCEPTED
        )