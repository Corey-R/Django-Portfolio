from django.shortcuts import render, HttpResponse

# Create your views here.

def projects(request):
    return render(request, 'projects.html')