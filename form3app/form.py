from django import forms
from form3app.models import Cost


class CostForm(forms.Form):
	date = forms.DateField()
	cost = forms.FloatField()