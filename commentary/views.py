from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import *

from .serializers import CommentarySerializer
from .models import Commentary

@api_view(['GET', 'POST'])
def commentary(request):

    if request.method == 'GET':
        commentary = Commentary.objects.all()
        serializer = CommentarySerializer(commentary, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    if request.method == 'POST':
        serializer = CommentarySerializer(data=request.data)
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
def commentary_detail(request, pk):

    try:
        commentary=Commentary.objects.get(pk=pk)
    except Commentary.DoesNotExist:
        return Response(
            status=HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        serializer = CommentarySerializer(commentary)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    if request.method == 'PUT':
        serializer = CommentarySerializer(commentary, data=request.data)
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
        serializer = CommentarySerializer(commentary, data=request.data, partial=True)
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
        commentary.delete()
        return Response(
            'Deleted succesfully',
            status=HTTP_202_ACCEPTED
        )