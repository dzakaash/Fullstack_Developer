from django.shortcuts import render
from .models import Customer, Contact, Compensation, Employee

# Create your views here.
#  One to One input
def createCustomer():
  print("start 1 ======")
  cont = Contact(
    phone = "0812345678",
    address = "Jl. raya Saung Bandrek"
  )
  cont.save()
  
  print("start 2 ======")
  cost = Customer(
    firstname = "John",
    lastname = "Wilson",
    contact = cont
  )
  cost.save()
  print("sukses ======")
  
class Command(BaseCommand):
  help = ""
  def handle(self, *args, **options):
    print("== start table loan")
    createCustomer()
    print("== end table loan")
  
#  Many to many input
def create_compensation_employee():
  comp = Compensation(
    name = "Bonus Tahunan"
  )
  comp.save()
  
  emp = Employee(
    first_name = "Hann",
    last_name = "Boy",
    contact_id = 1,
  )
  emp.save()
  
  emp.compensation.add(comp)
  emp.save()
  
class Command2(BaseCommand):
  help = ""
  def handle(self, *args, **options):
    print("== start table loan")
    create_compensation_employee()
    print("== end table loan")