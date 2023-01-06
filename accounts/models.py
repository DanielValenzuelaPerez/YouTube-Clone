from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Creator(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
