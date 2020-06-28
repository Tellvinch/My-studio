from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30,blank=True)
    
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()


class Category(models.Model):
    name = models.CharField(max_length = 30, blank=True)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =25)
    description = models.TextField
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='images')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='images')

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_name(cls, search_term):
        image = cls.objects.filter(image_name__icontains=search_term)
        return image

    @classmethod
    def filter_location(cls, location):
        # location = Location.objects.(image_location=location)
        images = cls.objects.filter(location__image_location__istartswith=location)
        return images

    @classmethod
    def filter_category(cls, category):
        images = cls.objects.filter(category__image_category__istartswith=category)
        return images