from django.urls import path, include
from .views import ContatoList, ContatoDetailView
from rest_framework import routers
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ContatoList.as_view()),
    path('<int:id>', ContatoDetailView.as_view()),


]
