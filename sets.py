# SETS IN PYTHON;;
# s={10,20,30,40}
# print(type(s))

# s={2,3,45,"khushbu"}
# s.add(30)
# print(s)

# CREATION OF SETS;;
# s={1,2,3,4,5}
# print(type(s))

# list=[1,2,3,4,5,6,7,8,9,10]
# s=set(list)
# print(s)
# print(type(s))

# set={}
# print(type(set))

# s=set()
# print(type(s))

# IMPORTANT FUNCTIONS FOR SETS;;(ADD,UPDATE,COPY,POP,REMOVE,DISCARD,CLEAR)
# s={10,20,30}
# s.add(100)
# s.add(1000)
# print(s)

# s={10,20,30}
# list=[1,2,4]
# s.update(list)
# print(s)
# s.update(range(5))
# print(s)

# s1={10,20,30}
# s2=s1.copy()
# print(s2)
# print(s1)

# s={10,20,30}
# print(s)
# print(s.pop())
# print(s)

# s={10,20,30,40}
# print(s.remove(10))
# print(s)
# print(s.remove(100))

# s={10,20,30,40}
# s.discard(10)
# print(s)
# print(s.discard(100))
# print(s)

# s={10,20,30,40}
# s.clear()
# print(s)

# ADD VS UPDATE;;
# s={10,20,30,40,50}
# s.add(5000)
# print(s)

# s={10,20,30,40,50}
# list=[500,60,700]
# s.update(list)
# print(s)

# s=set()
# s.update(range(1,10,2),range(0,10,2))
# print(s)

# MATHEMATICAL OPERATIONS FOR SETS(union,intersection,differnce);;
# s1={1,2,3,4,5}
# s2={6,7,8,9}
# print(s1.union(s2))
# print(s1|s2)

# s1={1,2,3,4,5}
# s2={2,6,7,1}
# print(s1.intersection(s2))
# print(s1&s2)

# s1={1,2,3,4}
# s2={2,6,7,1}
# print(s1.difference(s2))
# print(s1-s2)

# Programming Lab - 29 ;; page -481;;
# 1.  WAP to eliminate duplicates present in the list? 
# l=[10,20,30,40,10,20,10]
# print(l)

# s=set(l)
# print(s)

# l=list(s)
# print(l)

# 2.  WAP to print different vowels present in the given word?
# str=input("enter any string:")
# mydict={}
# vow=['a','e','i','o','u']
# for char in str:
#     if(char in vow):
#         c=str.count(char)
#         mydict.update({char:c})

# for keys,values in mydict.items():
#     print(f"{keys} present in string {values} times")