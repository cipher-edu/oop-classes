# Objects
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"
class Dog:

	attr1 = "mammal"
	def __init__(self, name):
		self.name = name


Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

#Inheritance 
class Person(object):

	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
	
# child class
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post
		Person.__init__(self, name, idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
		print("Post: {}".format(self.post))


a = Employee('Rahul', 886012, 200000, "Intern")

a.display()
a.details()

#Polymorphism
class Bird:

	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("Most of the birds can fly but some cannot.")

class sparrow(Bird):

	def flight(self):
		print("Sparrows can fly.")

class ostrich(Bird):

	def flight(self):
		print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

#Encapsulation
class Base:
	def __init__(self):
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
	def __init__(self):

		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)

obj1 = Base()
print(obj1.a)

