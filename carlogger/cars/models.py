import datetime
from django.db import models
from django.contrib.auth.models import User

from carlogger.core.models import BaseManager

YEAR_CHOICES = [(year, str(year)) for year in
                xrange(1920, datetime.datetime.now().year + 1)]


class CarManager(BaseManager):
    pass


class Car(models.Model):

    GEARBOX_MANUAL = 1
    GEARBOX_AUTOMATIC = 2
    GEARBOX_CHOICES = (
        (GEARBOX_MANUAL, 'Manual'),
        (GEARBOX_AUTOMATIC, 'Automatic'),
    )

    objects = CarManager()
    user = models.ForeignKey(User)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    gearbox = models.IntegerField(choices=GEARBOX_CHOICES,
                                  default=GEARBOX_AUTOMATIC)
    year = models.IntegerField(choices=YEAR_CHOICES,
                               default=str(datetime.datetime.now().year))

    def is_automatic(self):
        return self.gearbox == 2

    def get_name(self):
        return '{} {} {}'.format(self.brand, self.model, self.year)

    def __unicode__(self):
        return self.get_name()

    @models.permalink
    def get_absolute_url(self):
        return ('cars:detail', (), {'pk': self.pk})

    @models.permalink
    def get_treatments_absolute_url(self):
        return ('cars:treatments:list', (), {'pk': self.pk})

