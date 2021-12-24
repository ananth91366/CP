l = ["hello" , "take"]
l1 = ["dear","sir"]
print(l[0]+" " +l1[0])

l = [9,1,6,2,8,3,5,7,4]
l.sort(reverse=True)
print(l)

l = [1,2,3,4]
l.insert(1,[1,2,34])
print(l)

l = ["hello","hi"]
l1 = ["sir","madam"]

for x in l:
    for y in l1:
        print(x+' '+y)

list = [ [ ] ] * 5
print(list)  # output?
list[0].append(10)
print(list)  # output?
list[1].append(20)
print(list)  # output?
list.append(30)
print(list) # output?

l = ['aaaa','aaaaaa','aa','a','abcd','aaa']

for x in l:
    if len(x)>3:
        print(x)

l = [[1],[2],[3]]
l1 = []

for x in l:
    for y in x:
        l1.append(y)
print(l1)

l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]

output = []

# function used for removing nested
# lists in python.
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output.append(i)


print('The original list: ', l)
reemovNestings(l)
print('The list after removing nesting: ', output)

t = (1,2,3,4,2,2,2,3,4,2,2,2,1)
print(t[1])
print(len(t))
print(t.count(2))


t = (1,9,2,8,3,7,4,6,5)
print(sorted(t))


def one():

    print("I am from one method")
    two()
def two():
    print("I am from two method ")
    three()
def three():
    print("Iam from third method")

one()

for x in range(1,11):
    for n in range(2,10):
         print(n*x)

def make_word():
    word = ""
    for w in "krishna":
        word+=w
        yield word
res = list(make_word())
print(res)

def user(names):
    for name in names:
        print("Hello", "==", name)
user_names = ["abc","xyz","pqr"]
user(user_names)

a = 30
def fun():
    global a
    print(a)
    a =20
    print(a)
fun()
print(a)

x = "hyderbad"
print(x.isalpha())
y = "hyd123"
print(y.isalnum())
print("10.5".isdecimal())

n = int(input("Enter howmany time do you want:"))
d = {}
for i in range(n):
    item = input("Enter a no:")
    price = int(input("Enter a number:"))
    x = item
    y = x*price
    d[x] = y
print(d)

def fast_exponent(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_exponent(x*x, n/2)
    else:
        return x * fast_exponent(x, n-1)
res = fast_exponent(3,5)
print(res)

def exponent(x, n):
    if n == 0:
        return 1
    else:
        return x * exponent(x, n-1)

res = exponent(4,3)
print(res)
"""


"""
st = "iam learning python"
word = input("Enter a word:")
print(word in st )

x = "hyderbad"
print(x.isalpha())
y = "hyd123"
print(y.isalnum())
print("10.5".isdecimal())

l = int(input("Enter lower range:"))
u = int(input("Enter upper range:"))

for n in range(l,u+1):
    if n>1:
        for i in range(2,n):
            if(n%i) ==0:
                break
        else:
            print(n)
            
a = {1:3,"1":2,"a":5}

count = 0
for i in a:
   count+=a[i]

print(count)

for i in [20,10,3,4].sort():
    print(i)

for i  in [20,10,3,4][::-1]:
    print(i)


for i in sorted([20,10,3,4]):
    print(i)


list1 = ["these","are","a",["few","words"],"that","we","will","use"]

print(list1[3:4])
print(list1[3:4][0])
print(list1[3:4][0][1][2])

for i in range(1,20):
   if i == 5:

	  break
   else:
      print(i)
else:
   print("Hello")

import re
num = input("enter a num :")
res = re.findall('^[6-9]{1}[0-9]{9}$',num)
if res:
    print("valid")

else:
    print("invalid")

import re
password = input("enter password:")
res = re.findall('^[1-9]{2}[A-Za-z]{4}[!@#$%^&*]{2}$',password)
if res:
    print("valid")

else:
    print("invalid")
    
import re
st = "rain in hyd at 5:30 pm hyd is capital of tg hyd hyd hyd"
res = re.findall("hyd",st)
print(res)

import re
an = "ananth gopi krishna prudvi ananth akhila "
res = re.findall("ananth",an)
print(res)

import re
st = "rain in Hyd at 5:30 pm hyd is capital of tg hyd hyd hyd"
res = re.search("hyd",st)
print(res)
an = "ananth gopi krishna prudvi ananth akhila "
res = re.search("ananth",an)
print(res)

import re
st = "rain in hyd at 5:30 pm hyd is capital of tg hyd hyd hyd"
res = re.sub("hyd",'Hyderabad',st)
print(res)
an = "ananth gopi krishna prudvi ananth akhila "
res = re.sub("ananth",'krish',an)
print(res)

import re
st = "rain in hyd at 5:30 pm hyd is capital of tg hyd hyd "
res = re.subn("hyd","hyderabad",st)
print(res)
an = "ananth gopi krishna prudvi ananth akhila "
res = re.subn("ananth",'krish',an)
print(res)

import re
st = "rain in hyd at 5:30 pm"
res = re.findall('\d',st)
print(res)
res1 = re.findall('\D',st)
print(res1)
res2 = re.findall('\w',st)
print(res2)
res3 = re.findall('\W',st)
print(res3)
res4 = re.findall('\s',st)
print(res4)
res5 = re.findall('\S',st)
print(res5)

import re
st = "abcdefghijklmnopqrstuvwxyz"
res = re.findall('[d-n]',st)
print(res)

import re
st = "rain in hyd at 5:30 pm"
res = re.findall('^rain',st)
print(res)
st = "hyd is capital of tg"
res = re.findall('tg$',st)
print(res)

import re
st = "my mail id is xyz@gmail.com iam learning regular expression concept 191.0.01.1 python is oops 190.00.0.1 abc@gmail.com"
res = re.findall('\d{1,4}\.\d{1,3}\.\d{1,3}\.\d{1,3}',st)
print(res)
res1 = re.findall('\S',st)
print(res1)
res2= re.findall('\S+',st)
print(res2)
res3 = re.findall('\S+@',st)
print(res3)
res4 = re.findall('\S+@\S+',st)
print(res4)

a =  {1:3,"1":2,"a":5}


count = 0
for i in a:
   count+=a[i]

print(count)

for i  in [20,10,3,4][::-1]:
    print(i)


for i in sorted([20,10,3,4]):
    print(i)


for i in [20,10,3,4].sort():
    print(i)

list1 = ["these","are","a",["few","words"],"that","we","will","use"]
print(list1[6])
print(list1[3:4])
print(list1[3:4][0])
print(list1[3:4][0][1][2])

for i in range(1,20):
   if i == 5:
       break
	
   else:
      print(i)
else:
   print("Hello")

list1 = ["abc","123"]
list = []

for i in list1:
    list.append(i)

print(list)

list1 = ["ABC","XYZ","PqR"]
l = []

for i in list1:
    i.lower()
print(list1)
print(list(x.lower() for x in list1))

for i in list1:
    x = i.lower()
    l.append(x)
    print(l)

import re

password = input("enter password:")
res = re.findall('[1-9]{2}[A-Za-z]{4}[!@#$%^&*]{2}', password)
if res:
    print("valid")

else:
    print("invalid")

import re
num = input("enter a num :")
res = re.findall('^[6-9]{1}[0-9]{9}$',num)
if res:
    print("valid")

else:
    print("invalid")
    """
