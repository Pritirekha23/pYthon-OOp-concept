# prograam on instance variable
class Student:
    def __init__(self,name,age,rolll):
        self.name=name
        self.age=age
        self.roll=rolll
    def printdetails(self):
        print(f'name is {self.name}')
        print(f'age is {self.age}')
        print(f'roll is {self.roll}')
s1=Student('priti',17,156)
s1.address='Bhadrak'
s2=Student('kriti',18,157)
s3=Student('riti',19,158)
s3.address='bdk'
s3.course='Msc'
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)
print('-------')
s1.printdetails()
print('--------')
s2.printdetails()
print('---------')
s3.printdetails()