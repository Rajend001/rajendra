13/03/24
day three morning
Eg:
Take values of length and breadth of a
from user and check if it is square or not
length=int(input())
breadth=(int())
if length==breadth:
    print("its a square")
else:
    print("its not square")
    Eg:

    python program to check whether the
    given integer is a multiple of both 5 and 7
    n=int(input("enter the number"))
    if n%5==0 and n%7==0
    print("yes")
    else:
    print("no")
eg:
write a program to accept the cost price of a bike and display the
road tax to the paid
according to the following criteria:
    cost price (in Rs)           Tax
    >100000                     15%+discount 6%
    >50000 and <=100000         10%
    <=50000                     5%
price=int(input("enter the price"))
amount=0
if price>=100000:
    discount=price*(6/100)
    value=price-discount
    amount=value*(15/100)
    total=value+amount
else:
    tax=price*(5/100)
    total=price+tax
print("The onroad cost of bike is:",total)

if elif
Eg:1
a=7
b=9
c=3

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is grater")
else:
    print("c is greater")

A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
mark=int(input("enter mark:"))
if mark>=80 and mark<=100
    print("A")
elif mark>=60 and mark<=80:
    print("B")
elif mark>=50 and mark<=60:
    print("C")
elif mark>=40 and mark<=50:
    print("D")
else:
    print("fail")

    

Eg:
accept the age of 4 people and display the oldest one.
!--> short hand if else
Eg:1
a=9
b=60
if a>b:
    print("A")
else:
    print("B")
-->using short hand if else
* rules
1.statement inside the if condition have to be present at first
2.elif cannot be used in short hand if else
3e.Always it have to end with else

print("A") if a>b else print("B")

! code to check the given char is vowel or consonent
char =input("enter the char")
if char=="a" or char=='e' or char=='i' or char =='o' or char=='u':
      print("its consonent")

      ?or
 str="aelouAEIOU"
if char in strl:
    print("vowel")
else:
    print("consonent")
! short hand if else
char=input("enter the char:")
strl="aeiouAEIOU"
print("vowels") if char in strl else print("consonent)


elif ladder using short hand if else
eg:1
?find greatest among 3 variables using short hand if else
a=8
b=5
c=9

print("A is greater ") if a>b and b>C else print ("B is greater")
if b>a and b>c else print("C is greater")

Three day afternoon
!--------> looping

looping can be implimented using
for loop
while loop

---->for loop
for loop is used for ilteration,if we know the number of lines the loop have to run
?it is used to ilterate the iterables eg(string,list,tuple,etc...)

todo-->syntax for loop

for syntax in c
for (1=0;1<10,i++)(
    print("hello");

    
! for syntax in python
for userfined variable in range(start,end,step):defult step value is 1
    statement
    statement
    statement

    eg:1
To print the value from 1 to 10 using for loop

    for 1 in range(0,10):(n,n-1)
    print(i)
    print("helli")

    Eg:2
    for val in range(23,50,1):
    print(val)
    
    Eg:3
    for val in range(1,15,3):
    print(val)

to decrement the value

for val in range (10,0,-1):

    print(val)

for val in range(10,0,1):
    print(val)(no output)

    eg:4
    !print the output of 7th multiplication table from 21 to 43
for val in range (1,10+1,):
    print(val*7)
for val in range(1,10+1,):
    print('7','x',val,'=',val*7)-->method1

    ans="7 x {} ={}"
    print(ans.format(val,val*7)) --.method2
    -->metho3
for (val) in range (1,10+1,):
    print(f"7 x {val}={val*7}")
    eg :
    break -->used to terminate the loop
 eg :5
for val in range (1,10):
        if val==6:
            break
        print(val)
eg:6
for val in range (1,10):
        print val==6:
            if val ==6
             break
 eg:7       
for val in range (1,10):
        if val==6:
            print(val)
             break


! continue
eg:1
for val in range(1,10):
    if val==6:
        continue
    print(val)

!practice  problems
print the even number between 20 to 40
for val in range (20,41,)
    if val==%2==0:
    print(val)

!----> while loop
while is used when we do not knoe the number the loop have to run
to iterate the non iterable elements while loop is used

todo syntax

initilisation
while condition:
    statement
    incre or decre

eg:1
to literate number from 1 to 10

i=0
while i<11:
    print(i)

for loop practice
write a program to display sum of odd numbers and even
numbers that fall between
12 and 37(including both numbers)
for val in range (12,37)
in val==%1==0:
    print(val)

eg:
i=9
while i>0:
    print(i)
    i=i-10
             


eg:2
10,1
i=10
while i>0:
    print(i)
    i-=1

             
              


















