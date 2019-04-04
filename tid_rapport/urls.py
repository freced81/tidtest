from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    IndexView,
    ProjektList,
    ProjektDetail,
    CreateProjekt,
    ProjektUpdate,
    ProjektDelete,
    TidDetail,
    tidlist,
    CreateTid,
    TidUpdate,
    TidDelete,
    tidsedel,
)

app_name = "tid_rapport"

urlpatterns = [
    path("start/", login_required(IndexView.as_view()), name="index"),
    # Projekt
    path("projekt/list/", login_required(ProjektList.as_view()), name="projekt_list"),
    path(
        "projekt/<int:pk>/",
        login_required(ProjektDetail.as_view()),
        name="projekt_detail",
    ),
    path(
        "projekt/create/",
        login_required(CreateProjekt.as_view()),
        name="projekt_create",
    ),
    path(
        "projekt/<int:pk>/update/",
        login_required(ProjektUpdate.as_view()),
        name="projekt_update",
    ),
    path(
        "projekt/<int:pk>/delete/",
        login_required(ProjektDelete.as_view()),
        name="projekt_delete",
    ),
    # Tid
    path("tid/list/", tidlist, name="tid_list"),
    path("tid/<int:pk>/", login_required(TidDetail.as_view()), name="tid_detail"),
    path("tid/create/", login_required(CreateTid.as_view()), name="tid_create"),
    path(
        "tid/<int:pk>/update/", login_required(TidUpdate.as_view()), name="tid_update"
    ),
    path(
        "tid/<int:pk>/delete/", login_required(TidDelete.as_view()), name="tid_delete"
    ),
    path("tidsedel/", tidsedel, name="tidsedel"),
]
