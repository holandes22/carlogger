from django.db import models


class BaseManager(models.Manager):

    def for_user(self, user):
        return self.model.objects.filter(user=user)
