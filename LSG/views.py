from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rahul(request):
    return render(request,'rahul.html')

def dekock(request):
    return HttpResponse('<h1><marquee>de kock is the wicket keeper of LSG </marquee></h1>')
