from django.shortcuts import render

# Create your views here.

def homeElearning(request):
    return render(request, 'base/main.html')
