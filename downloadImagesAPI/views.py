from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bs4 import BeautifulSoup
import urllib
import os
import urllib.request

# Create your views here.
@api_view(['GET'])
def downloadImages(request):
    # url = "http://www.deviantart.com/browse/all/?section=&global=1&q=dota"
    # html = urllib.request.urlopen(url).read()
    # sopa = BeautifulSoup(html, "html.parser")
    # imgs = sopa.find_all("img", _class ="")
    # count = 0
    # for img in imgs:
    #     count = count + 1
    #     image_url = img['src']
    #     urllib.request.urlretrieve(image_url, str(count) + ".jpg")
    return Response('')