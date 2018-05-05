from django.test import TestCase
from .models import Image,Areas,Category

# Create your tests here.

#First Test
class ImageTestClass(TestCase):
    def setUp(self):
        self.img1 = Image(image_name = 'The moon', image_description = 'Blue in color', image_location = Areas(id), image_category = Category(id), pub_date = '2018-05-04' )

    def test_instance(self):
        self.assertTrue(isinstance(self.img1,Image))

         # Testing Save Method
    def test_save_method(self):
        self.img1.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    



    #  def test_save_method(self):
    #     self.james.save_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) > 0)
