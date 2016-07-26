from django.conf.urls import url

from . import views
from .forms import UserForm, UserProfileForm

urlpatterns = [
    url(r'^new-user/$', views.register, name='new_user'),
]
