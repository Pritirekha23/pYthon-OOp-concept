class Student1():
    def __init__(self):
        print(id(self))
s1=Student1()
print(id(s1))
# here self and s1 point into the same memory location

print('-'*10)
s2=Student1()
print(id(s2))

# 1st time s1 and self is same
# 2nd time s2 and self is same
# self is not a keyword in python
# instead of self we can use anything like x,y,any name or anything.
# But it is highly recomanded that use self .

print('prove that self is a variable')
class Student3:
    def __init__(vv):
        vv.name=input('Enter your name::')
        vv.age=int(input('Enter your age::'))
        vv.course=input('Enter your course::')
    
    def printdetails(vv):
        print('-'*40)
        print(f'Name is {vv.name}')
        print(f'Age is {vv.age}')
        print(f'Course is {vv.course}')


# 
s1=Student3()
s1.printdetails()

print('__________')
class Student22:
  def __init__(v,name,age,sid):
    v.name=name
    v.age=age
    v.sid=sid
  def printdetails(v):
    print(f'name is {v.name}')
    print(f'age is {v.age}')
    print(f'ssid is {v.sid}')
s1=Student22("priti",20,1056)
s1.printdetails()




print('----------')
class Student:
  def __init__(name,age,sid):
    name.age=age
    name.sid=sid
  def printdetails(v):
    print(f'age is {v.age}')
    print(f'sid is {v.sid}')
s1=Student(23,1002546)
s1.printdetails()




print('----------')
print('Here python take name as self so we get an error')
class Student:
  def __init__(name,age,sid):
    v.name=name
    v.age=age
    v.sid=sid
  def printdetails(v):
    print(f'name is {v.name}')
    print(f'age is {v.age}')
    print(f'ssid is {v.sid}')
s1=Student("priti",20,1056)
#s1=Student("priti",20,1056)
#TypeError: __init__() takes 3 positional arguments but 4 were given 
s1.printdetails()




