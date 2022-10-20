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
        print(f'roll is {self.roll}')
s1=Student('Xioqi',29,107)
print(s1.__dict__)

#access instance variable within the class inside the  constructor
print('___________')
class Student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
      # access instance variable within the class inside the  constructor
   
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'roll is {self.roll}')
s1=Student('kubri',19,10107)

  # access instance variable outide of the class
print('**************')
class Student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
s1=Student('kubri',19,10107)
# accessing instance variable outside of the class usinng  object reference or reference variable
print(f'Name is {s1.name}')
print(f'Age is {s1.age}')
print(f'roll is {s1.roll}')

s2=Student('Fang leng',30,1565)
print(f'Name is {s2.name}')
print(f'Age is {s2.age}')
print(f'roll is {s2.roll}')


# WE CAN WRITE LIKE THIS ALSO
#s1=Student('kubri',19,10107)
#s2=Student('Fang leng',30,1565)
#print(f'Name is {s1.name}')
#print(f'Age is {s1.age}')
#print(f'roll is {s1.roll}')
#print(f'Name is {s2.name}')
#print(f'Age is {s2.age}')
#print(f'roll is {s2.roll}')




# Deletion of insatnce variable
 # we can delete in two different places (1)Inside the class (2) outside the class

# inside the class
   # inside instance method
print('---')
class Student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
        # delete data inside class inside instance method
    def deletedata(self):
      del self.name
s1=Student('priti',23,293)
print(s1.__dict__)
s1.deletedata()
print(s1.__dict__)


# delete inside the class instamce constructor
print('-----------')
class Student:
  def __init__(self,name,age,roll):
    self.name=name
    self.age=age
    self.roll=roll
    print(self.__dict__) # It will give detail of instance variable
      # delete instance varible inside class inside constructor
    del self.age
    print(self.__dict__)
    del self.name
    print(self.__dict__)
s3=Student('jungkook',27,823)


# deletion of instance variable outside of the class
print('---')
class Student:
    def __init__(self,name,age,roll):
      self.name=name
      self.age=age
      self.roll=roll

s4=Student('piku',9,7363)
print(s4.__dict__)
# delete instance variable outside of the class using reference variables
del s4.age
print(s4.__dict__)
del s4.roll,s4.name
print(s4.__dict__)

