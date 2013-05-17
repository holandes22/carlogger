import datetime
from django.db import models

from carlogger.cars.models import Car


class Treatment(models.Model):

    BODYWORK_CAT = 1
    ELECTRIC_CAT = 2
    ENGINE_CAT = 3
    WHEELS_CAT = 4
    CHASIS_CAT = 5
    TREATMENT_CATS = (
        (BODYWORK_CAT, 'Body work'),
        (ELECTRIC_CAT, 'Electricity'),
        (ENGINE_CAT, 'Engine'),
        (WHEELS_CAT, 'Wheels'),
        (CHASIS_CAT, 'Chasis'),
    )

    BROKEN_REASON = 1
    SERVICE_REASON = 2
    AESTHETIC_REASON = 3
    NO_REASON = 4
    TREATMENT_REASONS = (
        (BROKEN_REASON, 'Failing component'),
        (SERVICE_REASON, 'Service'),
        (AESTHETIC_REASON, 'Aesthetic'),
        (NO_REASON, 'No reason'),
    )

    car = models.ForeignKey(Car)
    date = models.DateField(default=datetime.datetime.now())
    reason = models.IntegerField(choices=TREATMENT_REASONS,
                                 default=BROKEN_REASON)
    category = models.IntegerField(choices=TREATMENT_CATS,
                                   default=BODYWORK_CAT)
    description = models.TextField()
    parts_replaced = models.CharField(max_length=300, default='None',
                                      help_text='Replaced parts, comma separated')
    kilometrage = models.IntegerField()

    @models.permalink
    def get_absolute_url(self):
        return ('cars:treatments:update', (), {'pk': self.car.pk, 'treatment_pk': self.pk})

    @models.permalink
    def get_delete_absolute_url(self):
        return ('cars:treatments:delete', (), {'pk': self.car.pk, 'treatment_pk': self.pk})
