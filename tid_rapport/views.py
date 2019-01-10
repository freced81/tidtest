from django.views.generic import ListView
from .models import Tid, Projekt, Arbetsplats, Kund


class TidList(ListView):
    model = Tid
    context_object_name = "tid_rapport"
    template_name = "tid_list.html"
