from django import forms

class IsbnForm(forms.Form):
    isbn = forms.CharField(label='isbn', max_length=100)