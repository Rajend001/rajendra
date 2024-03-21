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



















a = 9
b = 6
print(a+b)
print(a._add_(b))# dunder method or mafic method


















