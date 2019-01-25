from django import forms

from .models import Kund, Arbetsplats, Projekt, Tid


class KundForm(forms.ModelForm):
    class Meta:
        model = Kund
        fields = ("kund_namn", "kund_kontakt_person", "kund_telefonnr")
        widgets = {
            "kund_namn": forms.TextInput(
                attrs={"class": "form-control", "type": "text"}
            ),
            "kund_kontakt_person": forms.TextInput(attrs={"class": "form-control"}),
            "kund_telefonnr": forms.TextInput(attrs={"class": "form-control"}),
        }


class ArbetsplatsForm(forms.ModelForm):
    class Meta:
        model = Arbetsplats
        fields = (
            "arbetsplats_namn",
            "arbetsplats_kontakt_person",
            "arbetsplats_telefonnr",
        )
        widgets = {
            "arbetsplats_namn": forms.TextInput(
                attrs={"class": "form-control", "type": "text"}
            ),
            "arbetsplats_kontakt_person": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "arbetsplats_telefonnr": forms.TextInput(attrs={"class": "form-control"}),
        }


class ProjektForm(forms.ModelForm):
    class Meta:
        model = Projekt
        fields = ("projektnr", "arbetsplats", "kund")
        widgets = {
            "projektnr": forms.NumberInput(attrs={"class": "form-control"}),
            "arbetsplats": forms.Select(attrs={"class": "form-control"}),
            "kund": forms.Select(attrs={"class": "form-control"}),
        }


class TidForm(forms.ModelForm):
    class Meta:
        model = Tid
        fields = ("datum", "projektnr", "timmar", "arbete", "sjuk", "tidbank")
        widgets = {
            "datum": forms.DateInput(attrs={"class": "form-control"}),
            "projektnr": forms.Select(attrs={"class": "form-control"}),
            "timmar": forms.NumberInput(attrs={"class": "form-control"}),
            "arbete": forms.CheckboxInput(),
            "sjuk": forms.CheckboxInput(),
            "tidbank": forms.CheckboxInput(),
        }


class TidRapportForm(forms.Form):
    week = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))

