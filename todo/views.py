from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.


@api_view(['GET'])
def all_todos(request:Request):

    if request.method == 'GET':

        todos = Todo.objects.order_by('priority').all()
        todos_serializer = TodoSerializer(todos,many=True)
        return Response(todos_serializer.data,status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
    return Response(None,status.HTTP_400_BAD_REQUEST)