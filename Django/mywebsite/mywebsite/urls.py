"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views
from blog import views as blogViews
# mengimport indexClassView untuk class views
from .views import index, IndexClassView, IndexTemplateView, ContextTemplateView, ParameterTemplateView, ArgRedirectView, QueryTemplateView, loginView, logoutView
from django.views.generic.base import TemplateView, RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    
    # login dan logout
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('indexuser/', views.indexUser, name='indexuser'),
    
    # template variable
    path('indexvar/', views.indexVar, name='indexVar'),
    # url class view
    path('classview/', IndexClassView.as_view(), name='classview'),
    # path('classview/', IndexClassView.as_view(template_name='classview.html'), name='classview'), #jika template_name mau langsung dideklarasikan
    
    #  url template class view
    path('templateview/', IndexTemplateView.as_view(template_name="templateview.html"), name='templateview'),
    path('templateview2/', TemplateView.as_view(template_name='templateview2.html'), name='template_view2'), #untuk halaman yag statis
    path('templateview3/', ContextTemplateView.as_view(), name='template_view3'), #jika template view bisa diubah isinya
    path('templateview4/<int:parameter>', ParameterTemplateView.as_view(), name='templteview4'), #jika menggunakan parameter
    
    # url redirect view
    path('redirectview/', RedirectView.as_view(url='/'), name='redirectview'),
    path('redirectview2/', RedirectView.as_view(pattern_name='index'), name='redirectview2'),
    # path('redirectview3/<str:user>/', ArgRedirectView.as_view(), name='redirectview3'), #dengan parameter
    path('redirectview3/<str:user>/', QueryTemplateView.as_view(), name='queryview'), #dengan query parameter
    # path('<str:user>/', TemplateView.as_view(template_name='redirectview.html'), name='arguments'),
    
    
    # path('blog/', blogViews.blog, name='blog'),
    # kita buat url blog yang lebih rapih dibawah menggunakan include sehingga tidak perlu banyak alias
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    path('sosmed/', include(('sosmed.urls', 'sosmed'), namespace='sosmed')),
    path('artikel/', include(('artikel.urls', 'artikel'), namespace='artikel')),
]
