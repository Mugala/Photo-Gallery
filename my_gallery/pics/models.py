from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Areas (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Image (models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =200)
    image_location = models.ForeignKey(Areas)
    image_category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)

    #returns a string representation of the model, useful for when we view return queries.

    def __str__(self):
        return self.image_name
    
    #to specify model-specific options.
    class Meta:
        ordering = ['image_name']