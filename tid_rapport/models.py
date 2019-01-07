from django.db import models

# Create your models here.


class Tid(models.Model):

    datum = models.DateField()
    timmar = models.IntegerField(default=0)
    projektnr = models.IntegerField(default=1900)
    arbetsplats = models.CharField(max_length=60)
    kund = models.CharField(max_length=60)
    arbete = models.BooleanField()
    sjuk = models.BooleanField()
    tidbank = models.BooleanField()

    def __str__(self):
        return str(self.datum)