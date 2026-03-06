email = input("Enter email ID: ")
if email == "":
    print("Email ID cannot be empty.")
elif email.count("@") != 1:
    print("Invalid Email ID")
elif email.startswith("@") or email.endswith("@"):
    print("Invalid Email ID")
else:
    username, domain = email.split("@")
    if "." not in domain:
        print("Invalid Email ID")
    elif domain.startswith(".") or domain.endswith("."):
        print("Invalid Email ID")
    else:
        print("Valid Email ID")