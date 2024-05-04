def parse_input(user_input):
    # Розбиваємо введений рядок на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # Перетворюємо команду на нижній регістр
    return cmd, args

def add_contact(contacts, name, phone):
    # Додаємо контакт до словника контактів
    contacts[name] = phone
    print("Contact added.")

def change_contact(contacts, name, phone):
    # Змінюємо номер телефону контакту
    if name in contacts:
        contacts[name] = phone
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(contacts, name):
    # Показуємо номер телефону за іменем
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def show_all(contacts):
    # Показуємо усі контакти
    print("Contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    contacts = {}  # Словник для зберігання контактів

    print("Welcome to the assistant bot!")
    print("Commands:")
    print("add [name] [phone] - Add a contact")
    print("change [name] [new_phone] - Change contact's phone number")
    print("phone [name] - Show phone number for a contact")
    print("all - Show all contacts")
    print("exit/close - Exit the program")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "add" and len(args) == 2:
            add_contact(contacts, args[0], args[1])
        elif command == "change" and len(args) == 2:
            change_contact(contacts, args[0], args[1])
        elif command == "phone" and len(args) == 1:
            show_phone(contacts, args[0])
        elif command == "all" and len(args) == 0:
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
