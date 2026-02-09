print("Hello there! Welcome to your personal Contact Manager.")
running = True
contact_list = []
while running:
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Update Contact")
    print("5. Delete Contacts")
    print("6. Exit program")

    choice = input("Choose an option: ").strip()

    if choice == "6":
        confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
        if confirm == "y":
            print("Goodbye, see you again soon!")
            running = False
    else:
        print(f"You chose option {choice}")

    if choice == "1":
        new_entry = input("Enter the name of the Person you want to add (First name & Last name)").strip().title()
        contact_list.append(new_entry)
        print(f"Added new contact")
    elif choice == "2":
        if not contact_list:
            print("No contacts found.")
        else:
            print("\nYour Contacts:")

            for item in contact_list:
                print(item)
    
    elif choice == "3":
        # input("Enter the name you are looking for?").find(contact_list) # Wrong logic
        # Searching must happen inside the list
        #.find() works on text, not lists
        # You need to compare the search term against each stored contact
        search = input("Enter the name you are looking for: ").strip().lower()
        found = False

        for item in contact_list:
            if search in item.lower():
                print("Contact found")
                print(item)
                found = True

        if not found:
            print("No matching contact found.")


    elif choice == "4":
        found = False
        old_entry = input("Which contact do you want to update?").strip().lower()
        update = input("Enter the name of the updated contact: ").strip().title()
        # Logic is wrong
        # item = value not position
        # you want to update the value by position
        #for item in contact_list:
           # if old_entry in item.lower():
           #     contact_list[item] = update
           #     print("Contact updated!")
           #     print(item)
            #    found = True
        for i in range(len(contact_list)):
            if old_entry in contact_list[i].lower():
                contact_list[i] = update
                print("Contact update!")
                found = True
                break
        if not found:
            print("Contact not found.")

    
    elif choice == "5": # Add confirmation before delete function
        found = False
        entry = input("Which contact do you want to delete?").strip().lower()
        for i in range(len(contact_list)):
            if entry in contact_list[i].strip().lower():
                confirm = input(f"Are you sure you want to delete {contact_list[i]} (y/n)")
                if confirm == "y":
                    del contact_list[i]
                    print("Contact Deleted.")
                    found = True
                    break
                else:
                    print("Action Canceled.")
                    found = True
                    break
        if not found:
            print("No matching contact found.")
