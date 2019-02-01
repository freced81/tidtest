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
    tidsedel
)

app_name = "tid_rapport"

urlpatterns = [
    path("start/", login_required(IndexView.as_view()), name="index"),
    # Arbetsplats
    path("arbetsplats/list/", login_required(ArbetsplatsList.as_view()), name="arbetsplats_list"),
    path(
        "arbetsplats/<int:pk>/", login_required(ArbetsplatsDetail.as_view()), name="arbetsplats_detail"
    ),
    path("arbetsplats/create/", login_required(CreateArbetsplats.as_view()), name="arbetsplats_create"),
    path(
        "arbetsplats/<int:pk>/update/",
        login_required(ArbetsplatsUpdate.as_view()),
        name="arbetsplats_update",
    ),
    path(
        "arbetsplats/<int:pk>/delete/",
        login_required(ArbetsplatsDelete.as_view()),
        name="arbetsplats_delete",
    ),
    # Projekt
    path("projekt/list/", login_required(ProjektList.as_view()), name="projekt_list"),
    path("projekt/<int:pk>/", login_required(ProjektDetail.as_view()), name="projekt_detail"),
    path("projekt/create/", login_required(CreateProjekt.as_view()), name="projekt_create"),
    path("projekt/<int:pk>/update/", login_required(ProjektUpdate.as_view()), name="projekt_update"),
    path("projekt/<int:pk>/delete/", login_required(ProjektDelete.as_view()), name="projekt_delete"),
    # Tid
    path("tid/list/", login_required(TidList.as_view()), name="tid_list"),
    path("tid/<int:pk>/", login_required(TidDetail.as_view()), name="tid_detail"),
    path("tid/create/", login_required(CreateTid.as_view()), name="tid_create"),
    path("tid/<int:pk>/update/", login_required(TidUpdate.as_view()), name="tid_update"),
    path("tid/<int:pk>/delete/", login_required(TidDelete.as_view()), name="tid_delete"),

    path("tidsedel/", tidsedel, name="tidsedel")
]
