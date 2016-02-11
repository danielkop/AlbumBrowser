from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^albums/$', views.albums),
	url(r'^artists/$', views.artists),
	url(r'^artists/(?P<artistId>[0-9]+)/albums/$', views.albums)
]
