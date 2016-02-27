from django.conf.urls import url
from django.contrib import admin
from posts import views



urlpatterns = [

	url(r'details/(?P<id>[0-9]+)', views.details, name='details'),
    url(r'create$', views.create, name='create'),
    url(r'^delete/(?P<id>[0-9]+)', views.delete, name = 'delete'),

    url(r'^$', views.index, name = 'index'),

]
