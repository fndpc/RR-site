from  . forms import SnipetsForm
from  . models import Snipet
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin


class SnippetsView(PermissionRequiredMixin, ListView):
    model = Snipet
    template_name = 'snippets/snippets.html'
    context_object_name = 'snippets'
    permission_required = 'snippets.view_Snipet'

    def get_queryset(self):
        return super().get_queryset()

# views.py
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Snipet
from .forms import SnipetsForm

class SnippetsAddView(PermissionRequiredMixin, CreateView):
    template_name = 'snippets/snippets_add.html'
    model = Snipet
    form_class = SnipetsForm
    success_url = reverse_lazy('snipet-list')
    permission_required = 'snippets.add_Snipet'

    def form_valid(self, form):
        return super().form_valid(form)
