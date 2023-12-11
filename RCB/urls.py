from RCB.views import *
from django.urls import path
app_name='PLAY BOLD'

urlpatterns=[
    path('virat/',virat,name='virat'),
    path('abd/',abd,name='abd'),
]