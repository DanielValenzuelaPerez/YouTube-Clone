from django.db import models


class Subscription(models.Model):
    account = models.ForeignKey('Account', models.CASCADE)
    creator = models.ForeignKey('Creator', models.CASCADE)
    date = models.DateField(auto_created=True)


class ContentEngagement(models.Model):
    content = models.ForeignKey('Content', models.CASCADE)
    account = models.ForeignKey('Account', models.CASCADE)
    liked = models.BooleanField(null=True, blank=True)


class ContentComment(models.Model):
    content = models.ForeignKey('Content', models.CASCADE)
    account = models.ForeignKey('Account', models.CASCADE)
    comment = models.TextField()
    reply = models.ForeignKey('ContentComment', models.CASCADE, null=True, blank=True)
