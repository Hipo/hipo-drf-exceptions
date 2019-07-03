# coding: utf-8

from __future__ import unicode_literals

from django.conf.urls import url
from .views import CreateItemView

urlpatterns = [
    url(r"^create-item/$", CreateItemView.as_view(), name="create-item"),
]