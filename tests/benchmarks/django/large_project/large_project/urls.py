from django.conf.urls import patterns, url
from django.shortcuts import render

urlpatterns = []

for i in xrange(10000):
    view = lambda(request): render(request, 'template.html', {'request': request})
    urlpatterns.append(url(r'^url%08d/' % i, view))
