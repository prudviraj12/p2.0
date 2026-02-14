contacts = {}

def add_contact():
    contact_id = str(len(contacts) + 1)

    first = input("Enter First Name: ")
    last = input("Enter Last Name: ")
    gender = input("Enter Gender: ")
    address = input("Enter Address: ")
    phone = input("Enter Phone Number: ")

    contacts[contact_id] = {
        "first_name": first,
        "last_name": last,
        "gender": gender,
        "address": address,
        "phone": phone
    }

    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    for cid, details in contacts.items():
        print(f"\nID: {cid}")
        for key, value in details.items():
            print(f"{key}: {value}")

def update_contact():
    cid = input("Enter Contact ID to update: ")

    if cid in contacts:
        contacts[cid]["first_name"] = input("Enter New First Name: ")
        contacts[cid]["last_name"] = input("Enter New Last Name: ")
        contacts[cid]["gender"] = input("Enter New Gender: ")
        contacts[cid]["address"] = input("Enter New Address: ")
        contacts[cid]["phone"] = input("Enter New Phone Number: ")

        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    cid = input("Enter Contact ID to delete: ")

    if cid in contacts:
        del contacts[cid]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

while True:
    print("\n----- Contact Management System -----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    match choice:
        case 1:
            add_contact()
        case 2:
            view_contacts()
        case 3:
            update_contact()
        case 4:
            delete_contact()
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid choice.")
