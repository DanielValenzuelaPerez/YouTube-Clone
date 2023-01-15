from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Subscription(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    creator = models.ForeignKey('accounts.Creator', models.CASCADE)
    date = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('user', 'creator')


class ContentEngagement(models.Model):
    content = models.ForeignKey('content.Content', models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    liked = models.BooleanField(null=True, blank=True)
    
    class Meta:
        unique_together = ('content', 'user')


class ContentComment(models.Model):
    content = models.ForeignKey('content.Content', models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    comment = models.TextField()
    reply_to = models.ForeignKey('engagement.ContentComment', models.CASCADE, null=True, blank=True)
    date_time = models.DateField(auto_now=True)

    def get_replies(self):
        replies = ContentComment.objects.filter(reply_to=self.pk)
        return replies
