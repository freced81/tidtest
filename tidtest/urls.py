from django.urls import path
from tid_rapport.views import TidList

urlpatterns = [
    path('tid/', TidList.as_view()),
]
