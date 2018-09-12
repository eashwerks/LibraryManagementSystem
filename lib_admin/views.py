# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'Lms_HomePage.html',{})
def about(request):
    return render(request,'About.html',{})
