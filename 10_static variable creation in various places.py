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

# output
#------example1----
#{}
#{}
#{'__module__': '__main__', 'college': 'NIT', '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}   

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
print(id(Student))
print(id(s1))
print(id(s2))
print(id(s3))

# output 
#--- Example2---
#Name is kubbbu
#Age is 27
#roll is 102434
#-----------
#Name is rahul
#Age is 26
#roll is 67333
#-----------
#Name is shilla
#Age is 22
#roll is 673873
#-----------
#{'name': 'kubbbu', 'age': 27, 'roll': 102434}
#{'name': 'rahul', 'age': 26, 'roll': 67333}
#{'name': 'shilla', 'age': 22, 'roll': 673873}
#{'__module__': '__main__', 'clg': 'NIT', 'branch': 'CSE', '__init__': <function #STudent.__init__ at 0x00000246138FFE50>, 'printdetails': <function STudent.printdetails at 0x00000246138FFEE0>, '__dict__': <attribute '__dict__' of 'STudent' objects>, '__weakref__': <attribute '__weakref__' of 'STudent' objects>, '__doc__': None}     
#2499997637936
#2499999212688
#2499999213168
#2499999213120



#2  Outside of the class(by using class name)
print('------outside of the class------Example-1--')
class Student2:
    pass
s11=Student2()
Student2.clg='NIIt clg' # static variable
Student2.branch='CSE'
print(s11.__dict__)
print(Student2.__dict__)
# output
#{}
#{'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Student2' objects>, '__weakref__': <attribute '__weakref__' of 'Student2' objects>, '__doc__': None, 'clg': 'NIIt clg', 'branch': 'CSE'}



print('*'*20)



print('----example-2-----')

