from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='list'),
    url(r'(?P<pk>\d+)/$', views.product_detail, name='detail'),
]
