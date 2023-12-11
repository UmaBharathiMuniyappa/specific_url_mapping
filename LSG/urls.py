from LSG.views import *
from django.urls import path
app_name='Lucknow Super Giants'

urlpatterns=[
    path('rahul/',rahul,name='rahul'),
    path('dekock/',dekock,name='dekock')
]