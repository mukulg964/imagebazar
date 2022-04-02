from django.http import HttpResponse
from django.shortcuts import render

def show_about_page(request):
    return render(request,'about.html')