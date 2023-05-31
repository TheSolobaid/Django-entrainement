from django.db import models


class marque(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    pays = models.CharField(max_length=255, null=True)
    createur = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.nom
class auto(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    puissance = models.CharField(max_length=255, null=True)
    marque = models.ForeignKey(marque, to_field='nom', on_delete=models.CASCADE)
