15/03/25 day 5 morning

----->common functions for List

l1=[6,7,8,9,0]
print(len(l1)

print(max(l1))
print(min(l1))

l1=[6,8,9,"p","u"]
print(max(l1)) --->error coz its a combination of int and string
print(min(l1)) --->error coz its a combination of int and string

l1=[6,7,8,9,8.89,5,0.78]
index()---->to get index value of specific element
print(l1,index(9))

count()--.how many number of times an element is repeated
print(l1.count(6))

some functions which is specifically used for list  

To add element inside list
insert()-->to add element at specific index position
l1=[6,7,8,9,8.89,-5,0.78]
l1.insert(2,"cars")
print(l1)

To delet element from list
l1=[6,7,8,9,8.89,-5,0.78]
pop()--->last element will be deleted      
l1pop()
print(l1)

pop(index_value)--->used to delete element at specific index
l1.pop(4)#4 is index value
print(l1)

remove(element)--->used to delete element directly        
l1.remove(8.89)
print(l1)

clear()--->to complete delete all element in list
l1.clear()      
print(l1)

del--->to delete the list
del l1 or del(l1)
print(l1)

--->join 2 lists

l1=[9,0,8]
l2=["p","o","t",34]
print(l1+l2)

or
extend()-->to combine 2 lists
l1.extend(l2)
print(l1)

--->copy()
l1=[6,7,8,9,3]
l2=l1:copy()
print(l1)
print(l2)

print(id(l1))
print(id(l2))

different between shallow copy and deep copy      
#shallow copy
import copy
l1=[8,9,0,[5,6],[3,2,1]]
l2=copy.copy(l1)
l1.append(890)
print(l1)
print(l2)

#deep copy-->used to copy the list with nested list
import copy
l1=[8,9,0,[5,6],[3,2,1]]
print(l1[-1][1])--->to index nested list

l2=copy.deepcopy(l1)
l1[-1].append('cars')
print(l1)
print(l2)

sort-->arrange elements in list in ascending or descending order
l1=[9,7,45,0,-6,5,12]
l1.sort()#to arrange in ascending order
print(l1)

l1.sort(reverse=true)#to arrange in descending order
print(l1)

l['z','i','o','p',9]
l1.sort()
print)l1)--->error

list constructor
list()-->to convert other collection datatype to list
l3=((8,9,0))
print(list(l3))

l4=(8,9)
print(list(l4))

--->nested list
l1=[8,9,[0,8,7],["p","o","y"],[8,'t']]
print(l1[-2][1])-->o

print(l1[1:4])
print(l1[1:-1])

to delete "t" from l1
l1[-1].remove('t')
print(l1)

combine these ["p","o","y"],[8,'t'] lists in l1
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)

--->Tuple
char of tuple

1.)tuple have to be surrounded by()
2.)The elements inside tuple are not changable
3.)The elements inside tuple are indexed
4.)The element will execute in order
5.)It is heterogenous
6.)It allow duplicate elements

Eg:
t1=(8,8,9,6,5.78,[9,0],(6,8),"hey",9+6)
print(t1)
print(type(t1))

indexing,slicing are all same as list

l1=[8]
print(type(l1) int

l1=(8)
print(type(l1)) tuple
     
t1=8,9
print(type(t1)) tuple
     
t2=8,
print(type(t2)) tuple
     
len(),min(),index(),count()--->all same as list

To add element inside tuple--->cannot add
cannot delete any element from tuple
     

join 2 tuples
t1=(8,9,0)
t2=(6,7,8)
print(t1+t2)

To add all element inside list and tuple
sum()      
l1=[8,9,7,6]
print(sum(l1))

sort tuple
t1=(8,9,0,89,12)
print(tuple(sorted(t1))
print(tuple(sorted(t1),reverse=True)))

iterate list and tuples

iterate based on index value
l1 = [9,8,0,6,5]
for i in ll:
    print(i)

iterate based on the index
l1 = [9,8,0,6,5,8,56]
for i in range(0,len(l1)):
    print(l1[i])

!--->strings

s1 = 'u'
print(type(s1))

s1 = "hello world"
to access string
print(s1)
  indexing and slicing-->same as list and tuple
print(s1[0:5])

-->common functions

len(),min(),max(),index(),count()
s1 = "hello world"
 print(len(s1))
 print(max(s1))
 print(min(s1))

ord()-->used to find the ASCII value of a character
s1 = 'u'
print(ord(s1))

  functions of string
s1 = "hello world"

 ?to convert all charactrs to upper case
 print(s1.upper())


 ? to convert to lower case
 s1 = "HFREDGiou"
 print(s1.lower())

-->strip()--> to eliminate the space in beginning and end of string''
s1 = where are you?"
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())

  split()-->to split the words in string based on a character
s1 = "where are you?"
print(s1.split())
print(s1.split("r"))

print(s1.count('e'))


replace()
s1 = "where are you?"
print(s1.replace('r', %%'))

swapcase()---> to convert capital to small to captial at a time
s1 = "HEY there"
print(s1.swapcase())

  title()--> to write the string in format of title
s1 = 'never give up'
print(s1.captialize())


join the strings
s1 = "hello"
s2 = 'world'
print(s1+s2)
                 
s1 = '''
how are you
iam fine
here there
'''


 splitline()--->used to split the string based on lines
print(s1.splitlines())


find()-->to find the index based on a character
s1 = "hello world"
print(s1.find('z'))
print(s1.index('z'))

join()-->
l1 = ["hey","there"]
print(" ".join(l1))
print("$".join(l1))

s1 = "welcom to  all"
    print(s1.endswitch('1))
    print(s1.startswitch('w'))

s1 = "67"
print(type(s1))
print(s1.isdigit())

print the string in reverse manner
s1 = "welcom" to all"
print(s1[::-1])

EG:1
wap to find the number of lower case letters
s1 = "HEY there you aRE"
for i in s1:
    print(i)

count = 0
for i in s1:
    if 1.islower():
         count+=1
print("the total num of lower case letters : ",count

eg:2--> "$"
s1 = 'restarter'
print(s1.replace('r',"$"))

s1 = 'restarter'
s1 = "IMAGIN"
fst = s1[0]
bal = s1[1:]
txt = bal.replace(fst,"$")
print(fst+txt)

eg:

s1='''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
chracters = len(s1)
print(characters)

words = s1,split(" ")
print(len(words))


sentenses = s1.split(',')
for val in sentences:
    if val =='':
        index = (sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))

space = 0
for val in s1:
    if val ==" ":
        space=space+1
print(space)        



















                 

s1 = "welcome to all"














s1 = "hey there dont sleep"
i = 7




      















15
