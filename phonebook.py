##python
# phonebook.py

# Step 2: Initialize the phonebook as an empty dictionary
phonebook = {}

# Step 3: Define a function to display the menu
def display_menu():
    print("\nPhonebook Menu:")
    print("1. Add New Contact")
    print("2. Search for a Contact")
    print("3. Delete a Contact")
    print("4. List All Contacts")
    print("5. Exit")

# Step 4: Implementing CRUD Operations

# Add a new contact
def add_contact():
    name = input("Enter the contact's name: ").capitalize()
    if name in phonebook:
        print(f"{name} already exists in the phonebook.")
    else:
        phone = input(f"Enter {name}'s phone number: ")
        phonebook[name] = phone
        print(f"{name} added successfully!")

# Search for a contact
def search_contact():
    name = input("Enter the name to search: ").capitalize()
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}")
    else:
        print(f"{name} not found in the phonebook.")

# Delete a contact
def delete_contact():
    name = input("Enter the name to delete: ").capitalize()
    if name in phonebook:
        del phonebook[name]
        print(f"{name} has been deleted.")
    else:
        print(f"{name} not found in the phonebook.")

# List all contacts
def list_contacts():
    if phonebook:
        print("\nPhonebook Entries:")
        for name, phone in phonebook.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("The phonebook is empty.")

# Main function to handle the menu and user actions
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            list_contacts()
        elif choice == '5':
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Step 5: Run the application
if __name__ == "__main__":
    main()