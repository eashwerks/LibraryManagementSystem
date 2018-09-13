from django.conf.urls import url,include
from lib_admin.views import *

urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'about/',about,name='about'),
]
