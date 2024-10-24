from contacts import Contacts

def main_menu():
    print("\n      *** TUFFY TITAN CONTACT MAIN MENU \n" )
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list")
    print("5. Set contact filename")
    print("6. Exit the program")

def main():
    contact_list = Contacts()

    while True:
        main_menu()
        choice = input("\nEnter menu choice: ")

        if choice == '1':
            id = input("\nEnter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = contact_list.add_contact(id, first_name, last_name)
            print(result if result != "error" else "Phone number already exists.")

        elif choice == '2':
            id = input("\nEnter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = contact_list.modify_contact(id, first_name, last_name)
            print(result if result != "error" else "Phone number not found.")

        elif choice == '3':
            id = input("\nEnter phone number: ")
            result = contact_list.delete_contact(id)
            print(result if result != "error" else "Invalid phone number.")

        elif choice == '4':
            contact_list.print_contacts()

        elif choice == '5':
            filename = input("\nEnter new contact filename: ")
            result = contact_list.set_filename(filename)
            print(result)

        elif choice == '6':
            break

        else:
            print("\nInvalid choice.")

if __name__ == "__main__":
    main()
