from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import guestBook
from .serializers import bookSerializers

@api_view(['GET', 'POST', 'DELETE'])
def content_list(request):
    if request.method == 'GET':
        guests = guestBook.objects.all()
        serializer = bookSerializers(guests, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = bookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def content_detail(request, pk):
    try:
        book = guestBook.objects.get(pk=pk)
    except guestBook.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = bookSerializers(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = bookSerializers(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)