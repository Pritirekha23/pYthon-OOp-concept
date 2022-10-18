# self variable 
# what is Self?
  # refernce variable---  access object members outside of the class
  # self variable --- access object members inside of the class


# By using self variable we can access attributes and methods outside of the class, but if we want to access object attributes and methods inside the class then we can use self variable.
# self variable is used to access instance variable and instance method of an object inside the class.
#Self is used to refer to a current class  object or current memory.
# It is also acting as an accessor.
# Self is the first argument for constructor and instance method.
# self is not a keyword in python,instead of self we can write other names,but it is highly recomanded to use self.

# create a class Student having 3 attributes and 1 method.
class Student:
    def __init__(self):
        self.name=input('Enter your name::')
        self.age=int(input('Enter your age::'))
        self.course=input('Enter your course::')
    
    def printdetails(self):
        print('-'*40)
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'Course is {self.course}')


s1=Student()
s2=Student()
s3=Student()
s1.printdetails()
s2.printdetails()
s3.printdetails()
# at the time of object creation constructor will execute automatically.









