from django.db import models
from django.utils import timezone

from django.utils.text import slugify


# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 50)
	content = models.TextField()
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()
	slug = models.SlugField(max_length=50)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		self.updated_at = timezone.now()
		if not self.id:
			self.created_at = timezone.now()
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title