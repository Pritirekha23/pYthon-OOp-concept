# Static variable creation in various places.
   # There are 6 different places we can create static variable.
   #1) Inside class directly
   #2) Outside of the class
   #3) Inside Constructor
   #4) Inside instance method
   #5) Inside class method
   #6) Inside Static method
 # insdie all these methods(4,5,6) we can create static variable

#(1) Creation of static variable inside class directly:


# example 1 inside class
print('------example1----')
class Student:
    college='NIT'  # static variable(class level variable)
s1=Student()
s2=Student()
print(s1.__dict__)
print(s2.__dict__)
print(Student.__dict__) # it is related to class

# Example2(instance class but outside of constructor and method)
print('--- Example2---')
class STudent:
    clg='NIT'
    branch='CSE'

    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
    def printdetails(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'roll is {self.roll}')
        print('-----------')

s1=STudent('kubbbu',27,102434)
s1.printdetails()
s2=STudent('rahul',26,67333)
s2.printdetails()
s3=STudent('shilla',22,673873)
s3.printdetails()
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)
print(STudent.__dict__)

# MEMORY REPRESENTATION:
print('---example3---')



#2)Creation of static variable inside class  inside constructor:


