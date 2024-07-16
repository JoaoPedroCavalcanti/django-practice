from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return render(req, 'recipes/home.html')

def about(req):
    return HttpResponse("Recipe about")
    
def contact(req):
    return HttpResponse("Recipe contact")
