from django.db import models

class Dojo(models.Model):
	# id = models.IntegerField()
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	desc = models.TextField(default="a dojo")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# ninjas = related_name field, a list of ninjas associated with a given dojo

class Ninja(models.Model):
	# id = models.IntegerField()
	dojo = models.ForeignKey(Dojo, related_name='ninjas', on_delete=models.CASCADE)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)