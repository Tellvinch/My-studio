def index(request):
    images = Images.objects.all()
    location = Location.objects.all()
    context = {
        "images":images,
        "location":location,
    }
    return render(request, 'index.html', context)

def images(request, images_id):
    try:
        images = Images.objects.get(id = images_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"gall/gallery.html", {"images":images})

def search_image(request):
    if 'images' in request.GET and request.GET['images']:
        search_term = request.GET["images"]
        searched_images = Images.search_by_category(search_term)
        message = f'{search_term}'
        location = Location.objects.all()
        context = {
            "location":location,
            "message":message,
            "images":searched_images
        }
        return render(request, 'gall/search.html',context)

    else:
        message = "You haven't searched for any image"
        return render(request, 'gall/search.html', {"message":message})

def display_by_location(request, id):
    location = Location.objects.all()
    images = Images.objects.filter(location__id=id)
    context = {
        "location":location,
        "images":images,
    }
    return render(request, "location.html", context)