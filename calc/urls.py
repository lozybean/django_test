from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$', views.add, name='add'),
    url(r'^add/(\d+)/(\d+)', views.add2, name='add2'),
]
