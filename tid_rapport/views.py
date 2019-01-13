from django.views.generic import (TemplateView, ListView,
                                  CreateView, UpdateView,
                                  DeleteView, DetailView)
from django.urls import reverse_lazy
from .models import Kund, Arbetsplats
from .forms import KundForm, ArbetsplatsForm


class IndexView(TemplateView):
    template_name = "index.html"

#Kund
class KundList(ListView):
    template_name = "kund/kund_list.html"
    model = Kund
    context_object_name = 'kunder'

class KundDetail(DetailView):
    template_name = "kund/kund_detail.html"
    model = Kund

class CreateKund(CreateView):
    template_name = "kund/kund_form.html"
    model = Kund
    form_class = KundForm
    success_url = reverse_lazy('tid_rapport:kund_list')

class KundUpdate(UpdateView):
    template_name = "kund/kund_form.html"
    model = Kund
    form_class = KundForm
    success_url = reverse_lazy('tid_rapport:kund_list')

class KundDelete(DeleteView):
    template_name = "kund/kund_confirm_delete.html"
    model = Kund
    success_url = reverse_lazy('tid_rapport:kund_list')


#Arbetsplats
class ArbetsplatsList(ListView):
    template_name = "arbetsplats/arbetsplats_list.html"
    model = Arbetsplats
    context_object_name = 'arbetsplatser'

class ArbetsplatsDetail(DetailView):
    template_name = "arbetsplats/arbetsplats_detail.html"
    model = Arbetsplats

class CreateArbetsplats(CreateView):
    template_name = "arbetsplats/arbetsplats_form.html"
    model = Arbetsplats
    form_class = ArbetsplatsForm
    success_url = reverse_lazy('tid_rapport:arbetsplats_list')

class ArbetsplatsUpdate(UpdateView):
    template_name = "arbetsplats/arbetsplats_form.html"
    model = Arbetsplats
    form_class = ArbetsplatsForm
    success_url = reverse_lazy('tid_rapport:arbetsplats_list')

class ArbetsplatsDelete(DeleteView):
    template_name = "arbetsplats/arbetsplats_confirm_delete.html"
    model = Arbetsplats
    success_url = reverse_lazy('tid_rapport:arbetsplats_list')