# # Python Classes and Objects
# A class is a user-defined blueprint or prototype from which objects are created.
# Classes provide a means of bundling data and functionality together.
# Creating a new class creates a new type of object, allowing new instances of that type to be made.
# Each class instance can have attributes attached to it for maintaining its state.
# Class instances can also have methods (defined by their class) for modifying their state.
# # class object
# an object is a instance of object of a class. a class like a blue print while an instance  is a copy  of the  class with  actual values.
# .select :it is  represted by the attributes  of an object .it is aslo reflects the properties of an object .
# .behaviour: it is resprestented  by the methods  of an objects. it is also  reflects the response  of an  object to other objects.
# .identiy:it gives a unique name to  an objects and enables one objects to interct with other objects.
class Dog:
    attr1= "mammal"
    attr2= "Dog"
    def fun(self):
        print("I'm a",self.attr1)
        print("I'm a",self.attr2)
Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()
# Class and Instance Variables
class Dog:
    animal = 'dog'

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color


Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed:', Rodger.breed)
print('color:', Rodger.color)
print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed:', Buzo.breed)
print('color:', Buzo.color)
print("\nAccessing  class variable  using class name ")
print(Dog.animal)
# opps in python


class Computer:
    def __init__(self):
        print("in init")

    def config(self):
        print("i5,16gb,1TB")


com1 = Computer()
com2 = Computer()
Computer.config(com1)
Computer.config(com2)
com1.config()
com2.config()
print("")

class Person:
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print('Hello ,my name is',self.name)
p = Person('ashish')
p.say_hi()
print("")

class Dog:
    animal='dog'
    def __init__(self,breed):
        self.breed=breed
    def setcolor(self, color):
        self.color=color
    def getcolor(self):
        return self.color
Rodger = Dog("pug")
Rodger.setcolor("white")
print(Rodger.getcolor())
print("")




# Constructors in Python
# def __init__(self):
#     # body of the constructor
class ashish:
    def __init__(self):
        self.ash="ashish"
    def print_ash(self):
        print(self.ash)
obj=ashish()
obj.print_ash()
print("")

class sum:
    first=0
    second=0
    answer=0
    def __init__(self,f,s):
        self.first=f
        self.second=s
    def display(self):
        print("First number="+str(self.first))
        print("second number=" + str(self.second))
        print("Adddition of two number ="+str(self.answer))
    def calculator(self):
        self.answer=self.first +self.second

obj = sum(1000,2000)
obj.calculator()
obj.display()
print("")

# Destructors in Python

# def __del__(self):
#   # body of destructor
class Employee:
    def __init__(self):
        print('Employee created.')
    def __del__(self):
        print('Destructor called,employee deleted.')
obj= Employee()
del obj
print("")



class A:
    def __init__(self,bb):
        self.b=bb
class B:
    def __init__(self):
        self.a= A(self)
    def __del__(self):
        print("die")
def fun():
    b =B()
fun()
print("")
# Inheritance in Python
# It represents real-world relationships well.
# Inheritance offers a simple, understandable model structure.
# Less development and maintenance expenses result from an inheritance.
# Class BaseClass:
#     {Body}
# Class DerivedClass(BaseClass):
#     {Body}
# parent class


class person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(self.name, self.id)

emp = person("ashish",102)
emp.display()
print("")
# child class


class emp(person):

    def print(self):
        print("emp class called")
emp_details = emp("ashish",103)

emp_details.display()
emp_details.print()
print("")

# Inheritance in Python
class person(object):
    def __init__(self, name):
        self.name = name
    def getname(self):
        return self.name
    def isEmployee(self):
        return False
class Employee(person):
    def isEmployee(self):
        return True
emp =  person("ashish1")
print(emp.getname(), emp.isEmployee())
emp = person("ashish2")
print(emp.getname(), emp.isEmployee())
print("")
# sub class
class person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
# chlid class



class Employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idnumber)
a=Employee('ashish',34475868,242454557,"intern")
a.display()




# multiple imheritances




class base1(object):
    def __init__(self):
        self.str1="ashish1"
        print("Base1")

class base2(object):
    def __init__(self):
        self.str2="ashish2"
        print("base2")

class Derived(base1,base2):
    def __init__(self):
        base1.__init__(self)
        base2.__init__(self)
        print("Derived")
    def printStrs(self):
        print(self.str1,self.str2)
ob=Derived()
ob.printStrs()
print("")

# Types of Inheritance in Python
# Single Inheritance:Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.
class parent:
    def func1(self):
        print("this function is in a parent class.")
class Child(parent):
    def func2(self):
        print("this function is in a child class.")
object = Child()
object.func1()
object.func2()
print("")


# Multiple Inheritance:
# When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class.




class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)
class Father:
    fathername=""
    def father(self):
        print(self.fathername)
class son(Mother,Father):
     def parents(self):
         print("Father:",self.fathername)
         print("Mother:",self.mothername)
s1=son()
s1.fathername=""
s1.mothernam=""
s1.parents()
print("")
