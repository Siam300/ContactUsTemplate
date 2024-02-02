from django import forms

class ContactFrom(forms.Form):
    name = forms.CharField(max_length= 100)
    email = forms.EmailField()
    mobile = forms.CharField()
    message = forms.CharField(widget=forms.Textarea, max_length= 500)
