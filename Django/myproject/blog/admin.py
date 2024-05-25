from django.contrib import admin

# Register your models here.
from .models import Artikel

# class ArtikelAdmin(admin.ModelAdmin):
#   def get_readonly_fields(self, request, obj=None):
#     current_user = request.user
#     # Jika obj adalah None, cek permission tanpa mengakses is_published
#     if obj is None:
#       # membuat if jika user punya permission untuk publis_artikel (editor)
#       if current_user.has_perm("blog.publish_artikel"):
#         readonly_fields = [
#           'created',
#           'updated',
#           'published',
#           'slug',
#         ]
#         return readonly_fields
#       # ini jika user memiliki permission add_artikel (penulis)
#       elif current_user.has_perm("blog.add_artikel"):
#         # jika oleh editor telah di publish maka yang dikembalikan bukan form melaikan hanya data dari fields saja
#         if obj.is_published:
#           # print([data.name for data in self.model._meta.fields])
#           return [data.name for data in self.model._meta.fields]
#         # ini jika belum di publish, masih bisa di edit dengan batasan yang hanya readonly
#         else:
#           readonly_fields = [
#             'created',
#             'updated',
#             'is_published',
#             'published',
#             'slug',
#           ]
#           return readonly_fields
#     # Jika obj tidak None, cek apakah artikel telah dipublikasikan
#     elif obj.is_published:
#       return [field.name for field in self.model._meta.fields]
#     # Jika artikel belum dipublikasikan, kembalikan readonly_fields
#     else:
#       readonly_fields = [
#           'created',
#           'updated',
#           'is_published',
#           'published',
#           'slug',
#         ]
#       return readonly_fields

class ArtikelAdmin(admin.ModelAdmin):
  def get_readonly_fields(self, request, obj=None):
    current_user = request.user
    readonly_fields = [
      'created',
      'updated',
      'published',
      'slug',
    ]
    # Jika obj tidak None dan telah dipublikasikan, kembalikan semua field sebagai readonly
    if obj and obj.is_published:
      return [field.name for field in self.model._meta.fields]
    # Jika obj adalah None atau belum dipublikasikan, cek permission
    else:
      if current_user.has_perm("blog.publish_artikel"):
        return readonly_fields
      elif current_user.has_perm("blog.add_artikel"):
        return readonly_fields + ['is_published']
      else:
        # Jika user tidak memiliki permission apapun, kembalikan readonly_fields
        return readonly_fields
      
admin.site.register(Artikel, ArtikelAdmin)