from django import forms
from .models import Post,UserProfile
from django.forms import Textarea, CheckboxInput,CharField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class UserForm(UserCreationForm):
	class Meta:
		model= User
		fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
	class Meta:
		model =UserProfile
		fields=('website','profile_img')
		

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields =[
		"title",
		"content",

		]

		widgets={

			"content": Textarea(),

		}