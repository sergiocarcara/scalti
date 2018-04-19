# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.

#Função para direcionar as pagina na web

#Página principal
def home(request):
    return render(request,'index.html',{})
