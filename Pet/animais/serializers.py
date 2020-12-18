from rest_framework.serializers import ModelSerializer
from .models import Animais


class AnimaisSerializer(ModelSerializer):

    class Meta:
        model = Animais

        fields = '__all__'