# print("hello world")

# ADDITION;;
# a=10
# b=20
# print("the sum is = ",a+b)

# DATA TYPES;;
# a=10
# print(type(a))

# a=True
# print(type(a))

# a="khushbu"
# print(type(a))

# a,b,c,d=10,20,30,40
# print("the sum is = ",a+b+c+d)

# a,b=10,20
# c=300 if c>d else 400
# print(c)

# def f1():
#     print("python as functional programming")
# f1()
# f1()

# class student:
#     def read(self):
#         print("python as object oriented programming")
# obj=student()
# obj.read()

# class test:
#     def read(self):
#         print("python is a easy language")
# obj=test()
# obj.read()

# a=10
# b=20
# print(a is b)
# print(a is a)
# print(b is a)
# print(a is not b)

# a=None
# if a is not None:
#     print("a is not none")

# TO GENRATE OTP BY USING MODULE ;;
# from random import randint
# for i in range(10):
#     print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep="")

# x=10
# def f1():
#     print("f1 function")
# class test:
#     def m1(self):
#         print("m1 method")
# f1()
# obj=test()
# obj.m1()
# print(x)

# def f1():
#     print("hello")
# f1()

# import keyword
# print(keyword.kwlist)

# x=10
# if (x == 10):
#     print("x is 10")
# else:
#     print("x is 20")

# for i in range(10):
#     print("hello world")

# x=10
# print(x)
# print(type(x))
# print(id(x))

# INT TYPES;;
# a=111   #binary form 
# b=0B111   #decimal form;;
# c=0o123    #octal form;;
# d=0o123+0b11
# e=0X123FACE  #hexadecimal;;
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# a=10
# b=0B10
# c=0o10
# d=0X10
# print(a,b,c,d)

# print(bin(10))
# print(bin(0o10))
# print(bin(0X10))

# FLOAT TYPE;
# f=1.234
# print(type(f))
# d=1.2e3
# print(d)

# COMPLEX;;
# a=10+20j
# print(type(a))

# bool data type;;
# a=True
# print(type(a))

# age=30
# if (age > 25):
#     print("u should go for marriage")

# print(True+True)
# print(True+False)

# str data;;
# k="khushbu"
# print(type(k))

# k='khushbu' 
# print(type(k))

# s="""khushbu
#             software
#                     solutions"""
# print(s)

# string formatting;;
# k="khushbu"
# print(k[0])
# print(k[1])
# print(k[2])
# print(k[-1])
# print(k[len(k)-1])

# s="abcjduisadhiu"
# print(s[3:8])
# print(s[:8])
# print(s[0:])
# print(s[:])
# print(s[7:2])

# FIRST STRING INTO UPPERCASE;;
# s="khushbu"
# output=s[0].upper()+s[1:]    #first char will be uppercase
# output=s[0:len(s)-1]+s[-1].upper()          #last char will be uppercase
# print(output)
# print(output)

# k="lksdfkjndjf"
# output=k[0].upper()+k[1:len(k)-1]+k[-1].upper()
# print(output)

#concatenation,mathematical,multiplication;;;
# s="khushbu" + "saifi"
# k="khushbu"+'10'
# s="khushbu"*5   #repitition
# print(s)
# print(k)
# print(s)

# type casting;;
# print(int(10.9))
# print(float(20))
# print(int(True))
# print(int('100'))
# print(int(10.5))

# print(float('10.5'))
# print(float(0B1111))
# # print(float(10+20j)) #not applicable
# print(float(True))
# print(float(0x1101)) #hexagon

# complex;;
# print(complex(True))
# print(complex(10))
# print(complex(10.5))
# print(complex(False))
# print(complex('10'))
# print(complex('10.5'))

# str;;
# print(str(10))
# print(str(10.5))

# IMMUTABILITY;;
# x=10
# print(x+1)
# print(id(x))

# x=20
# y=x
# print(id(x))
# print(id(y))

# y=y+1
# print(id(x))
# print(id(y))

# x=True
# print(id(x))
# x=False
# print(id(x))

# a=10
# b=10
# c=10
# print(id(a))
# print(id(b))
# print(id(c))

# a=10.5
# b=10.5
# print(id(a))
# print(id(b))
# print(a is b)  #operator

# reusability;;
# a=254
# b=290
# print(a is b)

# LIST daTA TYPES;;
# l=[10,20,30,40]
# print(l)
# print(id(l))
# l[0]=8888
# print(l)
# print(id(l))

# l1=[10,20,30,40]
# l2=l1
# l1[0]=77777
# print(l1)
# print(l2)
# l2[1]=999
# print(l1)
# print(l2)

# l1=[10,20,30,40]
# l2=[10,20,30,40]
# print(id(l1))
# print(id(l2))

# l=[10,10.5,'khushbu',True,10] #heterogenous data
# print(l)
# print(l[0])
# print(l[-1])
# print(l[2:5])
# print(l.append('hina'))  #methods to add
# print(l)

# LIST DATA TYPES;;
# l=[10,20,30,40]
# print(l)
# print(l.append(50))  #add items
# print(l)
# print(l.remove(50)) #remove items
# print(l)
# l[0]=999  #indexing objects
# print(l)

# TUPLE DATA TYPE;;;
# t=(10,20,30,40,10,'khushbu',1.4)
# print(t)
# print(t[0])
# print(t[2:4])

# t=()
# print(type(t))
# t=(10)
# print(type(t))
# t=(10,)
# print(type(t))
# t=('khushbu',)
# print(type(t))
# t=10,20,30,40
# print(type(t))

# SETS DATA TYPE;;
# s={10,20,30,-20,'khushbu','mother',10.5}
# print(type(s))
# print(s)
# for x in s:
#     print(x)
# print(s.add(100))  #to add items
# print(s)
# print(s.remove(100))
# print(s)
# s={}
# print(type(s))
# s={10}
# print(type(s))
# s=set()   #function to call set
# print(type(s))
# print(len(s))
# print(s)

# l=[10,20,30,40]
# print(l.append(30))
# print(l)
# s={10,20,30,40}
# print(s.add(100))
# print(s)

# FROZENSET;;
# s={10,20,30,40}
# fs=frozenset(s)
# print(type(s))

# DICTIONRY;;
# d={1:'khushbu',200:'hina'}
# print(type(d))
# print(d)
# d={}
# print(type(d))
# d={}
# d[100]='khushbu'
# d[200]='hina'
# print(d)
# print(d[100])
# d={100:'k','h':200}
# print(d)
# d={10,'l',10,'k'}   #duplicates are not allowed
# print(d)
# d={100:'khushbu'}
# d[100]='hina'
# print(d)
# d={100:'khushbu',100:'hina',100:'anshu'}
# print(d)
# d={100:['khushbu','hina']}
# print(d)

# RANGE VALUES;;
# r=range(10)
# print(type(r))
# print(r)
# for x in r:
#     print(x)
# r=range(1,21)
# for x in r:
#     print(x)
# r=range(1,12,2)   #incremental step by step
# for x in r:
#     print(x)
# r=range(20,10,-1)
# for x in r:
#     print(x)
# l=[]  #convert range into list
# for x in range(0,101,5):
#     l.append(x)
# print(l)
# r=range(10)
# print(r[0])
# print(r[1])
# print(r[2:4])

# BYTES;;within the range 0 to 255
# l=[10,20,30,40]    
# b=bytes(l)
# print(type(b))
# print(b[0])
# print(b[-1])
# print(b[1:3])
# b1=b[1:3]
# for x in b1:
#     print(x)
# b=bytearray(l)
# b[0]=123
# for x in b:
#     print(x)
# print(type(b))

# NONE DATA TYPE;;
# def f1():
#     # return 10
#     print('hello')
# r=f1()
# print(r)
# x=None
# print(x)
# print(id(x))
# print(type(x))
# a=None
# b=None
# c=None
# def f1():
#     pass   #empty body
# d=f1()
# print(id(a),id(b),id(c),id(d))
# print(type(a))
# x=None
# print(type(x))
# x=''
# print(type(x))

# ESCAPE CHARACTERS;;;
# s='khushbu\tsaifi'
# k='world \nclasss \nskill \ncentre'
# print(s)
# print(k)
# b='the special word  \'thanks\' is very important'
# print(b)

# CONSTANTS;;
# max_value=10
# max_value=20
# print(max_value)

# x=input('enter some value  = ')
# print(type(x))

# x=input('enter some value  = ')
# i=int(x)
# print(type(i))
# x=input('enter some value  = ')
# j=float(x)
# print(type(j))
# x=input('enter some value  = ')
# k=bool(x)
# print(type(k))

# converted into int and their sum?
# x=input("enter first number  = ")
# y=input("enter second number  = ")
# i=int(x)
# j=int(y)
# print("the sum is  = ",i+j )

# x=int(input("enter first number  = "))
# y=int(input("enter second number  = "))
# print("the sum is  = ",x+y)

# print('the sum is  = ',int(input('Enter first no = '))+int(input("enter second number = ")))
# print(10+20+30,30+40+50)

# eno=int(input("emter employee number  = "))
# ename=input("Enter employee name = ")
# esal=float(input("Enter employee salary = "))
# eaddr=input("Enter employee Address = ")
# married=bool(input("employee married?[True|False]:"))
# print("please confirm ur information : ")
# print('Employee number = ',eno)
# print('Employee name = ',ename)
# print('Employee salary = ',esal)
# print('Employee address = ',eaddr)
# print('Employee marriage = ',married)

# print(bool(''))
# x=eval('10+20+30')
# print(type(x))
# print(x)

# x=eval(input("enter a value  = "))
# y=eval(input("enter a value  = "))
# print(x+y)

# x=eval(input("Enter some values  = "))
# print(type(x))
# print(x)

# s='10 20 30'
# l=s.split()
# print(l)

# s=input("enter two numbers  = ")
# print(s)
# l=s.split()
# print(l)
# print(type(s))
# print(type(l))

# list comprehension;;
# a,b=[int (x) for x in input("enter number  = ").split()]
# print(type(a))

# a,b=[int(x)for x in input("enter 2 values  = ").split()]
# print("the product is  = ",a*b)

# a,b,c=[float(x) for x in input("enter three float values = ").split(',')]
# print("the sum =  ",a+b+c)

# print('hello')
# print()
# print('khushbu')

# a,b,c=10,20,30
# print("the values are = ",a,b,c)
# name='bhupi'
# gf='khushbu'
# print('hello',name,'your girlfriend',gf,'is too good')

# SEP AND END ATTRIBUTES;;
# a,b,c=10,20,30
# print(a,b,c,sep=" = ")

# print('khushbu',end=",")
# print('hina')

# a,b,c=10,20,30
# print(a,b,c,sep="*",end='###')
# print(a,b,c,sep='-')
# print('khushbu',end="")

# string formattingmkdm;;
# a=1
# b=2
# c=3
# print('a value is %i' %(a))                 
# print('b value is %d and c value is %d'%(b,c))

# s='khushbu'
# l=[10,20,30]
# print('hello %s..the list of items are %s' %(s,l))

# name='khushbu'
# salary=100000
# friend='bhupi'
# print('hello {x}, your salary is {y} and your friend {z} is waiting'.format(x=name,y=salary,z=friend))

# s="learning python is very easy"
# print(s[1:5])
# print(s[1:7])
# print(s[:7])
# print(s[1:])
# print(s[:])
# print(s[1:7:1])
# print(s[1:15:1])
# print(s[1:15:3])

# s=input("enter a string = ")
# print("in forward direction")
# i=0
# while(i<len(s)):
#     print(s[i])
#     i=i+1
# print("in backward direction")
# i=-1
# while(i>=-len(s)):
#     print(s[i])
#     i=i-1

# s="khushbu"
# print('s'in s)
# print('m' in s)

# s="learning python is python easy"
# print(s.find('python',10,15))
# print(s.find('java'))
# print(s.find('r'))
# print(s.rfind('python')) #reverse direction

# s="aabbabababababaababaa"
# print(s.find('a'))
# print(s.rfind("a"))
# print(s.rfind('a',5,20))

# s="khushbu"
# print(s.find('a'))
# print(s.find('k'))
# print(s.rfind('h'))