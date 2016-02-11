from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from django.core import serializers
from collections import OrderedDict
from urllib import urlencode
import requests

from .models import Artist, Album
def index(request):
	return HttpResponse("Hello world!")
		
def albums(request, artistId = None):
	if request.method == "GET":
		artists = []
		if artistId is not None:
			if Artist.objects.filter(id=artistId).exists():
				artists = [Artist.objects.get(id=artistId)]
			else:
				return HttpResponseNotFound()
		if len(artists) == 0:
			artists = Artist.objects.all()
		result = []
		for artist in artists:
			albums = [album.as_dict() for album in artist.album_set.all()]
			artist_dict = OrderedDict()
			artist_dict["name"] = artist.name
			artist_dict["albums"] = albums
			result.append(artist_dict)
		return JsonResponse(result, safe=False)
	return JsonResponse({})

def artists(request):
	if request.method == "GET":
		artists = Artist.objects.all()
		result = [{"name" : artist.name, "artistId" : artist.id} for artist in artists]
		return JsonResponse({"artists" : result})
		
	if request.method == "PUT":
		artist_name = request.body
		#check if artist already exists
		if(Artist.objects.filter(name=artist_name).exists()):
			return JsonResponse({"success": True, "status" : "Artist already added"})

		#request list of albums for this artist from iTunes search API
		r = requests.get("https://itunes.apple.com/search", {"media" : "music", "entity" : "album", "attribute" : "artistTerm", "term" : artist_name, "limit" : 200});
		response_json = r.json()
		if(response_json["resultCount"] == 0):
			#No albums for this artist :(
			return HttpResponseNotFound()
		
		#Add artist entry to db
		artist = Artist.objects.create(name=artist_name)
		#Add all the albums to the db as well
		for result in response_json["results"]:
			#Add album entry to db
			album = Album.objects.create(artist=artist, actualArtist=result["artistName"], name=result["collectionName"], date_released=result["releaseDate"], image=result["artworkUrl100"])
		return JsonResponse({"success": True, "status" : "All albums added"})
	#todo: add delete artist method
	return JsonResponse({})