from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=1000)
	image = models.ImageField(upload_to='posts/')
	author = models.ForeignKey(User, related_name= 'post_author', on_delete=models.CASCADE)
	
	
	
	def __str__(self):
		return self.title