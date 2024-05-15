from django import forms

class PersonInfoForm(forms.Form):
    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    role = forms.CharField(max_length=50)