from django.shortcuts import render

# Create your views here.

# import form
from .forms import ContactForm

def index(request):
  contact_form = ContactForm()
  context = {
    'heading' : 'Contact Page',
    'contact_form' : contact_form,
  }
  print(request.POST) #cek yang dikirim ke form
  
  if request.method == 'POST':
    context['nama'] = request.POST['nama']
    context['alamat'] = request.POST['alamat']
  return render(request, 'contact/index.html', context)

from .forms import PostForm
from .models import PostModel
from django.http import HttpResponseRedirect
def post(request):
  posts = PostModel.objects.all()
  context = {
    'page_title' : 'List Post',
    'posts' : posts,
  }
  return render(request, 'contact/post.html', context)

def postForm(request):
  post_form = PostForm(request.POST or None)
  
  if request.method == 'POST':
    if post_form.is_valid():
      # PostModel.objects.create(
      #   # judul = request.POST.get('judul'),
      #   # body = request.POST.get('body'),
      #   # category = request.POST.get('category')
      #   ### agar data yang diambil sudah divalidasi
      #   judul = post_form.cleaned_data.get('judul'),
      #   body = post_form.cleaned_data.get('body'),
      #   category = post_form.cleaned_data.get('category')
      # )
      post_form.save() # langsung membuat object baru di model dari form untuk setiap field yang diinput
      return HttpResponseRedirect("/contact/post")
    # else:
    #   error = post_form.errors
    
  context = {
    'page_title': 'Create Post',
    'post_form': post_form,
    # 'error' : error,
  }
  return render(request, 'contact/postform.html', context)