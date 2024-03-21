21/03/24
day 10 morning


#! method riding
polymorphism in class

Eg:1
class bank:
    def ratio(self):
        print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()

Eg:2
class USA:
    def language(self):
        print("English")


    def capital(self):
        print("washington Dc")

class India(USA):
    def language(self):
        print("none")

    def capital(self):
        print("New delhi")

I = India()
I.language()
I.capital()

Eg:3

polymorphism using objects

c1,c2---->c1 = print(c1),print(c2)
f1,f2

class c1:
    def f1(self):
        print("class1")

class c2(c1):
    def f1(self):
        print("class2")

obj1 = c2()
obj2 = c1()


Eg:4

class c1:
    def f1(self):
        print("class1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class2")

obj1 = c2()
obj2 = c1()

def display(a):
    a.f1()
display(obj1)
display(obj2)

# changing the functionality of builtin function
 class shooping:
     def_init_(self,l1):
         self,item = l1

     def_len_(self):
         length = len(self,item)
         return length
s = shoping ([1,2,3,4,5])
print(len(s))

#--->method overloading
Eg:
class suming:
    def add(self,a,b):
        print(a+b)

    def add(self,a,b,c):
        print(a+b+c)

s = suming()
s.add(4,3)#------>error
s.add(4,5,1)

Eg:2
class summing:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)
obj=summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)


#----->abstraction
The process of hiding the implimentation details is abstraction

Eg:1

from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
class shape(self):
    def sides(self):
        print("All shapes have sides expect circles")

class triangle:
    def triangle_sides(self):
        print("3sides")

    def name(self):
        print("iam triangle")

    def sides(self):
        pass

class square(shapes):
    def square(self):
        print("4 sides")

    def square(self):
        pass
        
tr = triangle()
tr.triangle_sides()
tr.name()

#rules to define abstact class1
1.Absract class cannot be instatained
2.from abc import ABC,abstractmethod
3.subclass the normal class with ABC
4.covert the normal method inside the abstact class to abstact method
5.All the child classes have to be subclasses with abstact class
6.the abstract method should be present in the child classes


Eg:2
super()--> used to access the parent class method from child method
from abc  import ABC,abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")


class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")

    def m1(self)
        pass

class2 = c2()
class2.m2()


eg:3
from abc import ABC,abstractmethod
class password:
    @abstractmethod
    def pwd(self):
        pswd = "sidd1994$"
        return pswd

class login:
    def validate(self,name,parent):
        if super().pwd()== password:
           print("welcome",name,'!!')
           print("login,successfull")
     else:
           print("please check the password")

    def pwd(self):
        pass

Login = login()
name = input("Enter the name: ")
pwd = input("Enter the password: ")
Login.validate(name,pwd)


#Encapsulation
eg:1
class car:
   _name = "BMW" private variable
   print(_name)

c1 = car()
print(c1.name)# error
c1.name = "Audi"
print(c1.name) # error

Eg:2
#! accessing private data outside the class
class c1:
    _phone = '7676767676'

    def display(self):
        print(self._phone)
c = c1()
c.display()


--->Eg:3
declare private method
class class1:
    def _m1(self): #private method
        print("Iam private method")

    def_init_(self):
        self._m1()
c = class1()
c._m1() #error

?nested class:
class class1:
    class class2:
        name = "sidhu"

        def display(self):
            print(self.name)
    obj1 = class2()

obj = class1()
obj.obj1.display()






























