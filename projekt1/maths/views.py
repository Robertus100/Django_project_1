from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def div(request, x, y):
    return HttpResponse(f'div = {x / y}')


def mul(request, x, y):
    return HttpResponse(f'mul = {x * y}')


def sub(request, x, y):
    return HttpResponse(f'sub = {x - y}')


def add(request, x, y):
    return HttpResponse(f'add = {x + y}')
