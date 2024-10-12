def show_menu(): #print menu with available options
    MENU = """
    Commands for use:
        help -- show available commands
        all -- show all phones in address book
        add [name] [phone] -- add new record
        change [name] [phone] -- change phone number for user with name [name]
        phone [name] -- show phone for user with name [name]
        close or bye -- exit from program
    """
    print(MENU)


def validate_count_arguments(args, expected_count = 2): #simple argument count validator
    if len(args) != expected_count:
        print(f"Please pass {expected_count} arguments")
        return False
    return True


def show_all_records(address_book):
    if not address_book: #if empty
        print("Address book is empty, add some records first")
        return

    for name, phone in address_book.items():
        print(f"{name}: {phone}")


def add_contact(address_book, args):
    if not validate_count_arguments(args): #check count of args
        return
    
    name, phone = args
    if name in address_book: #if name already in book
        print(f"Phone for user {name} already in book? if you want to change number use `change [name] [phone] command`")
    else:
        address_book[name] = phone
        print("Contact added")


def change_contact(address_book, args):
    if not validate_count_arguments(args):
        return
    
    name, phone = args
    if name in address_book:
        address_book[name] = phone
        print("Contact changed")
    else:
        print(f"There is no record for user {name}")


def show_phone(address_book, args):
    if not validate_count_arguments(args,1):
        return
    
    name = args[0]
    if name in address_book:
        print(f"{name} phone id {address_book[name]}")
    else:
        print(f"There is no record for user {name}")