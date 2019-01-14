from django.urls import path
from .views import (
    IndexView,
    KundList,
    CreateKund,
    KundDelete,
    KundUpdate,
    KundDetail,
    ArbetsplatsList,
    CreateArbetsplats,
    ArbetsplatsDelete,
    ArbetsplatsUpdate,
    ArbetsplatsDetail,
    ProjektList,
    ProjektDetail,
    CreateProjekt,
    ProjektUpdate,
    ProjektDelete
)

app_name = "tid_rapport"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    # Kund
    path("kund/list/", KundList.as_view(), name="kund_list"),
    path("kund/<int:pk>/", KundDetail.as_view(), name="kund_detail"),
    path("kund/create/", CreateKund.as_view(), name="kund_create"),
    path("kund/<int:pk>/update/", KundUpdate.as_view(), name="kund_update"),
    path("kund/<int:pk>/delete/", KundDelete.as_view(), name="kund_delete"),
    # Arbetsplats
    path("arbetsplats/list/", ArbetsplatsList.as_view(), name="arbetsplats_list"),
    path(
        "arbetsplats/<int:pk>/", ArbetsplatsDetail.as_view(), name="arbetsplats_detail"
    ),
    path("arbetsplats/create/", CreateArbetsplats.as_view(), name="arbetsplats_create"),
    path(
        "arbetsplats/<int:pk>/update/",
        ArbetsplatsUpdate.as_view(),
        name="arbetsplats_update",
    ),
    path(
        "arbetsplats/<int:pk>/delete/",
        ArbetsplatsDelete.as_view(),
        name="arbetsplats_delete",
    ),
    # Projekt
    path("projekt/list/", ProjektList.as_view(), name="projekt_list"),
    path("projekt/<int:pk>/", ProjektDetail.as_view(), name="projekt_detail"),
    path("projekt/create/", CreateProjekt.as_view(), name="projekt_create"),
    path("projekt/<int:pk>/update/", ProjektUpdate.as_view(), name="projekt_update"),
    path("projekt/<int:pk>/delete/", ProjektDelete.as_view(), name="projekt_delete"),
]
