from django.http import JsonResponse


def studentsView(request):
    students = {
        'id': '0001',
        'name': 'Regie',
        'class': 'Machine learning'
    }
    return JsonResponse(students)
