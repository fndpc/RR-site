from  . forms import SnipetsForm
from  . models import Snipet
from django.views.generic.list import ListView
from django.views.generic import CreateView


class SnippetsView(ListView):
    model = Snipet
    template_name = 'snippets/snippets.html'
    context_object_name = 'snippets'
    def get_queryset(self):
        return super().get_queryset()

# views.py
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Snipet
from .forms import SnipetsForm

class SnippetsAddView(CreateView):
    template_name = 'snippets/snippets_add.html'
    model = Snipet
    form_class = SnipetsForm
    success_url = reverse_lazy('snipet-list')

    def form_valid(self, form):
        return super().form_valid(form)



# def snippets(request):
#     snipets = Snipet.objects.all

#     #Форма для добавления снипета
#     if request.method == "POST":
#         form = SnipetsForm(request.POST, request.FILES)
#         # check whether it's valid:
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/snippets")
#     else:
#         form = SnipetsForm()
#     return render(request, "snippets/snippets.html", {"form": form, "snipets": snipets})