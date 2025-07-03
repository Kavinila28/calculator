contacts = {}

while True:
    print("\n1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit")
    choice = input("Choose: ")

    if choice == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Contact added.")
        
    elif choice == '2':
        for n, p in contacts.items():
            print(f"{n} - {p}")
        if not contacts:
            print("No contacts.")
        
    elif choice == '3':
        q = input("Search name or phone: ").lower()
        found = False
        for n, p in contacts.items():
            if q in n.lower() or q in p:
                print(f"{n} - {p}")
                found = True
        if not found:
            print("Not found.")
            
    elif choice == '4':
        name = input("Name to update: ")
        if name in contacts:
            contacts[name] = input("New phone: ")
            print("Updated.")
        else:
            print("Not found.")
            
    elif choice == '5':
        name = input("Name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Deleted.")
        else:
            print("Not found.")
            
    elif choice == '6':
        print("Closing the contact book!")
        break
    else:
        print("Invalid option.")
