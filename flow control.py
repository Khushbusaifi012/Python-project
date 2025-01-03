# class test:
#     print("statement-1")
#     print("statement-2")
#     def m1(self):
#         print("statements")
# print("statement-3")

# for i in range(1,10):
#     print("hello")
#     print("hi")       
# print("khushbu")

# IF CONDITION;;
# name=input("enter ur name = ")
# if (name=="khushbu"):
#     print("hello khushbu")
# print("u r not khushbu")

# IF ELSE CONDITION;;
# name=input("enter ur name = ")
# if (name=="khushbu"):
#     print("hello khushbu")
# else:
#     print("hello guest")
# print("how are u ?")

# IF ELIF ELSE CONDIITION;;
# brand=input("enter your favourite brand = ")
# if(brand=="RC"):
#     print("it is children brand")
# elif(brand=="KF"):
#     print("it is not that much kick")
# elif(brand=="KO"):
#     print("It is too light")
# elif (brand=="FO"):
#     print("buy one get one free")
# else:
#     print("other brands are no recommendeed")

# n1=int(input("enter first number = "))
# n2=int(input("enter second number  = "))
# if(n1>n2):
#     print("biggest number  = ",n1)
# else:
#     print("biggest number  = ",n2)

# n1=int(input("enter first number = "))
# n2=int(input("enter second number  = "))
# n3=int(input("enter third number  = "))
# if(n1>n2 and n1>n3):
#     print("biggest number  = ",n1)
# elif(n2>n3):
#       print("biggest number  = ",n2)
# else:
#      print("biggest number  = ",n3)
  
# n=int(input("enter a number  = "))
# if(n%2==0):
#     print("even number")
# else:
#     print("odd number")

# n=int(input("enter a digit from 0 to 9  = "))
# if(n==0):
#     print("zero")
# elif(n==1):
#     print("one")
# elif(n==2):
#     print("two")
# elif(n==3):
#     print("three")
# elif(n==4):
#     print("four")
# elif(n==5):
#     print("five")
# elif(n==6):
#     print("six")
# elif(n==7):
#     print("seven")
# elif(n==8):
#     print("eight")
# elif(n==9):
#     print("nine")
# elif(n==10):
#     print("ten")
# else:
#     print("print enter 0 to 10 digits only")

# n=int(input("enter a digit from 0 to 9  = "))
# d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:"nine",10:"ten"}
# if (n in d):
#     print(d[n])
# else:
#     print("enter digits only 0 to 9")

# n=int(input("enter a digit from 0 to 9  = "))
# units={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:"nine"}
# tens={2:'twenty',3:'thirty'}
# unitdigt=n%10
# tenthdigit=n//10
# output=tens[tenthdigit]+" "+units[unitdigt]
# print(output)

#  s="khushbu"
# s=input("enter any tring = ")
# for ch in s:
#     print("the current character is = ",ch)

# to check the string indexwise;;
# s=input("enter any string  = ")
# i=0
# for ch in s:
#     print("the character present at",i,'index:',ch)
#     i+=1

# for i in range(0,10):
#     print(i,"hello")

# for x in range(11):
#     print(x)

# for x in range(21):
#     if(x%2!=0):
#         print(x)

# for x in range(1,21,2):
#     print(x)

# for x in range(10,0,-1):
#     print(x)

# l=eval(input("enter list = "))
# sum=0
# for x in l:
#     sum=sum+x
# print('the sum is  = ',sum)

# WHILE LOOP;;
# x=1
# while(x<=10):
#     print(x)
#     x=x+1

# n=int(input("enter a number  = "))
# sum=0
# i=1
# while(i<=n):
#     sum=sum+i
#     i=i+1
# print("the sum of first {} numbers = {}".format(n,sum))

# name=''
# while(name!='khushbu'):
#     name=input("enter ur fvrt heroine = ")
# print("thanks for confirmation")

# i=0
# while(True):
#     i=i+1
#     print("the current count  = ",i)

# name=''
# i=1
# while(name!='khushbu'and i<=10):
#     name=input("enter ur favourite heroine = ")
#     i=i+1

# for i in range(4):
#     for j in range(4):
#         print(i,j)

# while (True):
#     username=input("enter username = ")
#     password=input("enter password = ")
#     if(username=="khushbu" and password=='saheen'):
#         print("u are valid user,u can avail services")
#         break
#     else:
#         print('ur credentials is invalid ,please provide login')

# BREAK STATEMENTS;;
# for i in range(10):
#     if (i==7):
#         print("loop execution enought..please break")
#         break
#     print(i)

# cart=[10,20,30,40,40,600,700]
# for item in cart:
#     if(item>500):
#         print("to place this order insurnace must be required")
#         break
#     print(item)

# CONTINUE STATEMENT;;
# for i in range(10):
#     if(i%2==0):
#         continue
#     print(i)

# cart=[10,20,500,700,50,60]
# for item in cart:
#     if(item>=500):
#         print("we cannot process this item because of insurance item",item)
#         continue
#     print("processing item",item)

# numbers=[10,20,0,5,0,30]
# for n in numbers:
#     if(n==0):
#         print("hello,how we can divide with zero..just skipping")
#         continue
#     print("100/{}={}".format(n,100/n))

# # ELSE METHOD;;
# cart=[10,20,30,700,40,50]
# for item in cart:
#     if(item>=500):
#         print("we cannot place this order")
#         break
#     print("processing items",item)
# else:
    # print("congrats all ur items processed successfully")

# pass statement;;
# if(10>20):
#     print("hello")
# else:
#     pass

# def additem():
#     pass
# def deleteitem():
#     pass
# def updateitem():
#     print("update item implementation")

# DELETE STATEMENT;;
# x=10
# del x
# print(x)

# s1='khushbu'
# s2=s1
# s3=s1
# del s1
# print(s2)
# print(s3)
# del s1,s2,s3

# s1='moon'
# del s1
# print(s1)
# s1='moon'
# s1=None
# print(s1)

# s1="khushbu"
# print(s1)
# del s1

# s="the butterfly "is" beautiful"
# print(s)

# s='khushbu'
# print(s[1])
# print(s[-1])

# s=input("enter any string = ")
# i=0
# for x in s:
#     print("the character present at positive index {} and at negative index is {} is : {}".format(i,i-len(s),x))
#     i=i+1

# s1=input("enter string = ")
# s2=input("enter second string = ")
# if(s1==s2):
#     print("both strings are equal")
# elif(s1<s2):
#     print("first string is less than second string")
# else:
#     print("first string is greater than second string")

# city=input("enter ur city name = ").lower().strip()   
# if(city=="delhi"):
#     print("hello delhities")
# elif (city=="chennai"):
#     print("hello madrasi")
# elif(city=="bangalore"):
#     print("hello kannadiga")
# else:
#     print("your entered city is invalid")