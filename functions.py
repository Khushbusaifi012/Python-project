# a=100
# b=20
# print("the sum :",a+b)
# print("the product :",a*b)
# print("the division :",a/b)
# print("the sub :",a-b)

# def calc(a,b):
#     print("the sum :",a+b)
#     print("the product :",a*b)
#     print("the division :",a/b)
#     print("the sub :",a-b)
# calc(10,20)    #call the function
# calc(10,200)

# 1.WAP TO PRINT HELLO IN FUNCTION?
# def wish():
#     print("hello")
# wish()

# 2. WAP TO PRINT HELLO WITH PARAMETERS?
# def wish(name):
#     print('hello {} , Good morning!!!'.format(name))
#  wish('khushbu')
# # wish('Bhupi')

# name=input("enter ur name:")
# wish(name)

# 3.WAP TO TAKE AS ARGUMENT AND PRINT A SQUARE VALUE?
# def square(number):
#     print("the square of {} is : {}".format(number,number**2))
# square(4)
# square(2)

# 4.WAP TO ACCEPT TWO NUMBERS AS INPUT AND RETURN SUM?
# def add(s,y):
#     return s+y
# result=add(10,20)
# result=add(100,20)
# print("the sum is : ",result)

# def f1():
#     print("hello")
# result=f1()
# print(result)

# 5.WAP TO CHECK EVEN OR ODD NUMBER?
# def even_odd(x):
#     if(x%2==0):
#         print("It is a even number")
#     else:
#         print("It is odd number.")
# even_odd(10)
# even_odd(9)
# even_odd(int(input("Enter a number : "))

# 6.WAP TO FIND FACTORIAL NUMBER?
# def factorial(x):
#     result=1
#     while(x>1):
#         result=result*x
#         x=x-1
#     return result
# print(factorial(5))

# for i in range(1,11):
#     print("The factorial of {} is : {}".format(i,factorial(i)))

# def calc(a,b):
#     sum=a+b
#     sub=a-b
#     return sum,sub
# x,y=calc(10,100)
# print("The sum :",x)
# print("the sub:",y)

# def f1(a,b):   #formal parameters
#     pass
# f1(10,20)  #actual arguments

#  POSITIONAL ARGUMENTS;;
# def sub(a,b):
#     print(a-b)
# sub(10,100)

# KEYWORD ARGUMENTS;;
# def sub(a,b):
#     print(a-b)
# sub(a=10,b=200)
# sub(b=100,a=10)

# def wish(name,msg):
    # print("hello",name,msg)
# wish('khushbu','good morning')

# DEFAULT ARGUMENTS;;
# def wish(name='Guest'):
#     print('Hello',name,'Good Morning!!')
# wish()
# wish('khushbu')

# VARIABLE LENGTH;;
# def f(*x):
#     print("Function")
# f()
# f(10)
# f(10,20)
# f(10,20,30)
# f(10,20,30,40,50)

# def sum(*n):
#     total=0
#     for n1 in n:
#         total=total+n1
#     print("The sum : ",total)
# sum(10,20)
# sum(10,20,30,0)
# sum(10,20,30,40,50)

# def sum(n,*s):
#     print(n)
#     print(s)
# sum(10)
# sum(10,20,30,50)

# def display(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
# display(name='khushbu',rollno=101,marks=90)

# def display(**kwargs):
#     for k,v in kwargs.items():
#         print('{}={}'.format(k,v))
# display(name='khushbu',rollno=101,esal=10000)

# def f1(arg1,arg2,arg3=4,arg4=8):
#     print(arg1,arg2,arg3,arg4)
# f1(3,2)
# f1(10,20,30,40)
# f1(25,50,arg4=100)
# f1(arg4=2,arg1=3,arg2=4)
# f1(arg3=10,arg4=20,30,40)
# f1(4,5,arg3=6)
# f1(4,5,arg3=5,arg5=6)

# def f1(*x,y=20):
    # print(x,y)
# f1(10,20,30,y=888)

# a=10
# def f1():
#     # a=20  #this is local variable
#     print(a)
# def f2():
#     print(a)
# f1()   #global variables
# f2()

# a=10   #global variable
# def f1():
#     a=777    #local variable
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()

# a=10
# def f1():
#     global a  #make global variable avaialabe to f1
#     a=777
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()

# def f1():
#     global a  #avaialble for both
#     a=10
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()

# def f1():
#     global a 
#     a=10
#     print(a)
# def f2():
#     global a
#     a=888
#     print(a)
# f1()
# f2()
# print(a)

# a=10
# def f1():
#     a=777
#     print(a)
# f1()

# a=10
# for i in range(1):
#     b=20
# print(a,b)

# RECURSIVE FUNCTIONS;;
# def factorial(n):
#     print('Finding factorial of : ',n)
#     if(n==0):
#         result=1
#     else:
#         result=n*factorial(n-1)
#     print('Completion of finding factorial of {} and result is {} '.format(n,result))
#     return result
# print("factorial of 4 is : ",factorial(4))
# print("factorial of 4 is : ",factorial(5))

# FIBONACCI SERIES;;
# def fib(n):
#     if(n==0):
#         return 0
#     elif(n==1 or n==2):
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(10):
#     print(fib(i))    

# LAMBDA FUNCTIONS;;
# WAP TO FIND SQUARE TO USING LAMBDA FUNCTION?
# s=lambda n:n*n
# print(type(s))
# print("The Square of 4 is :",s(4))

# WAP TO FIND OF TWO GIVEN NUMBERS?
# s=lambda a,b: a+b
# print("the sum of :",s(10,20))
# print("the sum of :",s(100,20))

# WAP TO FIND BIGGEST OF TWO NUMBERS?
# s=lambda a,b: a if a>b else b
# print("The biggest number is :",s(10,20))
# print("The biggest number is :",s(100,20))

# WAP TO FIND EVEN AND ODD NUMBERS?
# l=[0,5,10,15,20,25]
# EVENS=list(filter(lambda n:n%2==0,l))
# ODDS=list(filter(lambda n:n%2!=0,l))
# print(EVENS)
# print(ODDS)
 
# FILTER FUNCTION;;TO FIND EVEN NUMBERS?
# def is_Even(n):
#     if(n%2==0):
#         return True
#     else:
#         return False
# l=[1,2,3,4,5,6,7,8,9,10]
# output=list(filter(is_Even,l))
# print("The even number is :",output)

# TO FIND ODD NUMBERS?
# def is_odd(n):
#     if(n%2!=0):
#         return True
#     else:
#         return False
# l=[1,2,3,4,5,6,6,7,7,9,10,11]
# output=list(filter(is_odd,l))
# print("The odd number is :",output)

# TO FIND DIVISIBLE NUMBER BY 3;;
# l=[1,2,3,4,6,7,8,9,10]
# output=list(filter(lambda n:n%3 ==0,l))
# print(output) 

#  A SIMPLE PROGRAM;;
# class Employee:
#     def __init__(self,name,sal,age,has_gf):
#         self.name=name
#         self.sal=sal
#         self.age=age
#         self.has_gf=has_gf
#     def display(self):
#         return self.name
# e1=Employee('khushbu',200000,59,True)
# e2=Employee('hina',10000,23,True)
# e3=Employee('khushbu',200,58,False)
# e4=Employee('khushbu',1233,20,True)
# e5=Employee('durga',200000,60,True)
# e6=Employee('khushbu',200000,20,True)

# l=[e1,e2,e3,e4,e5,e6]
# output=filter(lambda e:e.sal >10000 and e.age>21 and e.has_gf,l)
# for e in output:
#    print(e.display())

# MAP FUNCTION;;
# def square(n):
#     return n*n
# l=[1,2,3,4,5]
# output=list(map(square,l))
# print(output)

# GENERATE OUTPUT BY MULTIPLYING VALUES FROM BOTH SIDES;;
# l1=[1,2,3,4]
# l2=[10,20,30,40]
# output=list(map(lambda x,y:x*y,l1,l2))
# print(output)

# CREATE A LIST WITH DOUBLE OF VALUES PRESENT IN LIST;;
# l=[1,2,3,4,5,6]
# output=list(map(lambda n:2*n,l))
# print(output)

# CREATE A LIST WITH DOUBLE OF VALUES SQUARE PRESENT IN LIST;;
# l=[1,2,3,4,5]
# output=list(map(lambda n:n**2,l))
# print(output)

# REDUCE FUNCTION;;TOTAL NUMBER SUM;;
# from functools import*
# l=[10,20,30,40,50]
# result=reduce(lambda x,y:x+y,l)
# print(result)

# PRINT THE SUM OF NUMBERS FROM 1 TO 100;;
# from functools import*
# l=[10,20,30,40]
# result=reduce(lambda x,y: x+y,range(1,101))
# print(result)