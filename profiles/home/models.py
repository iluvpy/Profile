from django.contrib.admin.sites import AdminSite
from django.db import models
from django.contrib import admin
from django.utils.timezone import now as time_now



class Profile(models.Model):
	name = models.CharField(max_length=30)
	creation_date = models.DateTimeField(default=time_now, editable=False)
	image_token = models.CharField(max_length=30, default='none')


admin.site.register(Profile)