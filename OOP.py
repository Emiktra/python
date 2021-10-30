import os
os.system('cls' if os.name=='nt' else 'clear')

class Human:
  name="isabelle"
  age=45
  height=188


Alex = Human()
Johnny = Human()


print(Alex.height)

Alex.job = "Front-End Dev"
print(Alex.job)

Human.job = "Developer"
print(Alex.job)
print("Johnny Job:",Johnny.job)


# Class attributes and instance attributes

Alex.name = "Helo there"
Johnny.name= "Darkamuna"
print(f"Johnny name: {Johnny.name}")



# Self Keyword
class Person:
  name = "Donah"
  age=51

  def test(self): #we have to add self because this argument is always provided
    print("test")
  
  def getDetails(self):
    print("name: ", self.name, "\nage: ", self.age, "\nlocation: ",self.location)

  def setDetails(self, name, age, location):
    self.name = name
    self.age = age
    self.location = location

person1 = Person()
person1.test()
Person.test(person1)

print("")
person1.setDetails("Alexa", 344, "Turgiye")
person1.getDetails()
print("")


class PersonII:
  name = "Donah"
  age=51

  def test(self): #we have to add self because this argument is always provided
    print("test")
  
  def getDetails(self):
    print("name: ", self.name, "\nage: ", self.age, "\nlocation: ",self.location)

  def setDetails(self, name, age, location):
    self.name = name
    self.age = age
    self.location = location

  @staticmethod
  def salute():
    print("Hi There! ", PersonII.name)


PersonII.salute()
person1 = PersonII()
person1.setDetails("Danial", 12, "Denizli")
person1.salute()



#Special Methods
class SpecialPerson:
  company = "Clarusway"

  def __init__(self, name, age): #constructor basically
    self.name = name
    self.age = age

  def __str__(self):
    return f"\nName: {self.name} \nAge: {self.age}" 
    #function gets called when we print person1

  def __len__(self):
    return self.age


person1 = SpecialPerson("Barry", 32) 

randomList = [1,2,3]
print(randomList)
print(person1)
print("")

print(len(person1))       #same thing
print(person1.__len__())  #same thing
#when we call len() on this class, it returns __len__

print("")
#abstraction and encapsulation
randomList = [3,2,5,6,3,4,6,1,3,2,6,7,3,5,8,9,6,7,8,9]
print(randomList)
randomList.sort()
print(randomList)
print("")


class NewPerson:
  company = "Clarusway"

  def __init__(self, name, age):
    self.name = name
    self.age = age
    self._id = 5000 #the underscode in front of id tells ppl to not change code
    self.__id2 = 2300 # double underscore makes it harder for people to change it

  def __str__(self):
    return f"Name. {self.name}\nAge: {self.age}"

person1 = NewPerson("Annah", 22)
print(person1._NewPerson__id2)
person1._NewPerson__id2 = 4000
print(person1._NewPerson__id2)


#Inheritance and polymorphism
class DopePerson:
  company = "Clarusway"

  def __init__(self, name, age):
    self.name = name
    self.age = age
    self._id = 5000 #the underscode in front of id tells ppl to not change code
    self.__id2 = 2300 # double underscore makes it harder for people to change it

  def __str__(self):
    return f"Name: {self.name}\nAge: {self.age}"

  def details(self):
    print(f"Name: {self.name}    Age: {self.age}")


class Lang:
  def __init__(self) -> None:
      self.path = path

class Employees(DopePerson, Lang):
  def __init__(self, name, age, path):
    super().__init__(name, age)
    self.path = path

  def __str__(self):
    return f"Name: {self.name}\nAge: {self.age}"

  def details(self):
    super().details()
    print(f"Path: {self.path}")
    # print(f"Name: {self.name}    Age: {self.age}      Path: {self.path}")


emp1 = Employees("Barry", 23, "Back-End")
print("")
print(emp1)
emp1.details()
print("")
print(Employees.mro())


class Customer:
  def __init__(self, name,age):
    self.name= name
    self.age= age
    self.__id = 1423534
    self.movements =[]
  
  def __str__(self):
    return f"Name: {self.name}    Id: {self.__id}"

  def add_movements(self, amount, date, explain):
    self.movements.append({"amount": amount, "date": date, "explain": explain})

  def all_movements(self):
    for i in self.movements:
      print(i["date"], i["amount"], i["explain"])
  
  def balance(self):
    return sum(i["amount"] for i in self.movements)
    # total = 0
    # for i in self.movements:
    #   total += i["amount"]
    # print(total)

print("")
customer1 = Customer("Bunny", 22)
print(customer1)
customer1.add_movements(5534, "23.5.2014", "salary")
customer1.add_movements(-1243, "25.5.2014", "rent")
customer1.add_movements(-720, "04.6.2014", "bent")
customer1.add_movements(-2314, "11.6.2014", "credit_card")
