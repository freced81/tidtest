from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    IndexView,
    ArbetsplatsList,
    CreateArbetsplats,
    ArbetsplatsDelete,
    ArbetsplatsUpdate,
    ArbetsplatsDetail,
    ProjektList,
    ProjektDetail,
    CreateProjekt,
    ProjektUpdate,
    ProjektDelete,
    TidList,
    TidDetail,
    CreateTid,
    TidUpdate,
    TidDelete,
)

app_name = "tid_rapport"

urlpatterns = [
    path("start/", login_required(IndexView.as_view()), name="index"),
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
    # Tid
    path("tid/list/", TidList.as_view(), name="tid_list"),
    path("tid/<int:pk>/", TidDetail.as_view(), name="tid_detail"),
    path("tid/create/", CreateTid.as_view(), name="tid_create"),
    path("tid/<int:pk>/update/", TidUpdate.as_view(), name="tid_update"),
    path("tid/<int:pk>/delete/", TidDelete.as_view(), name="tid_delete"),
]
