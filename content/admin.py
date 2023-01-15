from django.contrib import admin

from content.models import Content, Playlist, PlaylistContent

admin.site.register(Content)
admin.site.register(Playlist)
admin.site.register(PlaylistContent)
