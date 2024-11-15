from django import forms

class HeyName(forms.Form):
    name = forms.CharField( max_length=40)

class AgeForm(forms.Form):
    end = forms.IntegerField()
    birthyear = forms.IntegerField()

class OrderForm(forms.Form):
    burgers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()
