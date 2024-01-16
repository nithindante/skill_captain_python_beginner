class Person:
  def __init__(self,age,name) :
      self.age=age
      self.name=name

try:
  first_person_name =  str(input("Enter the name of the first person:"))
  first_person_age = int(input("Enter the age"))
  second_person_name =  str(input("Enter the name of the second person:"))
  second_person_age = int(input("Enter the age"))
except:
  print("Please enter a valid age/name")
else:
  Alice = Person(first_person_age,first_person_name)
  Bob = Person(second_person_age,second_person_name)

  print(Alice.name)
  print(Alice.age)
  print(Bob.name)
  print(Bob.age)