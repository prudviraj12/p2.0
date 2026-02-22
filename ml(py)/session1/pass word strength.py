password = input("Enter your password: ")

score = 0


if len(password) >= 8:
    score += 1


if any(c.isupper() for c in password):
    score += 1

if any(c.islower() for c in password):
    score += 1


if any(c.isdigit() for c in password):
    score += 1


special_chars = "!@#$%^&*()-_+=<>?/{}[]"
if any(c in special_chars for c in password):
    score += 1

if score <= 2:
    print("Password Strength: Weak")
elif score == 3 or score == 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")