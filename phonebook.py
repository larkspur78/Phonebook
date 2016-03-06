dictionary = {
    'chris': {'name': 'Chris', 'phone': "503-277-1234"},
    'sam': {'name': 'Sam', 'phone': "503-277-4321"}
}

def main():
    print("Welcome to the Phone Book!")
    while True:
        print("-" * 40)
        print("Press 1 to search.")
        print("Press 2 to add.")
        print("Press 3 to change an entry.")
        print("Press 4 to remove.")
        print("Press 5 to exit.")
        print("-" * 40)
        try:
            choice = int(input('> '))
            if choice == 1:
                search()
            if choice == 2:
                add()
            if choice == 3:
                change()
            if choice == 4:
                remove()
            if choice == 5:
                exit()
        except ValueError:
            print("That is not a valid entry. Please try again.")

def search():
    name = input("Please enter the name you are searching for: ").lower()
    try:
        print(dictionary[name]["name"])
        print(dictionary[name]["phone"])
    except KeyError:
        print("Unable to find this entry")


def add():
    name = input("Add a new name to the phonebook: ")
    phone = input("Add a phone number: ")
    dictionary[name.lower()] = {"name": name, "phone": phone}
    #print(dictionary[name.lower()]["name"])
    #print(dictionary[name.lower()]["phone"])
    print("The new name {name} and the new number {phone} have been added to your phonebook".format(name=name, phone=phone))

def change():
    name = input("To change an entry in your phonebook, first enter the name you wish to change: ")
    try:
        print(dictionary[name]["name"])
        print(dictionary[name]["phone"])
        confirm = input("Are you sure you wish to change this entry permanently? Yes or No: ").lower()
        if confirm == "yes" or confirm == "y":
            del(dictionary[name])
            new_name = input("Enter the new name: ")
            new_phone = input("Enter the new phone number: ")
            dictionary[new_name.lower()] = {"name": new_name, "phone": new_phone}
            print("The new name {new_name} and the new number {new_phone} have been successfully stored in your phonebook".format(new_name=new_name, new_phone=new_phone))

    except KeyError:
        print("Unable to find this entry")




def remove():
    name = input("To delete an entry in your phonebook, first enter the name you wish to delete: ")

    try:

        print(dictionary[name]["name"])
        phone = dictionary[name]["phone"]
        print(phone)
        confirm = input("Are you sure you wish to delete this entry permanently? Yes or No: ").lower()
        if confirm == "yes" or confirm == "y":
            del(dictionary[name])
        print("The name {name} and the number {phone} have been deleted permanently from your phonebook".format(name=name, phone=phone))

    except KeyError:
        print("Unable to find this entry")

main()
