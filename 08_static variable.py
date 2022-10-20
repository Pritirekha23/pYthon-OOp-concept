# static variable(class level variable)
# if the value of the variable is common for all the object then we can go for static variable
# only one copy it will create and share to all
# memory utilization


# without static variable we can work but that is not efficient(meemory wastage)
print('-------without static variable---------')
class Student:
    def __init__(self,name,age,roll,college):
        self.name=name
        self.age=age
        self.roll=roll
        self.college=college
s1=Student('kubri',19,10107,'NIT')
s2=Student('Fanglie',23,3278,'NIT')
s3=Student('xiaoqiii',22,278654,'NIT')
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)

print('-------with static variable---------')
class Student:
    college='NIT college' #static variable(It is not the part of any object)
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
        
s1=Student('kubri',19,10107)
s2=Student('Fanglie',23,3278)
s3=Student('xiaoqiii',22,278654)
print(s1.__dict__)
print(s2.__dict__)   # so it does not print that static variable object
print(s3.__dict__)
