# a = int(input("Enter Num 1 :"))
# b = int(input("Enter Num 2 :"))
# print("Result:", a * b)

#length
# a = "Navaj"
# len1=len(a)
# print("Length of a :",len1)

#indexing
# a = "navaj"
# ch = a[2] # ch = str[] # here str = navaj & indexing starts from 0 and from right side it starts from -1
# print(ch)

#or

# a = "navaj"
# print(a[0])

#slicing
# str = "navajmulla"
# slice = str[1:5]
# print(slice)

#or

# str = "navajmulla"
# print(str[1:5])
# print(len(str))
# print(str[-4:-1])


# To check list has plaindrome or not

# tou1=[1 ,2 ,1]
# tou2=[1 ,2 , 3, 3, 4 ,3 ,2 ,1]

# list_copy1= tou2.copy()
# list_copy1.reverse()

# if (list_copy1 == tou2):
#    print("palindrome")

# else:
#    print(" NOT palindrome")


# def identify(num):
#     if num == 0:
#         print("neither even nor odd ")
#     elif num % 2 == 0:
#         print("Even")
  
#     else:
#         print("odd")

# identify(3)

# def show(a):    #Recursion
#     if a==0:
#         return
#     print(a)
#     show(a-1)
#     print("End")

# show(5)


# def fact(n):
#     if (n == 1 or n == 0):  # Recursion2
#         return 1
#     return fact(n-1) * n

# print(fact(6))    

# def show(list,idx):
#     if idx == len(list):
#         return
#     print(list[idx])
#     show(list,idx+1)

# names = ["navaj", "mustakim", "ayesha", "ibrahim"]
# print(type(names))

# show(names,0)

# import os

# os.remove("new.txt")

# dict= {
#         "name" : "navaj",
#         "age" : "32",
#         "From" : "kolhapur",
#       }
# print(dict)

# print(type(dict))

# class account:
#      def __init__(self, bal, acc):
#           self.balance= bal
#           self.account_number= acc

#      def debit(self, amount):
#           self.balance -= amount
#           print("your account is debited by RS." , amount)
#           print("Your Total balance", self.get_balance())

#      def credit(self, amount):
#           self.balance += amount
#           print("your account is credited by RS." , amount)
#           print("Your Total balance", self.get_balance())

#      def get_balance(self):
#           return self.balance
     
# acc1=account(50000, 9545587200)
# acc1.debit(9500)
# acc1.credit(500)     

#calculator
# Number1=(int(input("Enter Number 1 = " )))
# operate=(input("Enter Operator(+ ,- ,* ,/) = "))
# Number2=(int(input("Enter Number 2 = ")))

# if operate== "+":
#      print(int(Number1 + Number2))
# elif operate== "-":
#      print(int(Number1 - Number2))
# elif operate== "*":
#      print(int(Number1 * Number2))     
# elif operate== "/":
#      if Number2 !=0:
#           print(int(Number1 / Number2))
#      else:
#           print("Error Division By Zero Is Not Allowed")
# else:
#      print("Please Enter Valid Opeartor Among +,-,*,/")

# def Con_Name(a,b):
#     return a + b

# s=Con_Name(5, 6)
# print(type(s))

# list=[12,24,36,48,60]
# lst=type(list)
# print(lst)
# l=len(list)
# print(l)
# idx=print(list[0])
# idx=print(list[4])
# print(list.index(36))


#swapping
# def swap_list(newlist):
#     l=len(newlist)
#     idx=newlist[0]
#     newlist[0] = newlist[l-1]
#     newlist[l-1]=idx
#     return newlist 
    
    
# g=swap_list([12,24,36,48,60])
# print(g)

import sys

# calculate size of touple
# touple1=(1,"a",2,"b",3,"c")
# touple2=(2,"b",3,"c",4,455,1,5,8,9,0,6,5)

# print("size of touple1 = " + str(sys.getsizeof(touple1)) + " bytes")
# print("size of touple2 = " + str(sys.getsizeof(touple2)) + " bytes")


#calculator
# Number1=int(input("Enter Number 1 = "))
# operator=input("Enter Operator(+,-,/,*) = ")
# Number2=int(input("Enter Number 2 = "))

# if operator== "+":
#     print(Number1 + Number2)
    
# elif operator== "-":
#     print(Number1 - Number2)

# elif operator== "*":
#     print(Number1 * Number2)

# elif operator== "/":
#     print(Number1 / Number2)

# else:
#     print("Enter Valid Opeartor")









          
                  
          
          





