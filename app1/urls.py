from django.urls import path
from app1.views import *
app_name='somethigfdn'

urlpatterns=[
    path('savu/',savu,name='savu'),
    path('madu/',madu,name='madu')
]