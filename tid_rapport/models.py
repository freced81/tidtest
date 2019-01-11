from django.db import models
from django.urls import reverse

class Kund(models.Model):
    kund_namn = models.CharField(max_length=100)
    kund_kontakt_person = models.CharField(max_length=100, blank=True)
    kund_telefonnr = models.CharField(max_length=100)

    def __str__(self):
        return str(self.kund_namn)


class Arbetsplats(models.Model):
    arbetsplats_namn = models.CharField(max_length=100)
    arbetsplats_kontakt_person = models.CharField(max_length=100)
    arbetsplats_telefonnr = models.CharField(max_length=100)

    def __str__(self):
        return str(self.arbetsplats_namn)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})


class Projekt(models.Model):
    projektnr = models.IntegerField(default=1900)
    arbetsplats = models.ForeignKey('Arbetsplats', on_delete=models.CASCADE, null=True)
    kund = models.ForeignKey('Kund', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.projektnr)




class Tid(models.Model):

    datum = models.DateField()
    timmar = models.IntegerField(default=0)
    projektnr = models.ForeignKey('Projekt', on_delete=models.CASCADE)
    arbete = models.BooleanField(default=True)
    sjuk = models.BooleanField(default=False)
    tidbank = models.BooleanField(default=False)

    def __str__(self):
        return str(self.datum)
