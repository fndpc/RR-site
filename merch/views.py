from django.shortcuts import render

# Create your views here.
def merch(request):
    return render(request, 'merch/merch.html')