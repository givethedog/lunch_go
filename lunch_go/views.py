from django.shortcuts import render

def index(request):
    return render(request, 'lunch_go/lunch_main.html')
