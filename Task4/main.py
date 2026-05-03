def show_help():    #help function
    return (
        "Available commands:\n"
        "  hello                - greet the bot\n"
        "  add <name> <phone>   - add a new contact\n"
        "  change <name> <phone>- update existing contact\n"
        "  phone <name>         - show phone number\n"
        "  all                  - show all contacts\n"
        "  help                 - show this message\n"
        "  close / exit         - quit the bot"
    )


def parse_input(user_input):    #input parsing
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def validate_contact(name, phone):  #validation of adding Name and phone
    if not name.isalpha():
        return "Error: name must contain only letters."
    clean = phone.lstrip("+")
    if not clean.isdigit() or len(clean) < 10 or len(clean) > 12:
        return "Error: phone must contain only digits (from 10 to 12), optionally starting with '+'."
    return None



def add_contact(args, contacts):    #adding phone number to dict
    if len(args) !=2:
        return "Error: Not enough info. Phone or Name is missing"
    
    name, phone = args
    error = validate_contact(name, phone)
    
    if error:
        return error
    
    contacts[name] = phone
    return "Contact added."



def change_contact(args, contacts): #changing existing contact
    if len(args) != 2:
        return "Error: Not enough info. Phone or Name is missing."
    
    name, phone = args
    error = validate_contact(name, phone)
    
    if error:
        return error
    
    if name not in contacts:
        return f"Error: contact '{name}' not found."
    
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts): #showing existing contact
    if len(args) != 1:
        return "Error: give me a name please."
    
    name = args[0]

    if name not in contacts:
        return f"Error: contact '{name}' not found."
    
    return contacts[name]

def show_all(contacts): #show all contacts
    if not contacts:
        return "No contacts saved."
    
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "help":
                print(show_help())
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case _:
                print("Invalid command. Type help for command list")

if __name__ == "__main__":
    main()
