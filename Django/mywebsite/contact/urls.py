from django.urls import path
from . import views

from . import views
urlpatterns = [
  path('', views.index, name='index'),
  path('post/', views.post, name='post'),
  path('create/', views.postForm, name= 'create')
]