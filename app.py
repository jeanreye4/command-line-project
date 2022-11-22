from peewee import * 
db = PostgresqlDatabase('contacts_api', user='', password='', host='localhost', port=5432)

db.connect()
class BaseModel(Model):
  class Meta:
    database = db
    
class Contacts(BaseModel):
  first_name = CharField()
  last_name = CharField()
  phone_number = CharField()
  address = CharField()

  
def user_choice():
  print("enter find to find a contact, enter add a contact, edit to edit a contact")
  res = input('')
  if res == 'find':
    find_contact()
  elif res == 'add':
    add_contact()
  elif res == 'edit':
    edit_contact()
  else: 
    print(f"error try again dummy")
    user_choice()
    
def find_contact():
  search_name = input('enter first name you search for: ')
  for contact in Contacts.select():
    if search_name == contact.first_name:
        print(f"{[contact.first_name, contact.last_name, contact.address, contact.phone_number]}") 
        
def add_contact():
  print(f"enter firstname, lastname, phone_num, address")
  first_name = input(f"enter first name ")
  last_name = input(f"enter last name ")
  phone_number = input(f"enter phone_num ")
  address = input(f"enter address ")
  adding_contact = Contacts(first_name=first_name, last_name=last_name, phone_number=phone_number, address=address)
  adding_contact.save()
  print(f"contact has been added") 
  
def edit_contact():
  contact_edit = input("enter firstname of contact you want to edit: ")
  for contact in Contacts.select():
    if contact_edit == contact.first_name: 
      print(contact.first_name, contact.last_name, contact.phone_number, contact.address)
      contact.first_name = input(f"enter first name ")
      contact.last_name = input(f"enter last name ")
      contact.phone_number = input(f"enter phone_num ")
      contact.address = input(f"enter address ")
      contact.save()
      print(contact.first_name, contact.last_name, contact.phone_number, contact.address)

user_choice()