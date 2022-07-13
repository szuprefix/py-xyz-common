# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from django.dispatch import Signal

to_save_version = Signal(providing_args=["instance", "exclude_fields"])
to_add_event = Signal(providing_args=["instance", "name", "context"])
new_version_posted = Signal(providing_args=["instance", "history", "changed_fields"])
to_clear_expired_data = Signal(providing_args=["now"])