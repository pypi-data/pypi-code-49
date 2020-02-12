from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from djangoldp.models import Model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import loader

class Activity(Model) :
    name = models.CharField(max_length=250,  verbose_name="Forme alternative d’activité")

    def __str__(self):
        return self.name

class Societe(Model) :
    name = models.CharField(max_length=250, verbose_name="Nom de la société")
    logo = models.ImageField(blank=True, null=True, verbose_name="Logo")
    activity = models.ForeignKey(Activity, blank=True, null=True, verbose_name="Forme alternative d’activité")
    siren = models.CharField(max_length=15, blank=True, null=True, verbose_name="Numéro de SIREN")
    address = models.CharField(max_length=250, blank=True, null=True, verbose_name="Adresse")
    postcode = models.CharField(max_length=5, blank=True, null=True, verbose_name="Code Postal")
    city = models.CharField(max_length=15, blank=True, null=True, verbose_name="Ville")
    website = models.CharField(max_length=250, blank=True, null=True, verbose_name="Site web")
    mail = models.CharField(max_length=50, blank=True, null=True, verbose_name="Adresse mail")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Numéro de téléphone")
    lat = models.CharField(max_length=25, blank=True, null=True, verbose_name="Lattitude")
    lng = models.CharField(max_length=25, blank=True, null=True, verbose_name="Longitude")
    peps = models.BooleanField(default="False", blank=True,verbose_name="PEPS")

    def __str__(self):
        return self.name