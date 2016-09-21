from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bs4 import BeautifulSoup
import urllib
import os
import urllib.request
import re
import requests

# Create your views here.
@api_view(['GET'])
def downloadImages(request):
    url = "http://www.deviantart.com/browse/all/?section=&global=1&q=dota&offset="
    c = 0
    count = 0
    while (c < 101):
        html = urllib.request.urlopen(url+str(c)).read()
        sopa = BeautifulSoup(html, "html.parser")
        for img in sopa.find_all("img", class_ =""):
            if img.find(src = re.compile("/avatars")):
                continue
            elif img['src'] == "http://a.deviantart.net/avatars/default.gif":
                continue
            try:
                count = count + 1
                image_url = img['src']
                urllib.request.urlretrieve(image_url, str(count) + ".jpg")
            except:
                pass
        #Controlling offset
        #In the case of Danbooru, I'll have to control only the page number
        c = c + 25
    return Response('')

@api_view(['GET'])
def downloadImagesUrl(request):
    urls = []
    count = 0
    url = str(request.GET.get('url'))
    # url = url.replace("section=", "section=0")
    html = urllib.request.urlopen(url).read()
    sopa = BeautifulSoup(html, "html.parser")
    for img in sopa.find_all("img", class_ =""):
        if img.find(src = re.compile("/avatars")):
            continue
        elif img['src'] == "http://a.deviantart.net/avatars/default.gif":
            continue
        try:
            count = count + 1
            image_url = img['src']
            urllib.request.urlretrieve(image_url, str(count) + ".jpg")
            urls.append(img['src'])
        except:
            pass
    return Response(url)