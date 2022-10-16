# dt-5/10/22
# 01 
# understanding class object and reference variable,self with real life example
# 02
# simple program using all 4 concept

# Real life example of class,object and reference variable
  # Usha company fan production example
  # Design(class)---Real fan(objrct)---to access the real fan we required some things like switch(here switch is the reference variable)

# for this design  we  can create multiple fans like for a single class we can create mmultiple objects.
#  class--- Blueprint,view,templet,layout,virtual encapsulation,virtual,logical entity,plan,model

# what is class?
  # If u want to create an object,then we required a blueprint and that bluprint is called class.
  # Inside class we will represent PROPERTIES(variable/attributes) and BEHAVIOUR(Methods or Action).
# Class is a grouping mechansing where we can store methods and variables.
# to wrap or bind properties and behaviour we required a class.
# if u want to wrap variable and methods into a single unit that is called as class.
# collection of object known as class.
# Syntax for define a class:
   # Class Classname:
      #  """Document String"""
      #Properties
      #methods


# what is object?
  # memory block,real,physical encapsulation,individual,part,instance
  # It is the physical existence of a class.
  # Object is the instance of a class.
  # Object means memory block.
  # Objects are created inside heap memory.
  # we can create any number of objects for a class.
#syntax for creating an object:
    # reference_variable=classname(arguments)

# what is reference variable?
  # Reference variable is used to refer to an object.
  # It is used to access properties and methods of an object.
  # refernce variable is acting as an accessor.
  # Multiple reference  variables can be point to the same object.
  
# Create a class Student
class Student:
  def __init__(self,name,age,sid):
    self.name=name
    self.age=age
    self.sid=sid
  def printdetails(self):
    print(f'name is {self.name}')
    print(f'age is {self.age}')
    print(f'ssid is {self.sid}')
s1=Student("priti",20,1056)
s1.printdetails()
print('------------------')
s2=Student("Smruti",23,4757)
s2.printdetails()
  

# self is always pointing to current object.
# self means current object.














































