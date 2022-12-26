from django.db import models


class Account(models.Model):
    handle = models.CharField(max_length=20, unique=True)


class Creator(models.Model):
    account = models.OneToOneField('Account', models.CASCADE)
