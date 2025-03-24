from django.shortcuts import render

# Create your views here.
def merch(request):

    me = request.user
    data = {'me': me}
    return render(request, 'merch/merch.html', data)