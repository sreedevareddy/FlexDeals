from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic.base import RedirectView

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.home_view, name='links'),
    path('search/',views.scraping,name='hme'),
    path('entertainment/',views.entertainment,name='entertainment'),
    path('clothing/',views.clothing,name='clothing'),
    path('electronics/',views.electronics,name='electronics'),
    path('appliances/',views.appliances,name='appliances'),
    path('beauty/',views.beauty,name='beauty'),
]
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)