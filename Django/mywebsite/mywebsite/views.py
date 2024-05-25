from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

def index(request):
  context = {
    'banner':'img/Banner2.jpg'
  }
  return render(request, 'index.html', context)

# template variable
def indexVar(request):
  context = {
    'judul': 'on My Website',
    'judul2': 'on My Blog',
    'kontributor' : 'Dzaka Ali',
    # template tag, liat varian lain di website django
    'nav' : [
      ['/', 'Home'],
      ['/blog', 'Blog'],
      ['/about', 'About'],
      ['/contact', 'Contact']
    ],
    # variable img
    'banner':'img/Background1.jpg'
  }
  return render(request, 'index.html', context)

# method view
def home(request):
  judul = "<h1> Ini Adalah Home </h1>"
  subjudul = "<h2> Selamat datang di website ini </h2>"
  
  output = judul  + subjudul
  return HttpResponse(output)

def about(request):
    return HttpResponse("About Me")
  
#  Class Based View
from django.views import View

class IndexClassView(View):
  template_name = "classview.html"
  context = {}
  # overide method get dari patenst class View
  def get(self, request):
    self.context['heading'] = 'GET class based view'
    return render(request, self.template_name, self.context)
  
  def post(self, request):
    self.context['heading'] = 'POST class based view'
    return render(request, self.template_name, self.context)

#  template views
from django.views.generic.base import TemplateView
# inheritance dari templateresponseMixin
# ContextMixin
# View
class IndexTemplateView(TemplateView):
  pass

class ContextTemplateView(TemplateView):
  template_name = 'templateview3.html'
  def get_context_data(self):
    context = {
      'judul': "Template dengan Context",
      'penulis' : "Ujang"
    }
    return context
  
class ParameterTemplateView(TemplateView):
  template_name = 'templateview4.html'
  
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs) #view mengetahui objek yang dimaksud yang mana
    # context = kwargs
    context['judul'] = 'Home Paramater'
    context['penulis'] = 'ujang'
    return context
  
class QueryTemplateView(TemplateView):
    template_name = 'redirectview.html'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Menambahkan parameter 'user' dari URL ke context
        context['user'] = self.kwargs.get('user')
        # Menambahkan parameter 'tipe' dari query string ke context
        tipe = self.request.GET.get('tipe')
        if tipe:
            context['tipe'] = tipe
        return context
    # return super().get_context_data(*args, **kwargs)

from django.views.generic.base import RedirectView
# RedirectView, inheritance hanya dari base view
class ArgRedirectView(RedirectView):
    pattern_name = 'queryview'
    permanent = False
    query_string = True
  
    def get_redirect_url(self, *args, **kwargs):
        user = kwargs.get('user')
        tipe = self.request.GET.get('tipe')
        if user and tipe:
            return reverse(self.pattern_name, kwargs={'user': user}) + '?tipe=' + tipe
        else:
            return super().get_redirect_url(*args, **kwargs)
          
    # template view untuk login
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
class LoginIndexView(TemplateView):
  template_name = 'index.html'
  
def loginView(request):
  context = {
    'page_title' : 'LOGIN'
  }
  # username_jack = 'JackAl'
  # password_jack = 'jack1234'
  # user = authenticate(request, username=username_jack, password=password_jack)
  # login(request, user)
  
  if request.method == 'POST':
    username_login = request.POST['username']
    password_login = request.POST['password']
    
    user = authenticate(request, username=username_login, password=password_login)
    
    if user is not None:
      login(request, user)
      return redirect('indexuser') #mengarahkan ke fungis indexVar disini
    else:
      return redirect('login')
    
  if request.method == "GET":
    if request.user.is_authenticated:
      #  logic jika user login
      return redirect('indexuser')
    else:
      #  login jika anonim
      return render(request, 'login.html', context)
  
from django.contrib.auth.decorators import login_required
#  logout
@login_required #dengna decorator maka hanya yang suda login yang bisa akses fungsinya
def logoutView(request):
  context = {
    'page_title' : 'logout'
    }
  if request.method == "POST":
    if request.POST["logout"] == 'submit':
      logout(request)
      return redirect('indexuser')
  return render(request, 'logout.html', context)

# view method dengan internal permission check
# template berubah sesuai login
def indexUser(request):
  context = {
    'judul': 'on My Website',
    'judul2': 'on My Blog',
    'kontributor' : 'Dzaka Ali',
    # template tag, liat varian lain di website django
    'nav' : [
      ['/', 'Home'],
      ['/blog', 'Blog'],
      ['/about', 'About'],
      ['/contact', 'Contact']
    ],
    # variable img
    'banner':'img/Background1.jpg'
  }
  template_name = None
  if request.user.is_authenticated:
    # jika login
    template_name = 'index_user.html'
  else:
    # jika tidak login
    template_name = 'index_anon.html'
  return render(request, template_name, context)