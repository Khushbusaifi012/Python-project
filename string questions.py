# QUESTION-1 WRITE A PROGRAM TO REVERSE THE GIVEN STRING?
# s=input("enter a string = ")
# print(s[::-1])

# SECOND METHOD;;
# s=input("enter a string  = ")
# r=reversed(s)
# output=''.join(r)
# print(output)

# THIRD METHOD;;
# s=input("enter a string  = ")
# i=len(s)-1
# target=''
# while(i>=0):
#     target=target+s[i]
#     i=i-1
# print(target)

# QUESTION-2 PROGRAM TO REVERSE ORDER OF WORDS?
# s=input("enter a string  = ")
# l=s.split()
# print(l)
# l1=[]
# i=len(l)-1
# while(i>=0):
#     l1.append(l[i])
#     i=i-1
# print(l1)
# output=' '.join(l1)
# print(output)

# QUESTION-3 WRITE A PROGRAM TO REVERSE INTERNAL CONTENT OF EACH WORD?
# s=input("enter a string  = ")
# l=s.split()
# print(l)
# l1=[]
# for x in l:
#     l1.append(x[::-1])
# print(l1)
# output=" ".join(l1)
# print(output)

# QUESTION-4 WRITE A PROGRAM  TO PRINT CHARACTERS AT ODD POSITION AND EVEN POSITION FOR THE GIVEN STING?
# s=input("enter a string  = ")
# print('characters at even position = ',s[::2])
# print('characters t odd position = ',s[1::2])

# SECOND METHOD;;
# s=input("enter a string  = ")
# print('characters at even position = ')
# i=0
# while i<len(s):
#     print(s[i],end=',')
#     i=i+2
# print()
# print('characters at odd position = ')
# i=1
# while i<len(s):
#     print(s[i],end=',')
#     i=i+2

# THIRD METHOD;;
# s=input("enter a string  = ")
# evens=[]
# odds=[]
# i=0
# while(i<len(s)):
#     if(i%2==0):
#         evens.append(s[i])
#     else:
#         odds.append(s[i])
#     i=i+1
# print(evens)
# print(odds)

# QUESTION-5 WRITE A PROGRAM TO MERGE CHARACTERS OF TWO STRINGS INTO A SINGLE STRING BY TAKING CHARACTERS ALTERNATIVELY ?
# s1 = input("Enter the first string: ")
# s2 = input("Enter the second string: ")

# output = ""
# i, j = 0, 0

# # Use a loop that runs until all characters from both strings are processed
# while i < len(s1) or j < len(s2):
#     if i < len(s1):  # Check if there are characters left in s1
#         output += s1[i]
#         i += 1
#     if j < len(s2):  # Check if there are characters left in s2
#         output += s2[j]
#         j += 1
# print("Merged string:", output)

# QUESTION -6 WAP TO SORT CHARACTERS PRESENT IN THE GIVEN STRING FIRST ALPHABET SYMBOLS AND NUMERIC VALUES?
# s=input("enter a string  = ")
# s1=s2=''
# for x in s:
#     if x.isalpha():
#         s1=s1+x
#     else:
#         s2=s2+x
# output=''
# for x in sorted(s1):
#     output=output+x
# for x in sorted(s2):
#     output=output+x
# print(output)

# QUESTION-7 WAP TO DECODE A STRING GIVEN IN A FORMAT WHERE EACH LETTER IS REPEATED BASED ON THE NUMBER FOLLOWS IT?
# s=input("enter a string  = ")
# output=" "
# for x in s:
#     if x.isalpha():
#         ch=x
#     else:
#         output=output+ch*int(x)
# print(output)

# QUESTION-8 WAP TO DECODE A STRING WHICH IS CONVERTED WORD INTO NUMERIC INTO THEIR NUMERIC WORD TO ALPHABET?  ?
# s=input("enter a string  = ")
# output=""
# for x in s:
#     if x.isalpha():
#         ch=x
#     else:
#         newch=chr(ord(ch)+int(x))
#         output=output+ch+newch
# print(output)

# QUESTION-9 WAP TO PRINT REMOVE DUPLICATES CHARACTERS IN THE GIVEN STRING?
# s=input("enter a string  = ")
# l=[]
# for x in s:
#     if x not in l:
#         l.append(x)
# output="".join(sorted(l))
# output=output.replace('','')
# print(output)

# QUESTION-10 WAP TO PRINT FIND THE NUMBER OF OCCURENCES OF EACH CHARACTER PRESENT IN THE GIVEN STRING ?
# s=input("enter a string  = ")    
# d={}
# for x in s:
#     if x not in d:
#         d[x]=1
#     else:
#         d[x]=d[x]+1
# print(d)
# for k,v in d.items():
#     print('{} occurs {} times'.format(k,v))