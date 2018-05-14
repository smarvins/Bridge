from django import forms
from .import models


class newpost(forms.ModelForm):
    class Meta:
        model = models.app
        fields = ['thumb','body']
