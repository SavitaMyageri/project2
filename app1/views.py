from django.shortcuts import render

from django.http import HttpResponse

def savu(request):
    return HttpResponse ('hi hello')

def madu(request):
    return HttpResponse('how are u')
