from django.shortcuts import render
from django.http import HttpResponse
from . forms import UserForm



# Create your views here.
def main(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    form = UserForm()
    data = {'form': form}
    return render(request, 'main/main.html', data)