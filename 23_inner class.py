#dt-11/01/23
# Inner or nested class

# if a class is present inside another class then this is called as inner class.
# inner class always depends upon outer class.Inner class does not exist without outer class existence.
# If there is no outer class then there is no chamce to exist inner class.
#ex- Bank is outer class where account is inner class

# One outer class can contain multiple inner class.

#ex-1
class Outer:
    def __init__(self):
        print('Outer class constructor')
    class Inner:
        def __init__(self):
            print('Inner class constructor')

# outer class object creation

obj1=Outer()

#i=Inner() (we cant create inner class object like this ,if we create then we will get an error)#NameError: name 'Inner' is not defined

#inner class object creation(outer class refernece.inner) 
# this is the way1 to create outer class objecr
i=obj1.Inner( )

#way2
i1=Outer.Inner()


# outer class as well aas inner class object creation.
i2=Outer().Inner()
# Outer().Inner() --- It means 1st it will create object of Outer class then it will create object of inner class


#output
#Outer class constructor
#Inner class constructor
#Inner class constructor
#Outer class constructor
#Inner class constructor


# NOTE :
    # you can not create inner class object directly u can create it by using Outer class reference variable or outer class name.
    # dual object creation also possible.


#ex-2
# inner class object creation inside outer class

print('---ex-2---------')

class Outer:
    def __init__(self):
        print('Outer class constructor')
    class Inner:
        def __init__(self):
            print('Inner class constructor')
    i5=Inner()
O=Outer()

#output:
#---ex-2---------
#Inner class constructor
#Outer class constructor


#ex-3  ---> one outer class can contain multiple inner class.
print('---ex-3----')
class Outer:
    def __init__(self):
        print('Outer class constructor')
    class Inner:
        def __init__(self):
            print('Inner class constructor')
    class Inner2:
        def __init__(self):
            print('Inner class2 constructor')

O=Outer()
i8=O.Inner()
i7=O.Inner()

# output
#---ex-3----
#Outer class constructor
#Inner class constructor
#Inner class constructor


# ex-4  Inner-Inner class
print('-----------')


class Outer:
    def __init__(self):
        print('Outer class constructor')

    class Inner:
        def __init__(self):
            print('Inner class constructor')

        class InnerInner:
            def __init__(self):
               print('InnerInner class constructor')
 

O = Outer()
i9 = O.Inner()
i34=i9.InnerInner()
obj=Outer.Inner.InnerInner()
#output
#-----------
#Outer class constructor
#Inner class constructor
#InnerInner class constructor
#InnerInner class constructor






