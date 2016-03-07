from django.conf.urls import url
from django.contrib import admin
from posts import views



urlpatterns = [

	url(r'details/(?P<slug>[0-9A-Za-z-]+)', views.details, name='details'),
    url(r'create$', views.create, name='create'),
    url(r'^delete/(?P<slug>[0-9A-Za-z-]+)', views.delete, name = 'delete'),
    url(r'^register$',views.register, name='register'),

    url(r'^$', views.index, name = 'index'),

]
