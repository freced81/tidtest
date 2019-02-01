import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Arbetsplats(models.Model):


    class Meta:
        verbose_name_plural = "Arbetsplatser"

    arbetsplats_namn = models.CharField(max_length=100, verbose_name="Arbetsplats")

    def __str__(self):
        return str(self.arbetsplats_namn)

    def get_absolute_url(self):
        return reverse("tid_rapport:arbetsplats_detail", kwargs={"pk": self.pk})


class Projekt(models.Model):

    class Meta:
        verbose_name_plural = "Projekt"

    projektnr = models.CharField(max_length=100, verbose_name="Beskrivning")

    def __str__(self):
        return str(self.projektnr)

    def get_absolute_url(self):
        return reverse("tid_rapport:projekt_detail", kwargs={"pk": self.pk})


class Tid(models.Model):


    class Meta:
        verbose_name_plural = "Tider"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Användare")
    ar = models.IntegerField(default=2019, verbose_name="År")
    vecka = models.IntegerField(default=1, verbose_name="Vecka")
    projektnr = models.ForeignKey("Projekt", on_delete=models.CASCADE, verbose_name="Beskrivning")
    mon = models.IntegerField(default=0, verbose_name="Måndag")
    tis = models.IntegerField(default=0, verbose_name="Tisdag")
    ons = models.IntegerField(default=0, verbose_name="Onsdag")
    tors = models.IntegerField(default=0, verbose_name="Torsdag")
    fre = models.IntegerField(default=0, verbose_name="Fredaq")
    lor = models.IntegerField(default=0, verbose_name="Lördag")
    son = models.IntegerField(default=0, verbose_name="Söndag")
    trakt = models.IntegerField(default=0, verbose_name="Trakt")

    def __str__(self):
        return str(self.vecka)

    def get_tot(self):
        tot = (
            self.mon + self.tis + self.ons + self.tors + self.fre + self.lor + self.son
        )
        return tot

    def get_absolute_url(self):
        return reverse("tid_rapport:tid_detail", kwargs={"pk": self.pk})
