from django.shortcuts import render
from rest_framework import generics

#from rest_framework import status
#from rest_framework.views import APIView
#from rest_framework.response import Response

from . import  models
from . import serializers

# Create your views here.


# class PostList(APIView):
#     def get(self, request, format=None):
#         posts = models.Post.objects.all()
#         serializer = serializers.PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = serializers.PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListaCreaPost(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class TraeActualizaDestruyePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer



















