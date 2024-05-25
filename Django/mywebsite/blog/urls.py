from django.urls import path
from . import views

from django.views.generic import ListView, DetailView, FormView
from .models import Artikel
from .views import ArtikelListView, ArtikelDetailView, ArtikelFormView, ArtikelCreateView1, ArtikelCreateView2, ArtikelUpdateView, ArtikelUpdateView2, ArtikelDeleteView
from .formview import ArtikelForm

urlpatterns = [
  path('', views.blog),
  path('recent/', views.recent),
  path('home/', views.home),
  path('index/', views.index),
  path('jurnal/', views.jurnal, name="jurnal"),
  path('berita/', views.berita, name="berita"),
  path('gosip/', views.gosip, name="gosip"),
  path('blogs/', views.blogs),
  path('form/', views.form, name="form"),
  
  # list view
  path('listindex/', views.listindex, name='listindex'),
  path('listview/', ListView.as_view(model=Artikel), name='listview'),
  # path('listview/', ArtikelListView.as_view(), name='listview'),
  path('listview/<page>', ArtikelListView.as_view(), name='listview'),
  path('listview/<penulis>/<page>', ArtikelListView.as_view(), name='listview'),
  path('detailview/<slug:slug>/', ArtikelDetailView.as_view(), name='detailview'),
  
  # Form View
  # path('formcreate/', FormView.as_view(form_class=ArtikelForm, template_name='blog/formview.html'), name='formcreate'),
  path('formcreate/', ArtikelFormView.as_view(), name='formcreate'),
  
  # Create View
  path('create/', ArtikelCreateView1.as_view(), name='create'),
  path('createform/', ArtikelCreateView2.as_view(), name='createform'),
  
  # update view
  path('update/<int:pk>/', ArtikelUpdateView.as_view(), name='update'),
  path('updateform/<int:pk>/', ArtikelUpdateView2.as_view(), name='updateform'),
  
  # delete view
  path('deleteform/<int:pk>/', ArtikelDeleteView.as_view(), name='delete'),
  
  # parameter
  path('<int:input>/', views.angka, name='page'), #menggunakan parameter
  # path('<str:category>/', views.categoryPost),
  path('post/<slug:slugInput>', views.singlePost), #menggunakan Slug
]