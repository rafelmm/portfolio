# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'rmm_portfolio'
urlpatterns = [
    url(r'^$', view=views.index, name='index'),
    url(r'^projects/', view=views.projects, name='projects'),
    url(r'^project/(?P<project_id>[0-9]+)/$', view=views.project_detail, name='project-detail'),
]
