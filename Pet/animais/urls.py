from django.urls import path, include
from .views import AnimaisList, AnimaisDetailView
from rest_framework import routers
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AnimaisList.as_view()),
    path('<int:id>', AnimaisDetailView.as_view()),
]
