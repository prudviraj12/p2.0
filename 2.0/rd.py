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

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    