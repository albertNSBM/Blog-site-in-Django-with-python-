from django import forms

class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=25,widget=forms.TextInput)
    email=forms.EmailField()
    to=forms.EmailField()
    comment=forms.CharField(required=False,widget=forms.Textarea)