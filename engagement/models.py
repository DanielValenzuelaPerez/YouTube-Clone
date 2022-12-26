from django.db import models


class Subscription(models.Model):
    account = models.ForeignKey('accounts.Account', models.CASCADE)
    creator = models.ForeignKey('accounts.Creator', models.CASCADE)
    date = models.DateField(auto_created=True)


class ContentEngagement(models.Model):
    content = models.ForeignKey('content.Content', models.CASCADE)
    account = models.ForeignKey('accounts.Account', models.CASCADE)
    liked = models.BooleanField(null=True, blank=True)


class ContentComment(models.Model):
    content = models.ForeignKey('content.Content', models.CASCADE)
    account = models.ForeignKey('accounts.Account', models.CASCADE)
    comment = models.TextField()
    reply = models.ForeignKey('engagement.ContentComment', models.CASCADE, null=True, blank=True)
