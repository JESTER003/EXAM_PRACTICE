### 1. ----------------------Adding value to dict ------------------

# dict1 = {}
# dict1["key1"]="Value1"
# dict1["key2"]=50
# dict1.update({"key3":54})
# print(dict1)

### 2 .------------------ raise error custom and built-in-------------

# def divide(a,b):
#     if b==0:
#         raise ZeroDivisionError("0 se nai Ho paega dost")
#     return a/b
 

# try:
#     ans = divide(5,10)
# except ZeroDivisionError as mye:
#     print("Error spotted :",mye)
# else:
#     print("Yout Ans is :",ans)

### 6 .------------------------- del keyword-------------------------

# lmain=["hii","hello","bye"]
# del lmain[1]
# print(lmain)

### 12 .------------------------ abstraction -------------------------

# class Bank:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdrawl(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Invalid Withdrawl amount or influence balance . check balance first")
#     def get_blc(self):
#         blc =f"Current Balance : {self.balance}"
#         print(blc)

# acc1 = Bank(5000)
# acc1.deposit(5500)
# acc1.withdrawl(11000)
# acc1.get_blc()


###------------------ Super keyword and utilzation--------------------- :

# class A:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print(self.name)

# class B(A):
#     def __init__(self,name,age):
#         self.age=age
#         super().__init__(name)

#     def show_age(self):
#         print(self.age)

# v1 = A("Abhi")
# # v1.show()
# v2=B("Sanjay",22)
# v2.show()
# v2.show_age()

### -------------------- Cursor object mysql ------------------ 

# my_connec = mysql.connector.connect(
#     host:"localhost",
#     user="username"
#     password="your_password"
#     databae="db_name"
# )

# cursor_obj = my_connec.cursor()
# cursor_obj.execute("SELECT * from table_name")
# result = cursor_obj.fetchall()

# for row in result:
#     print(row)

# cursor_obj.close()
# my_connec.close()    

### --------- shallow copy and deepcopy difference --------------

# import copy

# old_l=[[1,2,3],[4,5,6],["a","b","c"]]
# ## new_l=old_l.copy()
# new_l=copy.copy(old_l)
# new_l[0][0]=4
# print(old_l)
# print(new_l)

# print("\n")

# old_l=[[1,2,3],[4,5,6],["a","b","c"]]
# new_l=copy.deepcopy(old_l)
# new_l[0][0]=4
# print(old_l)
# print(new_l)

###############################################################
# 1. What will be the output of the following program? 
# L = list('123456')  
# L[0] = L[5] = 0 
# L[3] = L[-2]  
# print(L) 

# tuple1 = (1, 2, 4, 3)  
# tuple2 = (1, 2, 3, 4)  
# print(tuple1 == tuple2)
###############################################################

### -------------------------- password generator from length--------------------------

import random
def password_generator(length):
    # choices=['1234567890!@#$%^&*()+abcdefghijklmnopqrstuvwxyzASDFGHJKLQWERTYUIOPZXCVBNM']
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = lowercase_letters.upper()
    digits = "0123456789"
    special_chars = "!@#$%^&*()"

  # Combine character sets based on user preference (modify as needed)
    all_chars = lowercase_letters + uppercase_letters + digits   
    password=""
    password = "".join(random.sample(all_chars,length))
    return password

ans=password_generator(15)
print(ans)

### -------------------------- Prime Numbers check  ----------------------------------

# def prime(num):
#     if num<2:
#         return False
    
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#     return True

# ans = 10
# print (f"Prime numbers till {ans} : " )
# for i in range(2,ans+1):
#     if prime(i):
#         print(i,end=" ")


### -------------------------- Palindrome (slicing) ---------------------------

# def palindrome1(word):
#     return word==word[::-1]

# wd = 'racecar'
# if palindrome1(wd):
#     print(f"yes {wd} is palindrome")
# else:
#     print("it's not")    

## -- without slicing --

# def palindrome2(word):

#     cleaned_text = "".join(char.lower() for char in word if char.isalnum())
#     original = cleaned_text
#     reversed_text = ""

#     for char in original:
#         reversed_text = char + reversed_text

#     return original == reversed_text        

# wd = 'racecar'
# if palindrome2(wd):
#     print(f"yes {wd} is palindrome")
# else:
#     print("it's not")  

########################################################################################## 

s1="----------parul-university-------------"
s2=s1.find("p")
print(s2)


def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True        

n1=15
print("Ans : ")
for i in range(2,n1+1):
    if prime(i):
     print(i)

# ans = 10
# print (f"Prime numbers till {ans} : " )
# for i in range(2,ans+1):
#     if prime(i):
#         print(i,end=" ")
    

##################################################################3 

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db=client["mydb"]
collection=client["mycollection"]

result = collection.insert_one({})
read = collection.find_one({"name":"john"})
result= collection.update_one({})
 