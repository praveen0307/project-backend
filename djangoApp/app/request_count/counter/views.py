from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

count = 0 

def count_requests(request):
    global count 
    count += 1
    return HttpResponse(f"request count = {count}")