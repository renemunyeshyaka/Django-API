from django.http import JsonResponse
from .models import Fridge
from .serializers import FridgeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        fridge = Fridge.objects.all()
        serializer = FridgeSerializer(fridge, many=True)
        return Response(serializer.data)
        #return JsonResponse({'fridge' : serializer.data})
    if request.method == 'POST':
        serializer = FridgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def fridge_detail(request, id, format=None):
        

        try:
            fridge = Fridge.objects.get(pk=id)
        except Fridge.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)
        

        if request.method == 'GET':
           serializer = FridgeSerializer(fridge)
           return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = FridgeSerializer(fridge, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            fridge.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)