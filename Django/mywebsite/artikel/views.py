from django.shortcuts import render
from django.contrib.auth.models import Group

# Create your views here.
# internal check
def artikelIndexView(request):
  context = {
    'page_title' : 'Artikel',
  }
  test_group = Group.objects.get(name='penulis')
  user_group = request.user.groups.all()
  
  template_name = None
  if test_group in user_group:
    # jika user merupakan anggota dari group
    template_name = "artikel/index_penulis.html"
  else:
    # jika user bukan merupakan anggota dari group
    template_name = "artikel/index_pembaca.html"
  return render(request, template_name, context)

def artikelHomeView(request):
  context = {
    'page_title' : 'Home Artikel',
  }
  return render(request, "artikel/home.html", context)

from django.contrib.auth.decorators import user_passes_test
# decorator check
def checkGroupPenulis(user):
  test_group = Group.objects.get(name='penulis')
  user_group = user.groups.all()
  status = test_group in user_group
  return status

@user_passes_test(checkGroupPenulis)
def artikelAddView(request):
  context = {
    'page_title' : 'Tambah Artikel View'
  }
  return render(request, 'artikel/artikel_add.html', context)

# simple decorator check
@user_passes_test(lambda user: Group.objects.get(name='penulis') in user.groupd.all())
def artikelAddView2(request):
  context = {
    'page_title' : 'Tambah Artikel View'
  }
  return render(request, 'artikel/artikel_add.html', context)