from django import forms

from content.models import Content, Playlist


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['video', 'name', 'description']


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name']
