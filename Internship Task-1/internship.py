import os
import json

# File to store contact data
CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            try:
                contacts = json.load(file)
            except json.JSONDecodeError:
                contacts = {}
    else:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=2)

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Exit")

def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")

    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully!")

def search_contact(contacts):
    name = input("Enter the name to search: ")
    contact = contacts.get(name)
    if contact:
        print("\nContact Information:")
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print(f"No contact found with the name '{name}'.")

def update_contact(contacts):
    name = input("Enter the name to update: ")
    if name in contacts:
        print("\nExisting Contact Information:")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        
        new_phone = input("Enter the new phone number (press enter to keep the existing one): ")
        new_email = input("Enter the new email address (press enter to keep the existing one): ")

        if new_phone:
            contacts[name]['phone'] = new_phone
        if new_email:
            contacts[name]['email'] = new_email

        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"No contact found with the name '{name}'.")

def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            save_contacts(contacts)
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
