# DATA STRUCTURE;;
# d={100:'k',200:'h',200:'l'}
# print(d)

# d={100:'k','b':200}
# print(d)

# CREATION DICTIONARY;;
# d={}
# d[100]="khushbu"
# d[200]='b'
# d[100]="k"
# # print(d)

# ACCESSING KEY VALUES PAIRS;;
# d={100:'khushbu',200:'b',300:'h',400:'m'}
# print(d[100])
# print(d[200])

# EXAMPLE WITH MEMBERSHIP OPERATOR;;
# key=input('enter key to find corresponding values = ')
# if key in d:
#     print(d[key])
# else:
#     print('specified key not available')
# print(d[key])

# HOW TO UPDATE DICTIONARY;;
# d={100:'khushbu',200:'saifi'}
# d[400]="Anshika"
# print(d)
# d[100]="riya"
# print(d)

# HOW TO DELETED DICTIONARY;;
# d={100:'khushbu',200:'saifi'}
# del d[100]
# print(d)

# TO REMOVE ALL ENTRIES IN DICT;;
# d={100:'khushbu',200:'b',300:'h',400:'m'}
# d.clear()
# print(d)

# IMPORTANT METHOD-LEN();;
# d=dict({(100,'abc'),(200,'mdu'),(300,'Du')})
# print(len(d))

# GET();;
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.get(200))
# print(d.get(500))   #none

# POP();;
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.pop(100))
# print(d.pop(200))

# POPITEM();;
# d={100:"durga",200:"ravi",300:"shiva"}
# property(d.popitem())
# print(d)

# PROGRAM ALPHABET WITH NUMBERS;;
# i=0
# d={}
# while i<26:
#     d[chr(65+i)]=100+10*i
#     i=i+1
# print(d)
# while len(d)!=0:
#     print('processing item = ',d.popitem())
# k=d.keys()
# print(type(k))
# print(k)

# ITEMS(),VALUES(),KEYS();;
# d={100:"durga",200:"ravi",300:"shiva"}
# i=d.items()
# print(type(i))
# print(i)
# for x in d.items():
#     print(x)
# for k,v in d.items():
#     print('{}:{}'.format(k,v))
# for k in d.keys():
#     print(k)
# for v in d.values():
#     print(v)

# SETDEFAULT();;
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.setdefault(400,'khushbu'))
# print(d)

# COPY();;
# d1={100:"durga",200:"ravi",300:"shiva"}
# d2=d1.copy()
# print(id(d1))
# print(id(d2))

#  QUESTION-1 WAP TO ENTER NAME AND MARKS IN A DICTIONARY AND DISPPLAY INFORMATION?
# d={}
# while True:
#     name=input('enter student name = ')
#     marks=int(input('enter student marks = '))
#     d[name]=marks
#     print('student record inserted successfully')
#     option=input("Do you want to insert one more student marks[yes|no] = ")
#     while True:  
#         if option.lower()=='no':
#             option='no'
#             break
#         elif option.lower()=='yes':
#             option='yes'
#             break
#         else:
#             option=input('your entered option is invalid,please choose correct option [yes|no] = ')
#     if option=='no':
#         break
# print(d)

# QUESTION-2 WAP TO CREATE DICT AND PRINT THE SUM OF VALUES?
# d=eval(input("enter dictionary = "))
# print('The sum is = ',sum(d.values()))

# QUESTION-3 WAP TO FIND NUMBER OF OCCURENCES OF EACH LETTER PRESENT IN THE GIVEN STRING?
# s=input("enter any word = ")
# d={}
# for ch in s:
#     if ch in d:
#         d[ch]=d[ch]+1
#     else:
#         d[ch]=1
# print(d)

# QUESTION-4 WAP TO FIND NUMBERS OF OCCURENCES OF EACH VOWELS PRESENT IN THE GIVEN STRING?
# s=input("enter any string = ")
# vowels={'a','e','i','o','u'}
# d={}
# for ch in s:
#     if ch in vowels:
#         d[ch]=d.get(ch,0)+1
# for k,v in sorted(d.items()):
#     print('{} occurs {} times'.format(k,v)

# QUESTION-5 WAP TO ACCEPT STUDENT NAME AND MARKS WITH THAT DATA CREATES A DICT ALSO DISPLAY STUDENT MARKS BY TAKING STUDENT NAME AS INPUT?
# n=int(input("Enter number of students = "))
# d={}
# for i in range(n):
#     name=input("Enter student name  = ")
#     marks=int(input("Enter student marks = "))
#     d[name]=marks
# print("All students data inserted")
# while True:
#     name=input("Enter student name to get marks = ")
#     if name in d:
#         print('The marks of {}:{}'.format(name,d[name]))
#     else:
#         print('Student not found')
#     option=input("Do u want to find another student name[yes|no] = ")
#     while option.lower() not in ['yes','no']:
#         option=input('Inavalid option,please choose valid option[yes|no] = ')
#     if option.lower()=='no':
#         break
# print("Thanks for using our application")

# DICTIONARY COMPPREHENSION;;
# d={x:x*x for x in range(1,6)}
# print(type(d))
# print(d)

# doubles={x: 2*x for x in range(1,6)}
# print(doubles)

# alphabets={x: chr(64+x) for x in range(1,27)}
# print(alphabets)

# MERGING COLLECTIONS;;
# d1={100:'A',200:'B'}
# d2={300:'C',400:'D'}
# d3={500:'E',600:'F'}
# result={**d1,**d2,**d3}
# print(result)

# NESTED APPLICATIONS;;
# d={
#     'cars':('Innova','Honda','BMW'),
#     'Mobiles':('Samsung','Nokia','Iphone')
# }
# # TO DISPLAY 2ND CAR;;
# print(d['cars'][1])
# print(d.get('cars')[1]   )
# # TO DISPLAY ALL MOBILE NAMES;;
# for mobile in d['Mobiles']:
#     print(mobile)

#MINI PROJECT IMPLEMENTATION OF SUPERMARKET DICTIONARY;;
# supermarket = {
#     'Store1': {
#         'name': 'Durga general store',
#         'items': [
#             {'name': 'soap', 'quantity': 20},
#             {'name': 'brush', 'quantity': 30},
#             {'name': 'paste', 'quantity': 40}       
#         ]
#     },

#     'Store2': {
#         'name': 'Sunny book store',
#         'items': [
#             {'name': 'Python', 'quantity': 5},
#             {'name': 'Django', 'quantity': 15},
#             {'name': 'Devops', 'quantity': 20}
#         ]
#     }
# }

# print(supermarket)
# TO PRINT THE NAME OF STORE1;;
# print(supermarket['Store1']['name'])

# TO PRINT NAMES OF ALL ITEMS PRESENT IN STORE1;;
# print(supermarket['Store1']['items'])
# for d in supermarket['Store1']['items']:
    # print(d['name'])

# HOW MANY DJANGO BOOKS ARE AVAILABLE;;
# for d in supermarket['Store2']['items']:
#     if d ['name']=='Django':
#         print('the number of Django books = ',d['quantity'])