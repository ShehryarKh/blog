from django import forms
from .models import Post
from django.forms import Textarea, CheckboxInput,CharField


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields =[
		"title",
		"content",

		]
class UpdatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields =[
		"title",
		"content",

		]

		widgets={
			
			"content": Textarea(),

		}