from django import forms

from .models import Arbetsplats, Projekt, Tid


class ArbetsplatsForm(forms.ModelForm):
    class Meta:
        model = Arbetsplats
        fields = ("arbetsplats_namn",)
        widgets = {
            "arbetsplats_namn": forms.TextInput(
                attrs={"class": "form-control", "type": "text"}
            )
        }


class ProjektForm(forms.ModelForm):
    class Meta:
        model = Projekt
        fields = ("projektnr", 'arbetsplats',)
        widgets = {"projektnr": forms.TextInput(attrs={"class": "form-control"}),
                   "arbetsplats": forms.Select(attrs={"class": "form-control"}),
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
            "trakt": forms.NumberInput(attrs={"class": "form-control"}),
        }


class TidSedelForm(forms.Form):
    start_vecka = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    stopp_vecka = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
