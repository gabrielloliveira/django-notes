from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^add/$', views.create_note, name="create"),
    url(r'^edit/(?P<id>\d+)/$', views.edit_note, name="edit"),
    url(r'^delete/(?P<id>\d+)/$', views.delete_note, name="delete"),
]
