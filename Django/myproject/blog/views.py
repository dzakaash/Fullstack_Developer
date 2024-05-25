from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.
# @permission_required('blog.add_artikel') #ini adalah dekorator untuk memfilter berdasarkan permission yang dimiliki user
@permission_required('blog.add_artikel', login_url='/admin/') #jika user tidak memiliki permission maka otomatis akan diarahkan ke laman login admin
# @permission_required('blog.edit_artikel', login_url='None', raise_exception=True) #jika user tidak memiliki permission maka akan dikembalikankode kesalahan
def addView(request):
  context = {
    'page_title': 'Add Artikel',
  }
  return render(request, 'blog/add.html', context)

def indexView(request):
  context = {
    'page_title': 'Blog',
  }
  return render(request, 'blog/index.html', context)

@permission_required('blog.edit_artikel', login_url='/admin/') 
def updateView(request):
  context = {
    'page_title': 'Edit Artikel',
  }
  return render(request, 'blog/edit.html', context)
