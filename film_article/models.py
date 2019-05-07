from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=255)
	def __str__(self):
		return self.title
	class Meta:
		ordering = ('title',)

class Genre(models.Model):
	title = models.CharField(max_length=255)
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	def __str__(self):
		return self.title
	class Meta:
		ordering = ('title',)

class Article(models.Model):
	title = models.CharField(max_length=500)
	original_name = models.CharField(max_length=500,default='?')
	body = models.TextField()
	rating = models.BigIntegerField()
	iframe = models.TextField()
	trailer = models.TextField(default="")
	ganre = models.ManyToManyField(Genre)
	img = models.TextField()
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	created = models.DateField(auto_now_add = True, null=True, blank=True)
	likes = models.ManyToManyField(User,blank = True)
	data = models.BigIntegerField(default=2019)
	length = models.BigIntegerField(default=0)
	actor = models.TextField(default='?')
	director =models.CharField(max_length=255,default='?')
	country = models.TextField(default='?')
	quolity = models.CharField(max_length=255,default='?')
	translation = models.CharField(max_length=255,default='?')
	def __str__(self):
		return self.title
	class Meta:
		ordering = ('title',)



class Comment(models.Model):
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	article = models.ForeignKey(Article,on_delete=models.CASCADE)
	body = models.TextField()