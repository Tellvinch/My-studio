from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url('^$',views.index,name = 'index'),
    url(r'^image/(\d+)', views. Image, name ='image'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(?P<location>.*)', views.get_location, name='location'),
    url(r'^category/(?P<category>.*)', views.get_category, name='category')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)