from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('health', views.health,  name='health'),
    url(r'^detail/(?P<id>\d+)/$', views.detail, name='detail')
]
