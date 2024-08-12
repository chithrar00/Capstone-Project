from django.shortcuts import render
from django.http import HttpResponse

# View function to print Hello.
def sayHello(request):
    return HttpResponse('Hello World!')
