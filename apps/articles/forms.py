from django import forms 

class Add_article(forms.Form):
    art_title = forms.CharField(max_length=255)
