from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from api_basics.models import article
from api_basics.serializers import articleSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        article1 = article.objects.all()
        serializer = articleSerializers(article1, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = articleSerializers(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, pk):
    try:
        articles = article.objects.get(pk = pk)
    except article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = articleSerializers(articles)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = articleSerializers(articles, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        articles.delete()
        return HttpResponse(status= status.HTTP_204_NO_CONTENT)

    

