from django.conf.urls import url

from . import views
from .forms import UserForm, UserProfileForm

urlpatterns = [
    url(r'^new-user/$', views.register_user, name='new_user'),
    url(r'^new-pet/$', views.register_pet, name='new_pet'),
]
