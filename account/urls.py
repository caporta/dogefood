from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^pet/update/(?P<pk>\d+)$', views.pet_form, name='pet_form'),
    url(r'^pet/delete/(?P<pk>\d+)$', views.delete_pet, name='delete_pet'),
]
