from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    
    class Meta:
        model=User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )

class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields =  (
            'username',
            'first_name',
            'last_name',
            'email'
        )

class AddContenuForm(forms.ModelForm):
	
	class Meta:
	 model= Contenu
	 exclude = ['user']
