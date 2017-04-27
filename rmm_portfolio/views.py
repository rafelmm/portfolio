# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def index(request):
    return render(request, 'rmm_portfolio/index.html')


def projects(request):
    return render(request, 'rmm_portfolio/projects.html')


def project_detail(request, project_id):
    return render(request, 'rmm_portfolio/project_detail.html', {'id': project_id})
