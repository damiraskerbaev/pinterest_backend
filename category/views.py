from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import *

from .serializers import CategorySerializer
from .models import Category

@api_view(['GET', 'POST'])
def category(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
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
def category_detail(request, pk):

    try:
        category=Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(
            status=HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
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
        serializer = CategorySerializer(category, data=request.data, partial=True)
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
        category.delete()
        return Response(
            'Deleted succesfully',
            status=HTTP_202_ACCEPTED
        )