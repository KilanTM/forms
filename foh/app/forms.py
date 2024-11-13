from django import forms

class HeyName(forms.Form):
    name = forms.CharField( max_length=40)