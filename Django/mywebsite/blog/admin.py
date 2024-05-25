from django.contrib import admin

# Register your models here.
# from . import models #jika semuanya
from .models import Post #jika Post saja
# admin.site.register(models.Post);

#untuk tetap menampilkan slug di tambah postingan, namun tidak editable
class PostAdmin(admin.ModelAdmin):
  readonly_fields = ['slug']
  
admin.site.register(Post, PostAdmin);

from .models import Artikel
class ArtikelAdmin(admin.ModelAdmin):
  readonly_fields = ['slug', 'publish', 'update']
admin.site.register(Artikel, ArtikelAdmin);