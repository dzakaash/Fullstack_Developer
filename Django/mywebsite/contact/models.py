from django.db import models

from .validators import validate_judul

# Create your models here., jangan lupa di import di admin
class PostModel(models.Model):
  judul = models.CharField(max_length = 20, validators=[validate_judul])
  body = models.TextField()
  category = models.CharField(max_length =20)
  
  published = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return "{}. {}".format(self.id, self.judul)