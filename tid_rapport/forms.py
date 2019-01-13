from django import forms

from .models import Kund, Arbetsplats


class KundForm(forms.ModelForm):

    class Meta:
        model = Kund
        fields = ("kund_namn", "kund_kontakt_person", "kund_telefonnr")
        widgets = {"kund_namn": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
                   "kund_kontakt_person": forms.TextInput(attrs={"class": "form-control"}),
                   "kund_telefonnr": forms.TextInput(attrs={"class": "form-control"}),
                   }


class ArbetsplatsForm(forms.ModelForm):

    class Meta:
        model = Arbetsplats
        fields = ("arbetsplats_namn", "arbetsplats_kontakt_person", "arbetsplats_telefonnr")
        widgets = {"arbetsplats_namn": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
                   "arbetsplats_kontakt_person": forms.TextInput(attrs={"class": "form-control"}),
                   "arbetsplats_telefonnr": forms.TextInput(attrs={"class": "form-control"}),
                   }