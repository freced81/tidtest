from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField


class Projekt(models.Model):
    class Meta:
        verbose_name_plural = "Projekt"
        ordering = ["projektnr"]

    projektnr = models.CharField(max_length=100, verbose_name="Projektnummer", blank=True)
    anlaggning = models.CharField(max_length=100, verbose_name="Anläggning", blank=True)
    kund = models.CharField(max_length=100, verbose_name="Kund", blank=True)
    ort = models.CharField(max_length=100, verbose_name="Ort", blank=True)

    def __str__(self):
        return str(self.projektnr)

    def get_absolute_url(self):
        return reverse("tid_rapport:projekt_detail", kwargs={"pk": self.pk})


class Tid(models.Model):
    class Meta:
        verbose_name_plural = "Tider"
        ordering = ["-ar", "-vecka"]

    user = CurrentUserField()
    ar = models.IntegerField(default=2019, verbose_name="År")
    vecka = models.IntegerField(default=1, verbose_name="Vecka")
    projektnr = models.ForeignKey(
        "Projekt", on_delete=models.CASCADE, verbose_name="Projekt"
    )
    mon = models.FloatField(default=0, verbose_name="Måndag")
    tis = models.FloatField(default=0, verbose_name="Tisdag")
    ons = models.FloatField(default=0, verbose_name="Onsdag")
    tors = models.FloatField(default=0, verbose_name="Torsdag")
    fre = models.FloatField(default=0, verbose_name="Fredaq")
    lor = models.FloatField(default=0, verbose_name="Lördag")
    son = models.FloatField(default=0, verbose_name="Söndag")
    restid = models.FloatField(default=0, verbose_name="Restid")
    trakt = models.IntegerField(default=0, verbose_name="Trakt")
    pmil = models.IntegerField(default=0, verbose_name="Mil egen bil")
    fmil = models.IntegerField(default=0, verbose_name="Mil firmabil bil")

    def __str__(self):
        return str(self.vecka)

    def get_tot(self):
        tot = (
            self.mon
            + self.tis
            + self.ons
            + self.tors
            + self.fre
            + self.lor
            + self.son
            + self.restid
        )
        return tot

    def get_full_name(self):
        return self.user.first_name + " " + self.user.last_name

    def get_absolute_url(self):
        return reverse("tid_rapport:tid_detail", kwargs={"pk": self.pk})
