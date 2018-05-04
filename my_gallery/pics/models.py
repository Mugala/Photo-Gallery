from django.db import models

# Create your models here.

class image (models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =200)
    image_location = models.CharField(max_length=50)
    image_category = models.CharField(max_length=40)

