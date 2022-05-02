from django.shortcuts import render

# Create your views here.
def index(request, *args, **kwargs):        # https://www.geeksforgeeks.org/args-kwargs-python/
    return render(request, 'frontend/index.html')