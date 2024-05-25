from django.urls import path
from .views import addView, indexView, updateView

urlpatterns = [
  path('add/', addView, name='add'),
  path('', indexView, name='index'),
  path('update/', updateView, name='update'),
]