from django.contrib import admin

from carlogger.cars.models import Car
from carlogger.treatments.models import Treatment


admin.site.register(Car)
admin.site.register(Treatment)

