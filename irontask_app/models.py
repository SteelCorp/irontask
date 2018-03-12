from django.db import models
from django.core.validators import RegexValidator


# Create your models here.



class Intervenant(models.Model):
    """
    Class Reprénsentant un intervenant
    """
    siret = models.PositiveIntegerField(max_length=14, primary_key=True)
    raisonSocial = models.CharField(max_length=50, verbose_name='Raison Sociale', blank=False, null=False)
    type = models.CharField(max_length=50, blank=False, null=False)
    adresse = models.CharField(max_length=200, blank=False, null=False)
    codePostal = models.PositiveSmallIntegerField(max_length=5, blank=False, null=False)
    ville = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField()


class Sponsor(models.Model):
    """
    Class Reprénsentant un sponsor
    """

    siret = models.PositiveIntegerField(max_length=14, primary_key=True)
    raisonSocial = models.CharField(max_length=50, verbose_name='Raison Sociale', blank=False, null=False)
    adresse = models.CharField(max_length=200, blank=False, null=False)
    codePostal = models.CharField(max_length=5, blank=False, null=False)
    ville = models.CharField(max_length=50, blank=False, null=False)
    telephone = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField()


class Categorie(models.Model):
    """
    Class Reprénsentant une catégorie de triathlon

    age max peut etre nullable car une catégorie peux etre ouverte à toute age
    sexe est représenté sous forme de booléen pas soucie d'optimisation
    """

    libelle = models.CharField(max_length=50, blank=False, null=False)
    ageMin = models.PositiveSmallIntegerField(blank=False, null=False)
    ageMax = models.PositiveSmallIntegerField()
    sexe = models.BooleanField()


class Materiel(models.Model):
    """
    Class Représentant le materiel
    """

    nom = models.CharField(max_length=50, blank=False, null=False)
    type = models.CharField(max_length=50, blank=False, null=False)
    qteTotal = models.PositiveIntegerField(blank=False, null=False)
    lieuStockage = models.CharField(max_length=50, blank=False, null=False)




    def __str__(self):
        """
        :return: String représentant l'objet Sponsor
        """
        return self.raisonSocial
