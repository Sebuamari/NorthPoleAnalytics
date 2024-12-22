from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE, IntegerField

class Kid(models.Model):
    name = CharField(max_length=10)
    niceness_coefficient = IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    gift = CharField(max_length=20)
    santas_list = ForeignKey(
        'SantasList',
        on_delete=CASCADE,
        related_name='kids'
    )

    def __str__(self):
        return self.name

class SantasList(models.Model):
    name = CharField(max_length=100)

    @property
    def nice_list(self):
        return self.kids.filter(niceness_coefficient__gte=6)

    @property
    def naughty_list(self):
        return self.kids.filter(niceness_coefficient__lt=6)

    def __str__(self):
        return self.name