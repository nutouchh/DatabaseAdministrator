from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

# Views for main application

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')
@login_required
def instruction(request):
    return render(request, 'main/instructions.html')

def page_not_found(request, exception):
    return render(request, 'all/not_found.html')

