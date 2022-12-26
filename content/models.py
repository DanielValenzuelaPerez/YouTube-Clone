from django.db import models


class Content(models.Model):
    video = models.CharField(max_length=255)
    creator = models.ForeignKey('accounts.Creator', models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    publish_date = models.DateField(auto_now_add=True)


class Playlist(models.Model):
    user = models.ForeignKey('accounts.Account', models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True)


class PlaylistContent(models.Model):
    playlist = models.ForeignKey('content.Playlist', models.CASCADE)
    content = models.ForeignKey('content.Content', models.CASCADE)
