from django.conf.urls import url,include
from lib_admin.views import *

urlpatterns = [
    url(r'^lib1/',lib,name='lib'),
]
