from django.views.generic import ListView
from .models import Tid


class TidList(ListView):
    model = Tid
    context_object_name = 'tid_rapport'
    template_name = 'tid.html'