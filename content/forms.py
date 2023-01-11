from django import forms

from content.models import Content


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['video', 'name', 'description']
