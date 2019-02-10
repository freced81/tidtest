from django import forms

from .models import Projekt, Tid



class ProjektForm(forms.ModelForm):
    class Meta:
        model = Projekt
        fields = ("projektnr", "anlaggning", 'ort', "kund")
        widgets = {"projektnr": forms.TextInput(attrs={"class": "form-control"}),
                   "anlaggning": forms.TextInput(attrs={"class": "form-control"}),
                   "ort": forms.TextInput(attrs={"class": "form-control"}),
                   "kund": forms.TextInput(attrs={"class": "form-control"}),
                   }


class TidForm(forms.ModelForm):
    class Meta:
        model = Tid
        fields = (
            "user",
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
        )
        widgets = {
            "user": forms.Select(attrs={"class": "form-control"}),
            "ar": forms.NumberInput(attrs={"class": "form-control"}),
            "vecka": forms.NumberInput(attrs={"class": "form-control"}),
            "projektnr": forms.Select(attrs={"class": "form-control"}),
            "mon": forms.NumberInput(attrs={"class": "form-control"}),
            "tis": forms.NumberInput(attrs={"class": "form-control"}),
            "ons": forms.NumberInput(attrs={"class": "form-control"}),
            "tors": forms.NumberInput(attrs={"class": "form-control"}),
            "fre": forms.NumberInput(attrs={"class": "form-control"}),
            "lor": forms.NumberInput(attrs={"class": "form-control"}),
            "son": forms.NumberInput(attrs={"class": "form-control"}),
            "restid": forms.NumberInput(attrs={"class": "form-control"}),
            "trakt": forms.NumberInput(attrs={"class": "form-control"}),
        }


class TidSedelForm(forms.Form):
    ar = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    start_vecka = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    stopp_vecka = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
