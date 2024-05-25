from django.db import models

# Create your models here.
#  One to one models
class Contact(models.Model):
  phone = models.CharFielld(max_length=50, unique=True)
  address = models.CharField(max_length=255)
  class Meta:
    db_table = "contact"
    
class Customer(models.Model):
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  # untuk relasi one-to-one relationship
  contact = models.OneToOneField(
    Contact, 
    related_name="customers_contact", 
    on_delete=models.CASCADE
    )
  class Meta:
    db_table = "customers"

#  Many to many models
class Compensation(models.Model):
  name = models.CharField(max_length=75)
  class Meta:
    db_table = "compensation"
    
class Employee(models.Model):
  first_name = models.CharField(max_length=35)
  last_name = models.CharField(max_length=35)
  contact = models.OneToOneField(
    Contact, 
    related_name="employee_contact", 
    on_delete=models.CASCADE
    )
  compensation = models.ManyToManyField(
    Compensation, 
    related_name="employee_compensation",
  )
  class Meta:
    db_table = "employee"