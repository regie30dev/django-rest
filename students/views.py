from django.http import HttpResponse


def list_students(request):
    return HttpResponse('<h2>Hello Regie</h2>')
