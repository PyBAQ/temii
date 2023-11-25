from django import forms

from .models import Talk


class NewTalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = [
            "name",
            "description",
            "level",
            "language",
            "timezone",
            "comments",
            "precense",
            "months",
        ]
