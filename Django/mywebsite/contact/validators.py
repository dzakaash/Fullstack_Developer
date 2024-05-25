from django.core.exceptions import ValidationError

def validate_judul(value):
  from .models import PostModel
  judul_input = value
  judul_in_model = PostModel.objects.filter(judul=judul_input)
  if judul_in_model:
    raise ValidationError('Judul sudah ada')