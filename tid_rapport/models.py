import datetime
from django.db import models
from django.urls import reverse


class Kund(models.Model):
    kund_namn = models.CharField(max_length=100)
    kund_kontakt_person = models.CharField(max_length=100, blank=True)
    kund_telefonnr = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.kund_namn)

    def get_absolute_url(self):
        return reverse("tid_rapport:kund_detail", kwargs={"pk": self.pk})


class Arbetsplats(models.Model):
    arbetsplats_namn = models.CharField(max_length=100)
    arbetsplats_kontakt_person = models.CharField(max_length=100, blank=True)
    arbetsplats_telefonnr = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.arbetsplats_namn)

    def get_absolute_url(self):
        return reverse("tid_rapport:arbetsplats_detail", kwargs={"pk": self.pk})


class Projekt(models.Model):
    projektnr = models.IntegerField(default=1900)
    arbetsplats = models.ForeignKey("Arbetsplats", on_delete=models.CASCADE, null=True)
    kund = models.ForeignKey("Kund", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.projektnr)

    def get_absolute_url(self):
        return reverse("tid_rapport:projekt_detail", kwargs={"pk": self.pk})


class Tid(models.Model):

    datum = models.DateField()
    projektnr = models.ForeignKey("Projekt", on_delete=models.CASCADE)
    timmar = models.IntegerField(default=0)
    arbete = models.BooleanField(default=True)
    sjuk = models.BooleanField(default=False)
    tidbank = models.BooleanField(default=False)

    def __str__(self):
        return str(self.datum)

    def get_week(self):
        iso = datetime.date.isocalendar(self.datum)
        week = iso[1]
        return week

    def get_weekday(self):
        weekday = datetime.date.weekday(self.datum)
        if weekday == 0:
            return "Måndag"
        elif weekday == 1:
            return "Tisdag"
        elif weekday == 2:
            return "Onsdag"
        elif weekday == 3:
            return "Torsdag"
        elif weekday == 4:
            return "Fredag"
        elif weekday == 5:
            return "Lördag"
        elif weekday == 6:
            return "Söndag"

    def get_absolute_url(self):
        return reverse("tid_rapport:tid_detail", kwargs={"pk": self.pk})
