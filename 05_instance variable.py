# how to create instance variable in different different places.

# Instance variable:(object level variable)
# what is the requirement of an  Instance variable?
 # ans- If the value of a variable varies from object to object,then in such case we can go for instance variabel.

 # for each and every object separate copy of the instance variable will be created and that's why it is also called as Object level variable.

# Different place to create instance variable?
 # There are two places to create an instance variable, but there are 3 way to create an instance variable.

# 1. Inside class ((a) Inside constructor (b) Inside instance method) 2.Outside class((a) using reference variable)


# Creation of  instace variable  Inside constructor
print('_______Inside constructor__________')
class Student:
    def __init__(self,name,age,roll):
     self.name=name
     self.age=age
     self.roll=roll
s1=Student('prita',20,156)
print(s1.__dict__)
# it will give all the instace object present inside object and it will give in the form of dictionary

# Creation of  instace variable  Inside instance method
print('---------')
class studenT:
    def create(self,n,a,r):
        self.n=n
        self.a=a
        self.r=r
s1=studenT()
print(s1.__dict__) 
# when we create the object constructor will execute automatically but here create() is a  instance function so it wont be execute automatically, so we have to call it.
# before calling if i print 'print(s1.__dict__) ' then it will give an empty dictionary.
# this create() is a instance method.
s1.create('zinu',22,5676)
print(s1.__dict__)
#instance method it will take self as 1st argument


#Creation of  instace variable outside of the class (using reference variable)
print('___')
class sTudent():
    def __init__(self,name):
        self.name=name

s2=sTudent('zebra')
print(s2.__dict__)
s2.age=22  # this is create instace variable outside the class using reference variable
print(s2.__dict__)
s2.roll=1566 #dynamically we are adding instance variable to the object.
print(s2.__dict__)



