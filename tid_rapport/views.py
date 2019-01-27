from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.urls import reverse_lazy
from .models import Arbetsplats, Projekt, Tid
from .forms import ArbetsplatsForm, ProjektForm, TidForm


class IndexView(TemplateView):
    template_name = "index.html"


# Arbetsplats
class ArbetsplatsList(ListView):
    template_name = "arbetsplats/arbetsplats_list.html"
    model = Arbetsplats
    context_object_name = "arbetsplatser"


class ArbetsplatsDetail(DetailView):
    template_name = "arbetsplats/arbetsplats_detail.html"
    model = Arbetsplats


class CreateArbetsplats(CreateView):
    template_name = "arbetsplats/arbetsplats_form.html"
    model = Arbetsplats
    form_class = ArbetsplatsForm
    success_url = reverse_lazy("tid_rapport:arbetsplats_list")


class ArbetsplatsUpdate(UpdateView):
    template_name = "arbetsplats/arbetsplats_form.html"
    model = Arbetsplats
    form_class = ArbetsplatsForm
    success_url = reverse_lazy("tid_rapport:arbetsplats_list")


class ArbetsplatsDelete(DeleteView):
    template_name = "arbetsplats/arbetsplats_confirm_delete.html"
    model = Arbetsplats
    success_url = reverse_lazy("tid_rapport:arbetsplats_list")


# Projekt
class ProjektList(ListView):
    template_name = "projekt/projekt_list.html"
    model = Projekt
    context_object_name = "projekt"


class ProjektDetail(DetailView):
    template_name = "projekt/projekt_detail.html"
    model = Projekt


class CreateProjekt(CreateView):
    template_name = "projekt/projekt_form.html"
    model = Projekt
    form_class = ProjektForm
    success_url = reverse_lazy("tid_rapport:projekt_list")


class ProjektUpdate(UpdateView):
    template_name = "projekt/projekt_form.html"
    model = Projekt
    form_class = ProjektForm
    success_url = reverse_lazy("tid_rapport:projekt_list")


class ProjektDelete(DeleteView):
    template_name = "projekt/projekt_confirm_delete.html"
    model = Projekt
    success_url = reverse_lazy("tid_rapport:projekt_list")


# Tid
class TidList(ListView):
    template_name = "tid/tid_list.html"
    model = Tid
    context_object_name = "tider"


class TidDetail(DetailView):
    template_name = "tid/tid_detail.html"
    model = Tid


class CreateTid(CreateView):
    template_name = "tid/tid_form.html"
    model = Tid
    form_class = TidForm
    success_url = reverse_lazy("tid_rapport:tid_list")


class TidUpdate(UpdateView):
    template_name = "tid/tid_form.html"
    model = Tid
    form_class = TidForm
    success_url = reverse_lazy("tid_rapport:tid_list")


class TidDelete(DeleteView):
    template_name = "tid/tid_confirm_delete.html"
    model = Tid
    success_url = reverse_lazy("tid_rapport:tid_list")
