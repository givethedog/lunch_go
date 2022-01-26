from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    return render(request, 'main.html')
    # return HttpResponse("main page")

# Create your views here.
