from django.db import models
from django.db.models import CharField
from django.forms import IntegerField

class Toy(models.Model):
    name = CharField(max_length=20)
    toy_type = CharField(max_length=20)
    quantity = IntegerField()

    def __str__(self):
        return self.name

class Coal(models.Model):
    name = "Coal"

    def __str__(self):
        return self.name