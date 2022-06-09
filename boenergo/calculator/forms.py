from django import forms
from django.core.exceptions import ValidationError

class QuadraticForm(forms.Form):
    a = forms.FloatField()
    b = forms.FloatField()
    c = forms.FloatField()


class ColorsForm(forms.Form):
    var = forms.IntegerField(min_value=1, max_value=100)