from django.db import models


class Content(models.Model):
    video = models.CharField(max_length=255)
    creator = models.ForeignKey('Creator', models.CASCADE)
    views = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    publish_date = models.DateField(auto_created=True)


class Playlist(models.Model):
    user = models.ForeignKey('Account', models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    creation_date = models.DateField(auto_created=True)


class PlaylistContent(models.Model):
    playlist = models.ForeignKey('Playlist', models.CASCADE)
    content = models.ForeignKey('Content', models.CASCADE)
