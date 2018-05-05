from django.test import TestCase
from .models import Image,Areas,Category

# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.img1 = Image(image_name = 'The moon', image_description = 'Blue in color', image_location = Areas(id), image_category = Category(id), pub_date = '2018-05-04' )

    def test_instance(self):
        self.assertTrue(isinstance(self.img1,Image))

    def test_get_pics_today(self):
        today_pics = Image.todays_pics()
        self.assertTrue(len(today_pics)>0)

    def test_get_pics_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        pics_by_date = Image.days_pics(date)
        self.assertTrue(len(pics_by_date) == 0)

# class AreasTestClass(TestCase):

#     def setUp(self):
#         # Creating a new editor and saving it
#         self.area1= Areas(name = 'sky')
#         self.area1.save_area()

# class CategoryTestClass(TestCase):

#     def setUp(self):
#         # Creating a new editor and saving it
#         self.category= Category(name = 'Heavenly body')
#         self.category.save_category()     



#          # Testing Save Method
#     def test_save_method(self):
#         self.img1.save_image()
#         images = Image.objects.all()
#         self.assertTrue(len(images) > 0)


#         # Creating a new tag and saving it
#         self.new_category = Category(name = 'testing')
#         self.new_category.save()

#         self.new_areas= Areas(name = 'Moringa',post = 'This is a random test Post',editor = self.james)
#         self.new_article.save()

#         self.new_article.tags.add(self.new_tag)

#     def tearDown(self):
#         Image.objects.all().delete()
#         Areas.objects.all().delete()
#         Category.objects.all().delete()
    


# first create a test for Areas and then create a test for category and then use the self.area and self.category to test for image,,,
    #  def test_save_method(self):
    #     self.james.save_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) > 0)

# class ArticleTestClass(TestCase):

#     def setUp(self):
#         # Creating a new editor and saving it
#         self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
#         self.james.save_editor()

#         # Creating a new tag and saving it
#         self.new_tag = tags(name = 'testing')
#         self.new_tag.save()

#         self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
#         self.new_article.save()

#         self.new_article.tags.add(self.new_tag)

#     def tearDown(self):
#         Image.objects.all().delete()
#         Category.objects.all().delete()
#         Areas.objects.all().delete()
