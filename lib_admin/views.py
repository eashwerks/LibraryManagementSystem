# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
def lib(request):
    return render(request,'Lms_HomePage.html',{})
