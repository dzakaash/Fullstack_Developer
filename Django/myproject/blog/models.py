from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Artikel(models.Model):
  judul   = models.CharField(max_length=255)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  isi = models.TextField()
  is_published = models.BooleanField(null=True, blank=True, default=False) #saat makemigrations pilih 1 dan isi timezone.now
  published = models.DateTimeField(null=True)
  slug = models.SlugField(blank=True, editable=False)
  
  # mengatur default permissions yang bisa dilakukan pada model, pada defaultnya terdiri dari 'add', 'change', dan 'delete'
  class Meta:
    default_permissions = ('add', 'change', 'delete')
    permissions = (
      ('publish_artikel', 'can publish artikel'),
      ('edit_artikel', 'can edit artikel'),
    )
  
  def save(self):
    # membuat isi atribut slug
    self.slug = slugify(self.judul)
    
    # membuat waktu pada atribut published
    if self.is_published == True:
      self.published = timezone.now()
    else:
      self.published = None
    
    super().save()
    
  def __str__(self):
    return "{}. {}".format(self.id, self.judul)
  
  