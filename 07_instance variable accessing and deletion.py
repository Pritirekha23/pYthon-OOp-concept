# Accessing and Deletion of instance variable from differentplaces 

# ACCESSING INSTANCE VARIABLE
 # we can acess instance variable in 2 places
  #(1) Inside class (2) Outside of the class

# access within the class
print('---')
class Student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
      # access instance variable within the class inside instance method
    def printdetails(self): # instance method
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'Course is {self.roll}')
s1=Student('Xioqi',29,107)
print(s1.__dict__)


print('___________')
class Student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
      # access instance variable within the class inside constructor
    def printdetails(self): # instance method
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'Course is {self.roll}')
s1=Student('kubri',19,10107)
print(s1.__dict__)