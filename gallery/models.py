from django.db import models



class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Images(models.Model):
    image_path = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def save_images(self):
        self.save()


    @classmethod
    def search_by_category(cls, search_term):
        image = cls.objects.filter(category__name__icontains=search_term)
        return image

    def __str__(self):
        return self.description

    class Meta:
        ordering=["-pub_date"]