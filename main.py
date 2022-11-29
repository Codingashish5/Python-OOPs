import re
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import ChainMap
from collections import namedtuple
from collections import deque
from collections import UserList
from collections import UserDict
from collections import UserString
from collections import Counter
from collections import UserDict
from collections import UserList
from collections import UserString
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
"""
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
s1.mothername=""
s1.parents()
print("")




# Multilevel Inheritance :
# In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather.
class Dad:
    basketball=1
class Son(Dad):
    football=1
    def  isfootball(self):
        return f"yes i play football{self.football} no of times"
class Grandson(Son):
    football=6
    def isfootball(self):
        return f"yes i play football very aesome {self.football} no of times"
darry=Dad()
harry=Son()
cherry=Grandson()
# print(harry.isfootball())
print(harry.basketball)



# Hierarchical Inheritance:
# When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.
class Employee:
    no_of_leaves=8
    var=8
    def __init__(self,aname,asalary,arole):
        self.name= aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"the name is {self.name}.Salary is {self.salary}and role is {self.role}"
    def change_leaves (cls,newleaves):
        cls.no_of_leaves=newleaves
    def from_dash(cls,string):
        return cls (*string.split("-"))
    def printgood(string):
        print("this is good "+string )
class Player:
    var=9
    no_of_games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printdetails(self):
        return f"the name is {self.name}.game is {self.game}"
class Coolprogramer(Player,Employee):
    language ="C++"
    def printlanguage(self):
        print(self.language)
harry=Employee("Harry",255,"teacher")
rohan=Employee("Rohan",455,"student")
Rahul=Player("Rahul",["footballer"])
karan=Coolprogramer("Karan",["Cricket"])
print(karan.var)
print("")

# Hybrid Inheritance:
# Inheritance consisting of multiple types of inheritance is called hybrid inheritance.
class School:
    def func1(self):
        print("this is a function in school.")
class Student1(School):
    def func2(self):
        print("this function is in a student 1.")
class Student2(School):
    def func3(self):
        print("this function is in a student 2.")
class Student3(Student1,School):
    def func4(self):
        print("this function is in a student 3.")
object =Student3()
object.func1()
object.func2()
print("")

# Encapsulation in Python
# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.
# Protected members
class Base:
    def __init__(self):
        self._a=2
class Derived(Base):
        def __init__(self):
            Base.__init__(self)
            print("calling  protected member  of base class:",self._a)
            self._a=3
            print("calling modified protected member outside class:",self._a)
obj1 = Derived()
obj2 = Base()
print("accessing protected member of obj1:",obj1._a)
print("accessing protected member of obj2:",obj2._a)
print("")


# Private members
class Base:
    def __init__(self):
        self.a="ashish"
        self.c="mundra"
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("calling private member of base class:")
        print(self.__c)
obj1 =Base()
print(obj1.a)
print("")

# Polymorphism in Python
# The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.
print(len("ashish"))
print(len([10,20,30]))
print("")
def add(x,y,z=0):
    return x+  y+z
print(add(2,3))
print(add(2,3,5))
print("")


# Polymorphism with class methods:

class India():
    def capital(self):
        print("new delhi is the capital of india .")
    def language(self):
        print("hindi is the most widely spoken language of india .")
    def type(self):
        print("india is a developing country.")
class USA():
    def capital(self):
        print("washington,D.C is the capital of USA.")
    def language(self):
        print("English is the primary language of USA.")
    def type(self):
        print("USA is a developed country.")
obj_ind=India()
obj_usa=USA()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()
print("")


# Polymorphism with Inheritance:
class Bird:
    def intro(self):
        print("there are many types of birds .")
    def flight(self):
        print("most of the birds can fly but some cannot.")
class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly..")
class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly..")
obj_bird=Bird()
obj_spr=Sparrow()
obj_ost=Ostrich()
obj_bird.intro()
obj_bird.flight()
obj_spr.intro()
obj_spr.flight()
obj_ost.intro()
obj_ost.flight()
print("")

print("example2")

class India():
    def capital(self):
        print("New delhi  is the capital of india :")
    def language(self):
        print("hindi is the most widely sopken language  of india .")
    def type(self):
        print("india is a developing country.")
class USA():
    def capital(self):
        print("Washington ,D.C. is the capital of USA.")
    def langauge(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is a developed country.")
def fun(obj):
    obj.capital()
    obj.language()
    obj.type()
obj_ind=India()
obj_usa=USA()
fun(obj_ind)
fun(obj_usa)
"""
# Class or Static Variables in Python
"""
class Csstudent:
    stream='cse'
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll


a=Csstudent('ashish',1)
b=Csstudent('rohan',2)
print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)
print(Csstudent.stream)
a.stream='ece'
print(a.stream)
print(b.stream)
Csstudent.stream='mech'
print(a.stream)
print(b.stream)
print("")
      # Python Exception Handling
# Try and Except Statement – Catching Exceptions
a=[1,2,3]
try:
    print("Second element =%d"%(a[1]))
    print("Fourth element =%d"%(a[3]))
except:
    print("An error occurred")

# try with else clause
def AbyB(a,b):
    try:
        c= ((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
AbyB(2.0,3.0)
AbyB(3.0,3.0)"""
# Finally keyword in python
"""
try:
    k=5//0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print('this is always executed')
print("")"""
# try except in python
# def divide(x,y):
#     try:
#         result=x//y
#         print("Yeah! your answer is :",result)
#     except ZeroDivisionError:
#         print("Sorry! you are dividing by zero")
# divide(3,2)
# print("")

# except
# def divide(a,b):
#     try:
#         result=a//b
#         print("Yeah! your answer is :",result)
#     except ZeroDivisionError:
#         print("Sorry! you are dividing by zero")
# divide(3,3)
# print("")
# Error Handling
# Handling Exceptions with Try/Except/Finally
# We can handle errors by the Try/Except/Finally method. we write unsafe code in the try, fall back code in except and final code in finally block.
"""
try:
    print("code start")
    print(1/0)
except:
    print("an error occur")
finally:
    print("ASHISH")
print("")
print("EXAMPLE 2")
try:
    amount=1999
    if amount<2999:
        raise ValueError("please add money in your account")
    else:
        print("you are eligible to purchase Dsa self placed course")
except ValueError as e:
       print(e)"""
# try and execpt in python
# print("Enter num 1")
# num1=input()
# print("Enter num 2")
# num2=input()
# try:
#     print("The sum of these two number is",int (num1)+int(num2))
# except Exception as e:
#     print(e)
# print("This line is very important ")
# print("")
# python file IO Basics
"""
"r"-open file for reading 
"w"-open a file for writing 
"x"-creates files if  not exists
"a"-add more content to a file
"t"- text mode
"b"-binary mode
"+"-read and write

"""

# file1 = open("C://Users//Dell//Desktop//myfile.txt")
# print(file1.read())
# file1.close()
# # reading a file
# file1=open ("C://Users//Dell//Desktop//my my.txt","w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# file1.write("Hello\n")
# file1.writelines(L)
# file1.close()
# file1=open ("C://Users//Dell//Desktop//my my.txt","r+")
# print("output of read function is ")
# print(file1.read())
# print()
# file1.seek(0)
# print("output of readline function is ")
# print(file1.read())
# print()
# file1.seek(0)
#
# print("Output of Read(9) function is ")
# print(file1.read(9))
# print()
#
# file1.seek(0)
#
# print("Output of Readline(9) function is ")
# print(file1.readline(9))
# print()
#
# file1.seek(0)
#
# # readlines function
# print("Output of Readlines function is ")
# print(file1.readlines())
# print()
# file1.close()
# print("")
#
# # append
# file1=open("C://Users//Dell//Desktop//files.txt","w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London"]
# file1.writelines(L)
# file1.close()
# # Append-adds at last
# file1 = open("C://Users//Dell//Desktop//files.txt", "a")  # append mode
# file1.write("Today \n")
# file1.close()
#
# file1 = open("C://Users//Dell//Desktop//files.txt", "r")
# print("Output of Readlines after appending")
# print(file1.read())
# print()
# file1.close()
#
# # Write-Overwrites
# file1 = open("C://Users//Dell//Desktop//files.txt", "w")  # write mode
# file1.write("Tomorrow \n")
# file1.close()
#
# file1 = open("C://Users//Dell//Desktop//files.txt", "r")
# print("Output of Readlines after writing")
# print(file1.read())
# print()
# file1.close()
# print("")


# append from new line
# file1 = open("C://Users//Dell//Desktop//python.txt", "w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London"]
# file1.writelines(L)
# file1.close()
# # Append-adds at last
# # append mode
# file1 = open("C://Users//Dell//Desktop//python.txt", "a")
#
# # writing newline character
# file1.write("\n")
# file1.write("Today")
# # without newline character
# file1.write("Tomorrow")
# file1 = open("C://Users//Dell//Desktop//python.txt", "r")
# print("Output of Readlines after appending")
# print(file1.read())
# print()
# file1.close()
# print("")
# Regular Expression in Python


# s = 'GeeksforGeeks: A computer science portal for geeks'
#
# match = re.search(r'portal', s)
#
# print('Start Index:', match.start())
# print('End Index:', match.end())
# print("")

# re.findall()
# Return all non-overlapping matches of pattern in string, as a list of strings. The string is scanned left-to-right, and matches are returned in the order found.
# string='hello my number is 1234567890 and my friend number is 987654321'
# regex='/d+'
# match=re.findall(regex,string)
# print(match)
# print("")

# p = re.compile('[a-e]')
# print(p.findall("abcde"))

# Regular Expressions in Python

# regex = r"([a-zA-Z]+)(\d+)"
# match=re.search(regex,"I was born om june 24")
# if match  != None:
#     print("Match at index %s,%s"%(match.start(),match.end()))
#     print("Full match:%s"%(match.group(0)))
#     print("Month: %s" % (match.group(1)))
#     print ("Day: %s" % (match.group(2)))
# else:
#     print("The regex pattern does not match.")



# python collections

# python collection module
#   Counters
#   OrderedDict
#   DefaultDict
#   ChainMap
#   Namedtuple
#   DeQue
#   UserDict
#   Userlist
#   Userstring


#         Counters
# A counter is a sub-class of the dictionary. It is used to keep the count of the elements in an iterable in the form of an unordered dictionary where the key represents the element in the iterable and value represents the count of that element in the iterable.
# print(Counter(['B','B','A','B','C','A','B','B','A','B']))
# print(Counter({'A':3,'B':5,'C':2}))
# print(Counter(A=3, B=5, C=2))
# print("")
#
#
#       # orderedDict
# # An OrderedDict is also a sub-class of dictionary but unlike dictionary, it remembers the order in which the keys were inserted.
# # class collections.OrderDict()
#
# print("This is  a Dict:\n")
# d = {}
# d['a']=1
# d['b']=2
# d['c']=3
# d['d']=4
# for key,value in d.items():
#     print(key,value)
# print("This is an Ordered Dict:\n")
# od=OrderedDict()
# od['a']=1
# od['b']=2
# od['c']=3
# od['d']=4
# for key,value in od.items():
#     print(key,value)
# print("")
#
# print("example 2")
# od=OrderedDict()
# od['a']=1
# od['b']=2
# od['c']=3
# od['d']=4
# print('Before Deleting')
# for key,value in od.items():
#     print(key,value)
# od.pop('a')
# od['a']=1
# print('\nafter re-inserting')
# for key,value in od.items():
#     print(key,value)
# print("")

        # DefaultDict
# A DefaultDict is also a sub-class to dictionary. It is used to provide some default values for the key that does not exist and never raises a KeyError.
d=defaultdict(int)
# l=[1,2,3,4,6,4,6,7,5,4]
# for i in l:
#     d[i]+=1
# print(d)
# print("")
#
# # ChainMap
# # A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.
# # class collections.ChainMap(dict1, dict2)
# d1={'a':1,'b':2}
# d2 = {'c':3,'d':4}
# d3={'e':5,'f':6}
# c=ChainMap(d1,d2,d3)
# print(c)
# print("")


# NamedTuple
# A NamedTuple returns a tuple object with names for each position which the ordinary tuples lack.
# class collections.namedtuple(typename, field_names)
# Student=namedtuple('Student',['name','age','DOB'])
# S=Student('ashish','20','05-02-2001')
# print("the student age using index is :",end="")
# print(S[1])
# print("The student name  using keyname is: ",end="")
# print(S.name)
# print("the student DOB using keyname is :",end="")
# print(S.DOB)

# Deque
# Deque (Doubly Ended Queue) is the optimized list for quicker append and pop operations from both sides of the container. It provides O(1) time complexity for append and pop operations as compared to list with O(n) time complexity.
# class collections.deque(list)
# queue =deque(['name','age','DOB'])
# print(deque)
# print("")
#
# # INSERTING ELEMENT
# de=deque([1,2,3])
# de.append(4)
# print("this is after appending at right is :")
# print(de)
# de.appendleft(6)
# print("this is after appending at left is :")
# print(de)
# print("")
#
# # removing element
# de=deque([6,1,3,4,6,7,3])
# de.pop()
# print("the deque after deleting from right is :")
# print(de)
# de.popleft()
# print("the deque after deleting from left is:")
# print(de)
# print("")

# UserDict
# UserDict is a dictionary-like container that acts as a wrapper around the dictionary objects. This container is used when someone wants to create their own dictionary with some modified or new functionality.
# class collections.UserDict([initialdata])



# UserList
# UserList is a list like container that acts as a wrapper around the list objects. This is useful when someone wants to create their own list with some modified or additional functionality.
# class collections.UserList([list])
# class Mylist(UserList):
#      def remove(self, s= None):
#          raise RuntimeError("Deletion not allowed")
#      def pop(self, s=None):
#          raise RuntimeError("Deletion not allowed")
# l=Mylist([1,2,3,4])
# print("Original list")
# l.append(5)
# print("After Insertion")
# print(l)
# l.remove()



# UserString
# UserString is a string like container and just like UserDict and UserList it acts as a wrapper around string objects. It is used when someone wants to create their own strings with some modified or additional functionality.
# class collections.UserString(seq)
# class Mystring(UserString):
#     def append(self,s):
#         self.data += s
#     def remove(self,s):
#         self.data = self.data.replace(s, "")
# s1=Mystring("ashish")
# print("Original String:",s1.data)
# s1.append("s")
# print("String after appending:",s1.data)
# s1.remove("h")
# print("String after Removing :",s1.data)
# print("")



# Counters in Python
# Containers are objects that hold objects. They provide a way to access the contained objects and iterate over them. Examples of built in containers are Tuple, list, and dictionary. Others are included in Collections module..
# print(Counter(['B','D','D','G','R','H']))
# print(Counter({'A':3,'B':5,'C':4}))
# print(Counter(A=3,B=5,C=4))

# Collections.UserDict in Python
# Python supports a dictionary like a container called UserDict present in the collections module. This class acts as a wrapper class around the dictionary objects. This class is useful when one wants to create a dictionary of their own with some modified functionality or with some new functionality.
# d={'a':1,
#    'b':2,
#    'c':3
#
# }
# f={
#     'a':5,
#     'b':6,
#     'c':7
# }
# userD=UserDict(d)
# print(userD.data)
# userD=UserDict(f)
# print(userD.data)
# print("")

# Collections.UserList
# Python Lists are array-like data structure but unlike it can be homogeneous. A single list may contain DataTypes like Integers, Strings, as well as Objects. List in Python are ordered and have a definite count.
l=[
    1,2,4,3,5
]
p=[
    2,4,5,6,7,7
]
userl=UserList(l)
print(userl.data)
userl=UserList(p)
print(userl.data)
print("")

# Collections.UserString
# Strings are the arrays of bytes representing Unicode characters. However, Python does not support the character data type. A character is a string of length one.
print("example 1")
d = 123445
userS= UserString(d)
print(userS.data)
users=UserString("")
print(userS.data)
print("")