from django.views.generic import (ListView, TemplateView,
                                  DeleteView, CreateView,
                                  UpdateView)
from .models import Tid, Projekt, Arbetsplats, Kund
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"


class TidListView(ListView):
    model = Tid
    context_object_name = "tid_list"
    template_name = "tid_list.html"


class KundListView(ListView):
    model = Kund
    context_object_name = "kund_list"
    template_name = "kund_list.html"


class ProjektListView(ListView):
    model = Projekt
    context_object_name = "projekt_list"
    template_name = "projekt_list.html"


# Arbetsplats
class ArbetsplatsListView(ListView):
    model = Arbetsplats
    context_object_name = "arbetsplats_list"
    template_name = "arbetsplats_list.html"


class CreateArbetsplatsView(CreateView):
    model = Arbetsplats


class ArbetsplatsUpdateView(UpdateView):
    model = Arbetsplats


class ArbetsplatsDeleteView(DeleteView):
    model = Arbetsplats
    template_name = "arbetsplats_list.html"
    success_url = reverse_lazy('tid_rapport:arbetsplats_list')
