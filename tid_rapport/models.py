from django.db import models


class Kund(models.Model):
    kund_namn = models.CharField(max_length=100)
    kund_kontakt_person = models.CharField(max_length=100, default="Lägg till...")
    kund_telefonnr = models.CharField(max_length=100, default="Lägg till...")

    def __str__(self):
        return str(self.kund_namn)


class Arbetsplats(models.Model):
    arbtsplats_namn = models.CharField(max_length=100)
    arbetsplats_kontakt_person = models.CharField(max_length=100, default="Lägg till...")
    arbetsplats_telefonnr = models.CharField(max_length=100, default="Lägg till...")

    def __str__(self):
        return str(self.arbtsplats_namn)


class Projekt(models.Model):
    projektnr = models.IntegerField(default=1900)
    arbetsplats = models.ManyToManyField(Arbetsplats)
    kund = models.ManyToManyField(Kund)

    def __str__(self):
        return str(self.projektnr)




class Tid(models.Model):

    datum = models.DateField()
    timmar = models.IntegerField(default=0)
    projektnr = models.ForeignKey(Projekt, on_delete=models.CASCADE)
    arbete = models.BooleanField(default=True)
    sjuk = models.BooleanField(default=False)
    tidbank = models.BooleanField(default=False)

    def __str__(self):
        return str(self.datum)
