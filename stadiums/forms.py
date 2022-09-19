from django import forms

from .models import Stadium

class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = "__all__"