# -*- coding:utf-8 -*- 

from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType


class ContenttypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ("app_label", 'model', 'name', 'id')
