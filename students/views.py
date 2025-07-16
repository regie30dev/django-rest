from django.http import HttpResponse
from django.shortcuts import render


def list_students(request):
    return HttpResponse('<h2>Hello Regie</h2>')
