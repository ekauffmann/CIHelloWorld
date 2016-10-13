from django.shortcuts import HttpResponse

# Create your views here.

def hello_world(request):
    return HttpResponse('<h2>Hello world !</h2>')
