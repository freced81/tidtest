from django import forms

from .models import Projekt, Tid



class ProjektForm(forms.ModelForm):
    class Meta:
        model = Projekt
        fields = ("projektnr", "anlaggning", 'ort', "kund")



class TidForm(forms.ModelForm):
    class Meta:
        model = Tid
        fields = (
            "ar",
            "vecka",
            "projektnr",
            "mon",
            "tis",
            "ons",
            "tors",
            "fre",
            "lor",
            "son",
            "restid",
            "trakt",
            "pmil",
            "fmil",
        )


class TidSedelForm(forms.Form):
    ar = forms.IntegerField()
    start_vecka = forms.IntegerField()
    stopp_vecka = forms.IntegerField()
