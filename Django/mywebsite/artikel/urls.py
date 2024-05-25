from django.urls import path
from .views import artikelIndexView, artikelHomeView, artikelAddView, artikelAddView2

urlpatterns = [
  path("", artikelIndexView, name='index'),
  path("home/", artikelHomeView, name='home'),
  path("add/", artikelAddView, name='add'),
  path("add2/", artikelAddView2, name='add2'),
]