
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Url


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = '__all__'


class UrlSerializer1(serializers.Serializer):

    long_url = serializers.CharField(max_length=200)
