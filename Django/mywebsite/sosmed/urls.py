from django.urls import path
from . import views

urlpatterns = [
  path('list/', views.list, name='list'),
  path('create/', views.create, name='create'),
  path('delete/<int:delete_id>', views.delete, name='delete'),
  path('update/<int:update_id>', views.update, name='update')
]
