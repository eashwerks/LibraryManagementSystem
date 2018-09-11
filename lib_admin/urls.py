from django.conf.urls import url,include
from lib_admin.views import *

urlpatterns = [
    url(r'^lib/',lib,name='lib'),
]
