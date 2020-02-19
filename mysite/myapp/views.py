from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello_world(request):
    return HttpResponse('Hello World, IM!')

def temp(request):
    return render(request, 'temp.html', {
        'value_datetime': datetime.date.today()
        }
    )

def query_str(request):
    return render(request, 'query.html', {
        'test_user': request.GET['user'],
        'test_message': request.GET['message']
        }
    )