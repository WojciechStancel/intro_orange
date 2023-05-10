from django.db import models

# Create your models here.


# ONE-TO-ONE RELATION
class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)


class Capital(models.Model):
    name = models.CharField(max_length=100)


# ONE-TO-MANY RELATION
class Language(models.Model):
    name = models.CharField(max_length=100)


class Framework(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)


# MANY-TO-MANY

class Actor(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField('Actor')
