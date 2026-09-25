# def greatest(a, b, c):
#     if a > b and a > c:
#         print(a, "is largest")
#     elif b > a and b > c:
#         print(b, "is largest")
#     else:
#         print(c, "is largest")

# a = int(input())
# b = int(input())
# c = int(input())

# greatest(a, b, c)
# celcius to farrenheight
def convo(a, x):
    if a == 1:          # Celsius to Fahrenheit
        y = (9 * x) / 5 + 32
        return y
    elif a == 2:        # Fahrenheit to Celsius
        y = 5 * (x - 32) / 9
        return y
    else:
        return "Invalid choice"

a = int(input("Enter 1 for C to F and 2 for F to C: "))
x = int(input("Enter temperature: "))

print(convo(a, x))

