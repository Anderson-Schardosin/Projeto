from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contato
from .serializers import ContatoSerializer
from rest_framework import permissions


class ContatoList(ListCreateAPIView):

    serializer_class = ContatoSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contato.objects.filter(owner=self.request.user)


class ContatoDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ContatoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_url_kwarg = "id"
    lookup_field = "id"

    def get_queryset(self):
        return Contato.objects.filter(owner=self.request.user)

