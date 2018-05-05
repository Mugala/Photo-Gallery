from django.db import models
import datetime as dt

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()



class Areas (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def save_area(self):
        self.save()


class Image (models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =200)
    image_location = models.ForeignKey(Areas)
    image_category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'my-photos/', null=True)

    #returns a string representation of the model, useful for when we view return queries.

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    # def get_image_by_id(self):
    #     self.objects.get(id)


    #to specify model-specific options.
    class Meta:
        ordering = ['image_name']   

    @classmethod
    def todays_pics(cls):
        today = dt.date.today()
        pics = cls.objects.filter(pub_date__date = today)
        return pics

    @classmethod
    def days_pics(cls,date):
        pics = cls.objects.filter(pub_date__date = date)
        return pics

    @classmethod
    def search_by_category(cls,search_term):
        pics = cls.objects.filter(image_category__name__icontains=search_term,image_location__name__icontains=search_term)
        return pics

    @classmethod
    def search_by_category(cls,search_term):
        pics = cls.objects.filter(image_location__name__icontains=search_term)
        return pics

