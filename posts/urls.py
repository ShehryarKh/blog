from django.conf.urls import url
from django.contrib import admin
from posts import views



urlpatterns = [

	url(r'details/(?P<slug>[0-9A-Za-z-]+)', views.details.as_view(), name='details'),
    url(r'create$', views.create.as_view(), name='create'),
    url(r'^delete/(?P<slug>[0-9A-Za-z-]+)', views.delete.as_view(), name='delete'),
    url(r'^register$',views.register.as_view(), name='register'),
    url(r'^$',views.index.as_view(), name = 'index'),

]
