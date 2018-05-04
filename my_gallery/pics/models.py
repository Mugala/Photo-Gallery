from django.db import models

# Create your models here.

class Image (models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =200)
    image_location = models.CharField(max_length=50)
    image_category = models.CharField(max_length=40)

    #returns a string representation of the model, useful for when we view return queries.

    def __str__(self):
        return self.image_name
    
    #to specify model-specific options.
    class Meta:
        ordering = ['image_name']
        

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


