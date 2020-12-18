from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Animais
from .serializers import AnimaisSerializer
from rest_framework import permissions


class AnimaisList(ListCreateAPIView):

    serializer_class = AnimaisSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Animais.objects.filter(owner=self.request.user)


class AnimaisDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = AnimaisSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Animais.objects.filter(owner=self.request.user)

from django.shortcuts import render

# Create your views here.
