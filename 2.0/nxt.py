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
# for  i in range (1,101,1):
#     print(i ,end=" ")
# hello=100
# if hello==100 :
#     print("hello x10")
# else: 
#     print("none")
# for i in range (1,6):
#     if i==3:
#         continue
#     print(i)

#n=int(input("enter a number :"))
#for i in range(n,0,+2):
#    print(i,end=" ")
# n=int(input("enter a number :"))
# for i in range(2,n+1,2):
#     print(i ,end="")
# Given a list of numbers, print each element on a new line.
# l = []

# n = int(input())

# for i in range(n):
#     x = int(input())
#     l.append(x)

# for i in l:
#     print(i)
# a="hello world"
# b="world"
# if b in a:
#     print("sub")
# else:
#     print("not a sub")  
# p1=0
# p2=1
# print(p1)
# print(p2)
# for i in range (3):
#     new=p1+p2
#     print(new)
#     p1=p2
#     p2=new

# n = int(input())
# l = []

# for i in range(n):
#     l.append(int(input()))

# mod=l[0]
# for i in range(len(l)):
#     if mod<l[i]:
#         new=mod
#     else:
#         pass
# print(new)

# my_array=list(map(int,input().split()))
# n = len(my_array)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if my_array[j] > my_array[j+1]:
#             my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

# print("Sorted array:", my_array)
# my_array = list(map(int, input("Enter numbers separated by space: ").split()))

# n = len(my_array)

# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if my_array[j] > my_array[j + 1]:
#             my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]

# print("Sorted array:", my_array)        
# import random
# print("-----NUMBER GAME ----")
# print("select the difficultyy")
# print("1.EASY")
# print("2.MEDIUM")
# print("3.HARD")

# choice=int(input("enter a num between 1 to 3:"))
# if choice==1:
#     start=1
#     end=10
#     atempts=5
# elif choice==2:
#     start=1
#     end=50
#     atempts=7
# elif choice==3:
#     start=1
#     end=100
#     atempts=10
# else:
#     print("number greater than 3",end=''"GAME OVER")
#     exit()
# num=random.randint(start,end)  
# print("guess the num between ",start,"and",end)
# while atempts>0:
#     print("Attempts left:", atempts)
#     guess=int(input())
#     if num>guess:
#         print("TOO LOW ")  
#     elif num<guess:
#         print("TOO HIGH")
#     else:
#         print("you won") 
#         score=atempts*20
#         print("your score :",score)
#     atempts-=1
    
# if atempts==0:
#     print("game over u can even win this simple game")


# try:
#     password = input().strip()
# except EOFError:
#     password = ""
# if password == "":
#     print("Password cannot be empty.")
# else:
#     has_upper = any(c.isupper() for c in password)
#     has_lower = any(c.islower() for c in password)
#     has_digit = any(c.isdigit() for c in password)
#     has_special = any(not c.isalnum() for c in password)
#     if len(password) < 6:
#         strength = "Weak"
#     elif len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
#         strength = "Strong"
#     else:
#         strength = "Medium"
#     print(f"Password Strength: {strength}")
# try:
#     password=input().strip()
# except EOFError:
#     password=""
# if password=="":
#     print("Password cannot be empty.")
# else:
#     upper=any(c.isupper() for c in password)
#     special=any ( not c.isalnum() for c in password)
# students = {}
# while True:
#     try:
#         choice = input().strip()
#     except:
#         break
#     if choice == "1":
#         name = input().strip()
#         if name in students:
#             print("Student already exists.")
#         else:
#             students[name] = "Absent"
#             print("Student added successfully.")
#     elif choice == "2":
#         name = input().strip()
#         if name not in students:
#             print("Student not found.")
#         else:
#             status = input().strip()
#             if status == "P":
#                 students[name] = "Present"
#                 print("Attendance marked as Present.")
#             elif status == "A":
#                 students[name] = "Absent"
#                 print("Attendance marked as Absent.")
#             else:
#                 print("Invalid input.")
#     elif choice == "3":
#         if not students:
#             print("No attendance records.")
#         else:
#             for name in students:
#                 print(f"{name} : {students[name]}")
#     elif choice == "4":
#         if not students:
#             print("No attendance data.")
#         else:
#             total = len(students)
#             present = sum(1 for s in students.values() if s == "Present")
#             absent = total - present
#             print(f"Total Students : {total}")
#             print(f"Present        : {present}")
#             print(f"Absent         : {absent}")
#     elif choice == "5":
#         print("Program ended.")
#         break
total = 0

while True:
    print("----- Online Food Ordering System -----")
    print("1. Pizza - ₹200")
    print("2. Burger - ₹120")
    print("3. Sandwich - ₹100")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        break

    quantity = int(input("Enter quantity: "))

    if choice == 1:
        total += 200 * quantity
    elif choice == 2:
        total += 120 * quantity
    elif choice == 3:
        total += 100 * quantity
    else:
        print("Invalid choice")

    print("Current Total Bill: ₹", total)
    print()

print("Final Total Bill: ₹", total)
    