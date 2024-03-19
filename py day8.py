19/03/24
day:8 morning

eg:
def profile(name,age,place):
    txt = "my name is {}.iam {}years old.iam from{}."
    print(txt.format(name,age,place))
profile("sid",29,"cbe")

Eg:
return

1.a variable declared inside the function can be assessed outside the functionusing the return
2.return does not print anything
3.we cannot write any code below return statement



function with return statement

def f1():
    z = 8
f1()
print(z) #error--> cannot use outside the function


def f1(a,b):
    c = a*b
    return c
print(f1(6,8))
obj = f1(6,8)
obj1 = f1(4,6)

def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

123
 
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
        print("Not palindrome")
a = int(input("Enter the value:"))
palindrome(a)

based on the decleration of parameter and args
functions are divided into 5 catagories


positional args
keyword args
default args
variable length args
keyword variable length args

#positional args
The position of parameter a have to be same as position os arguments
Eg:1
To overcome the disadvantage of position args,we use keyword args
it is the process of initialishing the paremeter with the args with the args while calling the function
def def profile(name,phone,mark):
        txt = "my name is {}.my phone number is {}.i got {} marks."
        print(txt.format(name,phone,mark))

        

profile(9878776767,"sidhu",97) unexpected output

#keyword args
eg:1
todo-->Exception of keyword args function
def profile(name,phone,mark):
    txt = "my name is {}.my phone number is {}.i got {}marks."
    print(txt.format(name,phone,mark))

profile(name="sid, 1234567, mark=98) error-->positional arsg follow keyword
profile(1234567,name="sid"",mark=98)error --> name has multiple values
profile("sid",mark=98,phone=1234678)


--># default args
The method of assigning the argument to the paremeter while declaring the function
        
! Eg:1
def profile(name,phone,place="kadapa"):        
    txt = "my name is {}.my phone number is {}.i got {}marks."
    print(txt.format(name,phone,mark))

profile("sid",87878787)

eg:2
def profile(name,phone,place="kadapa"):
    if place=="kadapa" or place!="kadapa" or place!="kadapa":
        txt = "my name is {}.my phone number is {}.i got {}marks."
        print(txt.format(name,phone,place))
    else:
        print("you are not eligible to signup")
profile("sid",87676767)

# exception

def profile(name,phone,place="kadapa",phone):error-->coz default args should not follow positional param
    if place=="kadapa" or place!="kadapa" or place!="kadapa":
        txt = "my name is {}.my phone number is {}.i got {}marks."
        print(txt.format(name,phone,place))
    else:
        print("you are not eligible to signup")
profile("sid",87676767)

#1 variable length params
eg:1
To pass more than 1 arg to a paremeter means we use variable length args
To covert normal paremeter to variable length param,add to thir prefix of param

name = "sid",'name2','name3'
def profile(name):
    for val in name:
        print("my name is",val)
profile("sid",'name2','name3')


eg:

def profile(name):
    for val in name:
        print("my name is",val"my age is",age)
profile("sid",'name2','name3'28)-->error age has no args


def profile(name):
    for val in name:
        print("my name is",val,"my age is",age)
profile("sid",'name2','name3')

 #keyword variable length args
kwarges-->which is used to provide the args in the form of key value pair,
Eg;1
def price(**price_list):
    print(price_list)

price(shirt=1000,iphone=80000)

{'shirt': 1000, 'iphone': 80000}
{'a': 100, 'b': 200, 'c': 300}

n = 5
{1:1, 2:4, 3:9, 4:16, 5:25}

n = int(input("Enter the number:"))
d1 = {}
for val in range(1, n+1):
    d1[val] = val**2
print(d1)



def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val] = val**2
    print(d1)
dict(5)

#!---->object oriented programming
The paradigms of objects oriented programming are

class
objects
inheritance
polymorphism
abstaction
encapsulation

#! class is a blue print of an object

l1 = [1,2,3,4,5,6]


Eg:1
class c1:
    name = "sidhu"
    print(name1)


eg:2
class person:
    name = "sidhu"

c = person()
print(c.name) 

c = person() c as object
The process of creation of an object is called as instantiation
print(c.name)

#method without parameter
eg:3
create of a method
when the function is created with a class is called as method

class person:
    def display(): it is a method
        print("Hello welcome to class")
        
p = person()
p.display()


eg:4
#method with parameter
class person:
    def display(person,name,age):
        print(name,age)


p = person()
p.display("sidhu",28)


eg:5
class person:
    fname = "sidhu" #attribute or static variable
    fname = "T"
    
    def first_name(self):
        print(self.fname)
              
    def full_name(self):
        print(self fname+" "+self.fname)


p = person1()
p.first_name()
p.full_name()

eg:6
constructors-->_init_()
this is a special method which has the ablity to execute iotself without
calling it manually through the process of instaliation

class profile:
    def_init_(self): -->constructor method 
        print("hey")

p = profile() excution of constructor  through this process

























