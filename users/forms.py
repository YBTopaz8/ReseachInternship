from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, Invit


class CustomUserCreationForm(UserCreationForm):
 #   username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'UserName'}))
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Password'}))
    email = forms.EmailField( required=False , widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'email'}))
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email','username',)

class InvitationForm(forms.ModelForm):
    

    class Meta:
        model = Invit
        fields = ('invCode',)
        #fields = ('')