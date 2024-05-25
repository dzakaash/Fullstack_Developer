from django import forms

class ContactForm(forms.Form):
  nama = forms.CharField(max_length=20)
  GENDER = (
    ('P', 'pria'),
    ('W', 'wanita')
  )
  jenis_kelamin = forms.ChoiceField(
                        widget=forms.RadioSelect,
                        choices=GENDER)
  email = forms.EmailField(label='Alamat Email')
  TAHUN = range(1945, 2019, 1)
  tanggal_lahir = forms.DateField(
                        widget = forms.SelectDateWidget(years=TAHUN)
  )
  alamat = forms.CharField(
                  widget = forms.Textarea,
                  max_length = 200,
                  required=False)
  kode_pos = forms.IntegerField(required=False)
  kota = forms.CharField(required=False)
  provinsi = forms.CharField(required=False)
  agree = forms.BooleanField()

## Post Form
from .models import PostModel

# class PostForm(forms.Form):
#   judul = forms.CharField(max_length = 20)
#   body = forms.CharField(
#     widget = forms.Textarea
#   )
#   category = forms.CharField()
## menggunakan Model Form
class PostForm(forms.ModelForm):
  class Meta:
    model = PostModel
    fields = ['judul', 'body', 'category']
  
  ## cleaning field judul, jika tidak menggunakan model form dan validtors.py
  # def clean_judul(self):
  #   judul_input = self.cleaned_data.get('judul')
  #   judul_in_model = PostModel.objects.filter(judul=judul_input)
  #   if judul_in_model:
  #     raise forms.ValidationError('Judul sudah ada')
  #   return judul_input

# Tipe data form
class TypeForm(forms.Form):
  #  python data type
  integer_field = forms.IntegerField(required=False)
  decimal_field = forms.DecimalField(required=False)
  float_field = forms.FloatField(required=False)
  boolean_field = forms.BooleanField(required=False)
  null_boolean_field = forms.NullBooleanField() #boolean yang boleh null
  char_field = forms.CharField(max_length=10, required=False)
  #  String Input
  email_field = forms.EmailField(required=False)
  regex_field = forms.RegexField(regex=r'(P?<test>)')
  slug_field = forms.SlugField()
  url_field = forms.URLField(required=False)
  ip_field = forms.GenericIPAddressField()
  # Select Input
  PILIHAN = (
    ('nilai1', 'Pilihan1'),
    ('nilai2', 'Pilihan2'),
    ('nilai3', 'Pilihan3'),
  )
  choice_field = forms.ChoiceField(choices=PILIHAN)
  multi_choice_field = forms.MultipleChoiceField(choices=PILIHAN)
  multi_type_choice = forms.TypedMultipleChoiceField(choices=PILIHAN)
  # date time
  date_field = forms.DateField()
  datetime_field = forms.DateTimeField()
  duration_field = forms.DurationField()
  time_field = forms.TimeField()
  splitdatetime_field = forms.SplitDateTimeField()
  # file input
  file_field = forms.FileField()
  image_field = forms.ImageField()
  