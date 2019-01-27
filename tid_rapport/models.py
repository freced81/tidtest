import datetime
from django.db import models
from django.urls import reverse


class Arbetsplats(models.Model):
    arbetsplats_namn = models.CharField(max_length=100)

    def __str__(self):
        return str(self.arbetsplats_namn)

    def get_absolute_url(self):
        return reverse("tid_rapport:arbetsplats_detail", kwargs={"pk": self.pk})


class Projekt(models.Model):
    projektnr = models.CharField(max_length=100)

    def __str__(self):
        return str(self.projektnr)

    def get_absolute_url(self):
        return reverse("tid_rapport:projekt_detail", kwargs={"pk": self.pk})


class Tid(models.Model):

    ar = models.IntegerField(default=2019)
    vecka = models.IntegerField(default=1)
    projektnr = models.ForeignKey("Projekt", on_delete=models.CASCADE)
    mon = models.IntegerField(default=0)
    tis = models.IntegerField(default=0)
    ons = models.IntegerField(default=0)
    tors = models.IntegerField(default=0)
    fre = models.IntegerField(default=0)
    lor = models.IntegerField(default=0)
    son = models.IntegerField(default=0)
    trakt = models.IntegerField(default=0)

    def __str__(self):
        return str(self.vecka)

    def get_tot(self):
        tot = (
            self.mon + self.tis + self.ons + self.tors + self.fre + self.lor + self.son
        )
        return tot

    def get_absolute_url(self):
        return reverse("tid_rapport:tid_detail", kwargs={"pk": self.pk})
