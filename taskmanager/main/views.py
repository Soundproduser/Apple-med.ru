from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4>go</h4>")


def go(request):
    return HttpResponse("<h4>привет</h4>")