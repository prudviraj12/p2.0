# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not a prime number")
# else:
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime number")
#     else:
#         print("Not a prime number")n = int(input("Enter the number of terms: "))

# a, b = 0, 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
    
# class Solution:
#     def resultArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         arr1 = []
#         arr2 = []

#         arr1.append(nums[0])
#         arr2.append(nums[1])

#         for i in range(2, n):
#             if arr1[-1] > arr2[-1]:
#                 arr1.append(nums[i])
#             else:
#                 arr2.append(nums[i])
        
#         return arr1 + arr2n = int(input("Enter a number: "))

square = n * n
sum_digits = 0

while square > 0:
    digit = square % 10
    sum_digits += digit
    square //= 10

if sum_digits == n:
    print(n, "is a Neon Number")
else:
    print(n, "is not a Neon Number")
    