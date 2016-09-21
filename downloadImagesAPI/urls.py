from django.conf.urls import url,patterns
from django.contrib import admin

urlpatterns = patterns(
    'downloadImagesAPI.views',
    url(r'^downloadImages/$', 'downloadImages', name='downloadImages'),
    url(r'^downloadImagesUrl/$', 'downloadImagesUrl', name='downloadImagesUrl'),
)