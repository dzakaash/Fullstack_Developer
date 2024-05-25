from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Post(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField()
  category = models.CharField(max_length=255, null=True)
  waktuPosting = models.DateTimeField(auto_now_add = True)
  slug = models.SlugField(blank=True, editable=False)
  
  def save(self):
    self.slug = slugify(self.title)
    super(Post, self).save()
  
  def __str__(self):
    return "{}. {}".format(self.id, self.title)
  
class Artikel(models.Model):
  judul = models.CharField(max_length=225)
  isi = models.TextField()
  penulis = models.CharField(max_length=255)
  publish= models.DateTimeField(auto_now_add=True)
  update = models.DateTimeField(auto_now=True)
  slug = models.SlugField(blank=True, editable=False)
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.judul)
    super().save(*args, **kwargs)
    
  def get_absolute_url(self):
    return reverse('blog:listview') 
  #ini bisa diganti dengan url slug
  # url_slug = {
    # 'slug': self.slug,
  # }
  # return reverse('blog:detail', kwargs=url_slug)
  
  def __str__(self):
    return "{}. {}".format(self.id, self.judul)