# # print("hi")
# # print("hello")
# # print("hey")
# # def greet():
# #     print("greetings!") 
# # greet()
# # WAP to check if a number entered by the user is odd or even.

# num = int(input("Enter a number: "))
# if num %2 == 0:
#     print(num,"is even number")
# else:
#     print(num,"is odd")
# WAP to find the greatest of 3 numbers entered by the user
# a=int(input("num1:"))
# b=int(input("num2:"))
# c=int(input("num3:"))
# if(a>b and a>c):
#     print(a,"is higheset")
# elif(b>a and b>c):
#     print(b,"is highest")
# else:
#     print(c,"is highest")
# # WAP to c
# # A
# heck
# p
# if a number is a multiple of 7 or not.
# n=int(input("enter a number:"))
# if(n%7==0):
#     print(n,"is a multiplle")
# else:
#     print(n,"is not a multiple")
# lists and its some appli
# red=[1,2,3,4,5]
# # red[1:3]
# print(red)
# # red.
# red.sort(reverse=True)
# print(red)
# red.insert(0,7)
# print(red)
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list
# stu=["ranam","rangam","raju"]
# print(stu)
# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# [1, 2, 3, 2, 1] [1,
# “abc”
# ,
# “abc”
# , 1]
# stu=["reddy","reddy"]
# if(stu.reverse==stu):
#     print("palindrome")
# else:
#     print("not a palindrome")
# stu=["red","red"]
# rev=stu.copy()
# rev.reverse()
# if(stu==rev):
#     print("palindrome")
# else:
#     print("not a palindrome")
# tup=("C","A","B","A","K","D","C","C")
# tup.count("C")
# print(tup.count("C"))
# tup=["C","A","B","A","K","D","C","C"]
# tup.sort()
# print(tup)
# dict={
#     "stu":"reddy"
# }

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class sll:
#     def __init__(self):
#         self.head=None
    
#     def dis(self):
#         if self.head is None:
#             print("list is empty")
#         temp=self.head
#         while temp.next is not None:
#             print(temp.data,"-->",end="")
#             temp=temp.next
#         print("None")
# l=sll()
# n=node(10)
# n1=node(20)
# n2=node(30)
# l.head =n
# n.next=n1
# n1.next=n2
# l.dis()
    
    
    
    
# . Create a list of numbers and print the sum of all elements.
# l=[1,2,3,4]
# r=0
# for i in range(len(l)):
#     r=r+l[i]
# print(r)
# Find the largest number in a list (don’t use max() yet).
# l=[1,2,3,4,5]
# mar=l[0]
# for i in range (len(l)):
#     if(mar<l[i]):
#         mar=l[i]
        
# print(mar)
# Reverse a list without using reverse().
# l=[1,2,3,4,5]
# r=l[::-1]
# print(r)
# Given a string, count how many vowels are in it.
# s=input("enter a string:")
# s=s.lower()
# r=0
# for i in range(len(s)):
#     if(s[i] in 'aeiou'):
#         r += 1
# print(r)        
# 5. Reverse a string using a loop.
# s=input('enter the string:')
# r=''
# for i in range(len(s)-1,-1,-1):
#     r=r+s[i]
# print(r)
# s = input('enter the string: ')
# r = ''

# for ch in s:
#     r = ch + r

# print(r)

# Check if a string is a palindrome.
# s= input()
# r=s[::-1]
# if(s==r):
#     print("palindrome")
# else:
#     print("none")
# Count frequency of each character in a string.
# Example: "apple" → {'a':1,'p':2,'l':1,'e':1}
# s=input("enter a string:")
# freq={}
# for ch in s:
#     if(ch not in freq):
#         freq[ch]=1
#     else:
#         freq[ch]+=1
# print(freq)    
# Remove duplicate elements from a list using a set.
# Q10. Find common elements between two lists.
for  i in range (1,101,1):
    print(i ,end=" ")