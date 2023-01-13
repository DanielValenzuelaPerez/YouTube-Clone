from django import forms

from engagement.models import ContentComment


class ContentCommentForm(forms.ModelForm):
    class Meta:
        model = ContentComment
        fields = ['comment']
