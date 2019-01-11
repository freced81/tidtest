from django.urls import path
from .views import (TidListView, KundListView,
                    ProjektListView, IndexView,
                    ArbetsplatsListView, CreateArbetsplatsView,
                    ArbetsplatsUpdateView, ArbetsplatsDeleteView)

app_name = 'tid_rapport'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tid/', TidListView.as_view(), name='tid_list'),
    path('kund/', KundListView.as_view(), name='kund_list'),
    path('projekt/', ProjektListView.as_view(), name='projekt_list'),
    path('arbetsplats/', ArbetsplatsListView.as_view(), name='arbetsplats_list'),
    path('arbetsplats/new/', CreateArbetsplatsView.as_view(), name='arbetsplats_new'),
    path('arbetsplats/<int:pk>/edit/', ArbetsplatsUpdateView.as_view(), name='arbetsplats_edit'),
    path('arbetsplats/<int:pk>/delete/', ArbetsplatsDeleteView.as_view(), name='arbetsplats_delete'),
]

