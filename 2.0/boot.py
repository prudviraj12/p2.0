# n=int(input("enter a number:"))
# tot=0
# for i in range (1,n+1):
#     tot+=i
# print(tot)0
# n= int(input())
# for i  in range(1,11):
#     print(n*i)
# n=int(input())
# c=0
# for i in range(1,n+1):
#     if i%2==0 and i%3==0:
#         c+=1
# print(c)a
# n=int(input())
# for digit in str(n):
#     print(digit,end =" ")

# s="pps"
# print(s[0:2])
# print(s[0:1])
# print(s[2:])
# print(s[0:3])

# s1='apple'
# s2='banana'
# s3="apple mandela"
# print(s1==s2)
# print(s1==s3)
# print(s1!=s2)
# print(s1>s2)
# print(s1>s3)
# print(id(s1))
# print(id(s3))
# print(s3>s1)
# main=" ilove mmm"
# sub="raj"
# new=main.replace("mmm","raj")
# print(new)
# s="py is easy"

# # words=s.split()
# # print(words)
# print(s.startswith("py"))
# print(s.lower())
# print(s.title())
# list=[]
# print(list)
# print(type(list))
# l=list(range(0,10,2))
# print(l)
# print(type(l))
# l=[10,20,30]
# print(l[0]>=10)
# f=["apple","banana"]
# f.insert(1,"cherry")
# print(f)
#  mop=l[0]
# mat=l[0]
# for num in l:
#     if num>mop:
#         mop=num
#     if num < mat:
#         mat=num
# print(mop)
# print(mat)
# l=[10,20,30,40,50,30,10,20,40]
# c=0
# for i in range (len(l)):
#     mop=l[i]

#     if l[i]==mop:
#         mop=l[i]
#         c+=1
# print(mop)
# l = [10,20,30,40,50,30,10,20,40]
# unique = []
# for num in l:
#     if l.count(num) == 1:
#         unique.append(num)
# print(unique)
# l=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5]
# pos=[]
# neg=[]
# for i in range(len(l)):
#     if l[i]>0:
#         pos.append(l[i])
#     if l[i]<0:
#         neg.append(l[i])
# print(pos)
# print(neg)
# l =list(map(int,input().split()))
# print(l)


# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return sum+sum(n-1)
# n=int(input())
# sum(n)    
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
