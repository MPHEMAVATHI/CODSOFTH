contacts = {}

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"  Phone: {details['Phone']}")
        print(f"  Email: {details['Email']}")
        print(f"  Address: {details['Address']}\n")

def search_contact():
    query = input("Enter name or phone to search: ").strip().lower()
    found = False
    for name, details in contacts.items():
        if query in name.lower() or query in details['Phone']:
            print(f"Found Contact: {name}")
            print(f"  Phone: {details['Phone']}")
            print(f"  Email: {details['Email']}")
            print(f"  Address: {details['Address']}\n")
            found = True
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print("Enter new details (leave blank to keep current):")
        phone = input(f"Phone ({contacts[name]['Phone']}): ").strip()
        email = input(f"Email ({contacts[name]['Email']}): ").strip()
        address = input(f"Address ({contacts[name]['Address']}): ").strip()
        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        if address:
            contacts[name]['Address'] = address
        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")

def menu():
    while True:
        print("\n==== Contact Book Menu ====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the Contact Book
menu()