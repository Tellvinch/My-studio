from django.test import TestCase
from .models import Images, Location,Category

class LocationTest(TestCase):
    def setUp(self):
        self.location = Location(name = 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(name = 'Food')

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

class ImageTest(TestCase):

    def setUp(self):
        self.location = Location(name= 'Nairobi')
        self.location.save()
        self.category = Category(name = 'name')
        self.category.save()
        self.image = Images(image_path = 'images/1.jpeg', name = 'Tellvinch', description = 'dance accepts everyone', location = self.location, category = self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Images))

    def test_save(self):
        self.image.save_images()
        image = Images.objects.all()
        self.assertTrue(len(image) > 0)