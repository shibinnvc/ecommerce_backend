from django.http import JsonResponse
from django.shortcuts import render


def handler404(request, exception):
    message = ('Route not found')
    response = JsonResponse(data={'error': message})
    response.status_code = 404
    return response

def handler500(request):
    # Your custom error handling logic here
    context = {'error_message': 'An internal server error'}
    return render(request, '500.html', context)

