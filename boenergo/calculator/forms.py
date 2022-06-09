from django import forms


class QuadraticForm(forms.Form):
    a = forms.IntegerField(required=False)
    b = forms.IntegerField(required=False)
    c = forms.IntegerField(required=False)


class ColorsForm(forms.Form):
    int = forms.IntegerField(required=False)