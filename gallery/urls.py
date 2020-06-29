from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^images/(\d+)', views.images, name = 'images'),
    url(r'^search/', views.search_image, name = 'search_image'),
    url(r'^locations/(\d+)', views.display_by_location, name = 'display_by_location'),
    # url(r'^category/(?P<category>.*)', views.get_category, name='category')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)