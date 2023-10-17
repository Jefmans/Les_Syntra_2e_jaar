from django.db import models

# Create your models here.

class Soort(models.Model):
    naam = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.naam

class Kleur(models.Model):
    naam = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.naam

class Dier(models.Model):
    naam = models.CharField(max_length=20)
    soort = models.ForeignKey(Soort, on_delete=models.CASCADE)
    kleur = models.ForeignKey(Kleur, on_delete=models.CASCADE)
    grootte = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.naam} - {self.soort}"