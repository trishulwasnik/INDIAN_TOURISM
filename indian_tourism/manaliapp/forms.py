from django import forms


class manali_form(forms.Form):
    DURATION = forms.CharField(max_length=100)
    HOTELS = forms.CharField(max_length=100)
    BUDGET = forms.IntegerField()
    CITIES = forms.CharField(max_length=100)