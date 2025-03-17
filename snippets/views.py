from django.shortcuts import render
from django.http import HttpResponseRedirect
from  . forms import SnipetsForm
from  . models import Snipet



# Create your views here.


def snippets(request):


    snipets = Snipet.objects.all



    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SnipetsForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/snippets")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SnipetsForm()

    return render(request, "snippets/snippets.html", {"form": form, "snipets": snipets})