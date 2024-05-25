from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
  return render(request, 'blog.html')

def home(request):
  return render(request, 'blog/blog.html')

def recent(request):
  return HttpResponse('<h1> Ini ada Recent saja </h2>')

# dengan mysql
from .models import Post
def index(request):
  postingan = Post.objects.all() #ngambil dari database
  context = {
    'Title': 'Blog',
    'Heading': 'Blog dengan MySQL',
    'Post' : postingan,
  }
  return render(request, 'blog/index.html', context)

def jurnal(request):
  postingan = Post.objects.filter(category='jurnal') #ngambil dari database
  context = {
    'Title': 'Blog',
    'Heading': 'Blog Jurnal dengan MySQL',
    'Post' : postingan,
  }
  return render(request, 'blog/index.html', context)

def berita(request):
  postingan = Post.objects.filter(category='berita') #ngambil dari database
  context = {
    'Title': 'Blog',
    'Heading': 'Blog Berita dengan MySQL',
    'Post' : postingan,
  }
  return render(request, 'blog/index.html', context)

def gosip(request):
  postingan = Post.objects.filter(category='gosip') #ngambil dari database
  context = {
    'Title': 'Blog',
    'Heading': 'Blog Gosip dengan MySQL',
    'Post' : postingan,
  }
  return render(request, 'blog/index.html', context)

# Menggunakan Paramter
def angka(request, input):
  return HttpResponse(f'<h1> Ini adalah Page {input}</h2>')

# #jika input lebih dari satu
# def angka(request, **input):
#   #input akan berupa dictionary
#   return HttpResponse(f'<h1> Ini adalah Page {input}</h2>')

def categoryPost(request, category):
  posts = Post.objects.filter(category=category)
  
  return HttpResponse("Category Post")

def singlePost(request, slugInput):
  post = Post.objects.get(slug=slugInput)
  
  title = "<h1>{}</h1>".format(post.title)
  body = "<p>{}</p>".format(post.body)
  category = "<p>{}</p>".format(post.category)
  
  return HttpResponse(title + body + category)

def blogs(request):
  context = {
    'Title': 'Blogs Page',
    'Contents' : 'Ini adalah page dari Blogs',
  }
  return render(request, 'blog/blogs.html', context)

def form(request):
  context={
    'heading' : 'Form Page' 
  }
  if request.method == 'POST':
    nama = request.POST['nama']
    alamat = request.POST['alamat']
    print(nama + " " + alamat)
  else:
    print("Ini adalah method get")
  return render(request, 'blog/form.html', context)

def listindex(request):
  context = {
    'page_title':'List Index View',
  }
  return render(request, 'blog/listindex.html', context)

from django.views.generic import ListView
from .models import Artikel

class ArtikelListView(ListView):
  model = Artikel
  ordering = ['update']
  paginate_by = 1
  extra_context = {
    'page_title': 'List Index View',
  }
  def get_queryset(self):
    if self.kwargs['penulis'] != 'all':
      self.queryset = self.model.objects.filter(penulis__iexact = self.kwargs['penulis'])
      self.kwargs.update({
        'penulis': self.kwargs['penulis'],
      })
    return super().get_queryset()
    
  def get_context_data(self, *args, **kwargs):
    self.kwargs.update(self.extra_context)
    kwargs = self.kwargs
    print(kwargs)
    return super().get_context_data(*args, **kwargs)
  pass

from django.views.generic.detail import DetailView

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = 'blog/artikel_detail.html'  # Pastikan ini sesuai dengan nama file template Anda
    context_object_name = 'artikel'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    extra_context = {
      'page_title' : 'Detail Artikel',
    }
    
    def get_context_data(self, *args, **kwargs):
      self.kwargs.update(self.extra_context)
      
      artikel_lain = self.model.objects.exclude(slug=self.kwargs['slug'])
      self.kwargs.update({'artikel_lain': artikel_lain})
      
      kwargs = self.kwargs
      print(kwargs)
      return super().get_context_data(*args, **kwargs)
    
from django.views.generic import FormView    
from .formview import ArtikelForm
from django.urls import reverse, reverse_lazy

class ArtikelFormView(FormView):
  form_class = ArtikelForm
  template_name = 'blog/formview.html'
  success_url = reverse_lazy('blog:listview')
  extra_context = {
    'page_title' : 'Tambah Artikel',
  }
  def get_context_data(self, *args, **kwargs):
    kwargs.update(self.extra_context)
    return super().get_context_data(*args, **kwargs)
  def form_valid(self, form):
    #print(from.cleaned_data)
    form.save()
    return super().form_valid(form)

# create view
from django.views.generic import CreateView
class ArtikelCreateView1(CreateView):
  form_class = ArtikelForm
  template_name = 'blog/formview.html'
  extra_context = {
    'page_title' : 'Tambah Artikel dengan Create View',
    }
  def get_context_data(self, *args, **kwargs):
    kwargs.update(self.extra_context)
    return super().get_context_data(*args, **kwargs)
  
class ArtikelCreateView2(CreateView): 
  # langsung mengambil modelnya
  # template akan diambil dari artikel_form, atau yang memiliki sufix "_form"
  model = Artikel
  fields = {
    'judul',
    'isi',
    'penulis',
  }
  extra_context = {
    'page_title' : 'Tambah Artikel dengan Create View',
  }
  def get_context_data(self, *args, **kwargs):
    kwargs.update(self.extra_context)
    return super().get_context_data(*args, **kwargs)
  
# update
from django.views.generic import UpdateView
class ArtikelUpdateView(UpdateView):
  form_class = ArtikelForm
  model = Artikel
  template_name = 'blog/formview.html'
  extra_context = {
    'page_title' : 'Update Artikel dengan Update View 1',
  }
  def get_context_data(self, *args, **kwargs):
    kwargs.update(self.extra_context)
    return super().get_context_data(*args, **kwargs)
  
class ArtikelUpdateView2(UpdateView):
  model = Artikel
  fields = [
    'isi'
  ]
  extra_context = {
    'page_title' : 'Update Artikel dengan Update View 2',
  }
  def get_context_data(self, *args, **kwargs):
    kwargs.update(self.extra_context)
    return super().get_context_data(*args, **kwargs)

#  Delete View
from django.views.generic import DeleteView
class ArtikelDeleteView(DeleteView):
  model = Artikel
  template_name = 'blog/confirm_delete.html'
  success_url = reverse_lazy('blog:listview')