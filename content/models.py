from django.conf import settings
from django.db import models

from engagement.models import ContentEngagement

User = settings.AUTH_USER_MODEL

class Content(models.Model):
    video = models.CharField(max_length=255)
    creator = models.ForeignKey('accounts.Creator', models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    publish_date = models.DateField(auto_now=True)

    def get_likes_dislikes_count(self):
        engagement = ContentEngagement.objects.filter(content=self.pk)
        liked = engagement.filter(liked=True).count()
        dislikes = engagement.filter(liked=False).count()
        return liked, dislikes


class Playlist(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    creation_date = models.DateField(auto_now=True)


class PlaylistContent(models.Model):
    playlist = models.ForeignKey('content.Playlist', models.CASCADE)
    content = models.ForeignKey('content.Content', models.CASCADE)
