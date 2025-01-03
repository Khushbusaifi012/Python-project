# n=int(input("enter no of rows = "))     #* * *
# for i in range(n):
#     print(" * ",end="")

# n=int(input("enter no of rows = "))    # * * * 
# for i in range(n):                     # * * * 
#     for j in range(n):                 # * * * 
#        print(" * ",end=" ")
#     print()

# n=int(input("enter no of rows = "))    #A A A A
# for i in range(n):                     #A A A A  
#     for j in range(n):                 #A A A A
#         print(" A ",end="")
#     print()
        
# n=int(input("enter no of rows = "))          #1 1 1 1 
# for i in range(n):   #for every row          #2 2 2 2
#     for j in range(n):   #for every column   #3 3 3 3
#         print(i+1, end=" ")  
#     print() 

# n=int(input("enter no of rows = "))    #A A A
# for i in range(n):                     #B B B 
#     for j in range(n):                 #C C C
#         print(chr(65+i),end=" ")
#     print()
          
# n=int(input("enter no of rows = "))  #1 2 3 4 5
# for i in range(n):                   #1 2 3 4 5   
#     for j in range(n):               #1 2 3 4 5
#         print(j+1,end=" ")
#     print()

# n=int(input("enter no of rows = "))     #5 4 3 2 1
# for i in range(n):                      #5 4 3 2 1
#     for j in range(n):               
#         print(n-j,end=" ")
    # print()
                
# n=int(input("enter no of rows = "))     #*  
# for i in range(n):                      #* * 
#     for j in range(i+1):                #* * *
#         print(" * ",end=" ")            #* * * *
#     print()

# n=int(input("enter no of rows = "))   #5   
# for i in range(n):                    #5 4
#     for j in range(i+1):              #5 4 3
#         print(n-j,end=" ")            #5 4 3 2 
#     print()

# n=int(input("enter no of rows = "))         
# for i in range(n):                                     
#         print("  "*(n-i-1),end=" ")            
#         print(' *'*(i+1))
        
# n=int(input("enter no of rows = "))         
# for i in range(n):                                     
#         print(" "*(n-i-1),end=" ")            
#         print('* '*(i+1))

# n=int(input("enter a rows = "))
# for i in range(n):
#     print(" "*(n-i-1),end=" ")
#     print('* '*(i+1))