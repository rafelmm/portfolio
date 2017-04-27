# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'rmm_contact'
urlpatterns = [
    url(r'^$', view=views.index, name='index'),
]
