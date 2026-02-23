# food={}
# while True:
#     print("-----ONLINE FOOD ORDERING SYSTEM-----")
#     print("1.Pizza - $200")
#     print("2.combo - $5000")
#     print("3.burger - $100")
#     print("Exit")
#     choice=int(input("choose the food item:"))
#     if choice==1:
#         n=int(input("enter quantity:"))
#         food["pizza"]=n
#         print("added item succesfully")
#         prise=200*n
#         print("total amount:",prise)
#     elif choice==2:
#         c=int(input("enter quantity:"))
#         food["combo"]=c
#         print("added item succesfully")
#         prise1=5000*c
#         print("total amount:",prise1)
#     elif choice==3:
#         b=int(input("enter quantity:"))
#         food["burger"]=c
#         print("added item succesfully")
#         prise_2 =100*b
#         print("total amount:",prise_2)
#     else:
        
#         print("exisiting")
#         break
# total=prise+prise1+prise_2
# print("total budget for food:",total)     
    
    
    
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

