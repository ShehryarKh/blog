from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 50)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title