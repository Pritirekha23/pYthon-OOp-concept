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
class Student3:
    def __init__(self,name):
        self.name=name # insatnce variable
s10=Student3('Rahul')
Student3.clg='NIIt clg' # static variable
Student3.branch='CSE'
print(s10.__dict__)
print(Student3.__dict__)

#output
#----example-2-----
#{'name': 'Rahul'}
#{'__module__': '__main__', '__init__': <function Student3.__init__ at 0x0000022816F1FF70>, '__dict__': <attribute '__dict__' of 'Student3' objects>, '__weakref__': <attribute '__weakref__' of 'Student3' objects>, '__doc__': None, 'clg': 'NIIt clg', 'branch': 'CSE'}

print('*'*50)


  #3) Inside Constructor(using class name)
print('-----inside constructor----')
#example-1
class Student4:
    def __init__(self):
        Student4.clg='MNK college'
s12=Student4()
s13=Student4()
print(s12.__dict__)
print(s13.__dict__)
print(Student4.__dict__)

#output
#-----inside constructor----
#{}
#{}
#{'__module__': '__main__', '__init__': <function Student4.__init__ at 0x000002022915F040>, '__dict__': <attribute '__dict__' of 'Student4' objects>, '__weakref__': <attribute '__weakref__' of 'Student4' objects>, '__doc__': None, 'clg': 'MNK college'} 


print('example2')
class Student5:
    def __init__(self,name):
        Student5.clg='MNK college' #static variable
        Student5.branch='CSE'
        self.name=name # instance variable
s7=Student5('rahul')
s8=Student5('Kamalal')
print(s7.__dict__)
print(s8.__dict__)
print(Student5.__dict__)

# output
#example2
#{'name': 'rahul'}
#{'name': 'Kamalal'}
#{'__module__': '__main__', '__init__': <function Student5.__init__ at 0x000001EBF06310D0>, '__dict__': <attribute '__dict__' of 'Student5' objects>, '__weakref__': <attribute '__weakref__' of 'Student5' objects>, '__doc__': None, 'clg': 'MNK college', 'branch': 'CSE'}


#example--3
print()