from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Projekt, Tid
from .forms import ProjektForm, TidForm, TidSedelForm
from tid_rapport.tidsedel import skapa_tidsedel
from django_currentuser.middleware import get_current_authenticated_user


class IndexView(TemplateView):
    template_name = "index.html"


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
@login_required
def tidlist(request):

    user = get_current_authenticated_user()
    tider = Tid.objects.filter(user=user)

    return render(request, 'tid/tid_list.html', {'tider': tider})


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


@login_required
def tidsedel(request):

    if request.method == 'POST':

        form = TidSedelForm(request.POST)

        if form.is_valid():
            ar = form.cleaned_data['ar']
            start = form.cleaned_data['start_vecka']
            stopp = form.cleaned_data['stopp_vecka']

            if start == stopp:
                filepath = "Tidsedel" + str(ar) + "V" + str(start) + ".xlsx"
            else:
                filepath = "Tidsedel" + str(ar) + "V" + str(start) + "-" + str(stopp) + ".xlsx"
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=' + filepath
            user = get_current_authenticated_user()

            return skapa_tidsedel(ar, start, stopp, response, user)

    else:
        form = TidSedelForm()

    return render(request, 'tidsedel.html', {'form': form})
