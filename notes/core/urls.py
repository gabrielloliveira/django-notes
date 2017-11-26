from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^add/$', views.create_note, name="create"),
]
