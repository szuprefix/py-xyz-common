# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from . import serializers, models
from rest_framework import viewsets, decorators
from xyz_restful.decorators import register

__author__ = 'denishuang'


from django.contrib.contenttypes.models  import ContentType


@register()
class ContenttypeViewSet(viewsets.ModelViewSet):
    queryset = ContentType.objects.all().order_by('app_label')
    serializer_class = serializers.ContenttypeSerializer
    search_fields = ('app_label', 'model')
    filter_fields = {
        'id': ['exact', 'in']
    }

    def filter_queryset(self, queryset):
        from xyz_auth.helper import get_user_model_permissions
        from django.db.models import Q
        mps = get_user_model_permissions(self.request.user)
        ms = [m.split('.') for m in mps.keys()]
        lookup = None
        for m in ms:
            q = Q(**dict(app_label=m[0], model=m[1]))
            lookup = (lookup | q) if lookup else q
        return lookup and queryset.filter(lookup) or queryset
