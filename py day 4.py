Day 4 morning 14/03/2024

--->while loop
--->break using while loop

Eg:1
1.literate from 20 to 30 and break the loop in 27
i=20
while i<30:
    if i==27:
        break
    print(i)
    i+=1
---> continue
eg:2
i=20
while i<31:
    if i==27:
        continue
    print(i)
    i+=1
eg:1
i=20
while i<31:
    i=i+1
    if i==27:
       continue
    print(i)
eg:
i=20
while i<31:
    if i==27:
        i=i+1
        continue
    print(i)
eg;
while to ilerate from 12 to 22
find the sum of all numbers

i=12
while i<23:
    if i==23:
        continue
    print(i)
    i+=1
eg:
i=12
sum=0
while i<23:
    sum=sum+i
    print(sum)
    i+=1

eg:
i=12
sum=0
while i<23:
    sum=sum+i
    i+=1
print(sum)
 eg:
find the average of value from 20 to 25
i=20
sum=0
while i<25:
    SUM=SUM+I
    i+=1
print(sum/6)

i=20
sum=0
count=0
while i<=30:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)

---->Nested for loop
Eg:

for row in range(1,3+1):
    for col in range(1,4+1):
        print(row,col)
Eg:
* * * *
* * * *
* * * *
* * * *

for row in range(rows):
    for col in range(cols):
        print("1",end="2")
        print()

eg:
for row in range(6):
    for col in range(6):
        print("*")

rows=int(input("enter the rows:"))
cols=int(input('enter the cols:"))

afternoon


for row in range(5):
    for col in range(5):
        print(row,end=" ")
   print()



eg:
sum=0
for row in range(5):
    for col in range(5):
         sum=sum+1
         print(sum,end=" ")
    print()


! to print stars in right angled triangle

  for row in range(0,6):
      for col in range(0,row):
          print("*",end=" ")
      print()


for row in range(0,6):
    for col in range(row+1,6):
          print("*",end=" ")
    print()


for row in range(5):
  for col in range(5):
    if row==0 or col==5-1 or row ==0 or col==5-1:
      print("*", end="")
    else:
      print(" ",end=" ")
  print()

for row in range(0,5):
    for col in range(0,6):
        if ((row==0 or col==3) or (row ==1 and col>=2 and col<=4)) or (row==2 and (col>1 and col<=5)))): or(row==2 and (col<=1 and col<=5)))):
      print("*", end="")
    else:
      print(" ",end=" ")
    print()


#----> list

---->data types
primary

1,numbers-->int,float,complex
2,string
3,boolean
4,none

collection
1,list
2,tuple
3,set
4,dictionary

--->list

1.if the collection of elements are surrounded by square brackets,it is considered
to be list
eg:
    l1=[4,7,9,9,89,"hello",7+9j,[8,9,0]]

characteristics of list
1.list have to be surrounded by[]
2.it is mutiple (the elements in the list are changable)
3.every element inside list is indexed
4.the elements inside list will be ordered format
5.it can hold duplicate values
6.its heterogenous

To access the elements in list
l1=[1,4,1,7,89,7,7,5,"p","i"]
   print(l1)

--->indexing
in the collection datatypes like list,tuple,string,the elements will be alloted
with pre-defined unique value called index value

we have 2 types of indexing
positive indexing -->starts with 0 from left hand side
Negitive indexing-->starts with -1 from left to right


positive indexing
print(lst1[0])
print(lst1[4])
print(lst1[20])--> error

negitive indexing
lst1=[1,4,1,7,7.5,"p","i"]
print(lst1[-1])
print(lst1[-5])


--->slicing
lst1=[1,4,1,7,7.5, "p","i"]
lst1[start_index:end_index:step]

print(lst1[0:4])
print(lst1[6:8])
print(lst1[3:6])
print(lst1[:5])
print(lst1[3:])
print(lst[:l])

print(lst1[0:7:1]) (lst1[0:7]---> both are same
print(lst1[0:7:2])


trail = int(input())

lst1=[1,4,1,7,7.5, "p","i"]
print(lst1[-1:-4])
print(lst1[-1:4])-->[]
print(lst1[-7:1])
print(lst1[-7:-1:2])

To insert at add element inside list

append()--> used to add element at last position of list
l1=[9,8,0,6]
l1.append("car")
print(l1)













    
        


    
                                                                                                                                                                                                                                       
    
         
    



