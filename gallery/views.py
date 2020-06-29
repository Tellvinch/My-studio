from django.shortcuts import render
from .models import Images

# Create your views here.

def index(request):
    images = Image.get_images()
    a = images[0::4]
    b = images[1::4]
    c = images[2::4]
    d = images[3::4]
    return render(request, 'index.html',locals())


def image(request,image_id):
    image = Image.objects.get(id=image_id)
    return render (request, 'image.html', {"image":image})


def search_results(request):

   if 'image' in request.GET and request.GET["image"]:
       search_term = request.GET.get("image")
       searched_images = Image.search_by_name(search_term)
       a = searched_images[0::4]
       b = searched_images[1::4]
       c = searched_images[2::4]
       d = searched_images[3::4]
       message = f"{search_term}"

       return render(request, 'search.html',{"message":message,"searched_images": searched_images}, locals())

   else:
       message = "You haven't searched for any term"
       return render(request, 'search.html',{"message":message})

def get_location(request,location):
   images = Image.filter_location(location)
   return render(request,'location.html',locals())

def get_category(request,category):
   image = Image.filter_category(category)
   return render(request,'category.html',locals())