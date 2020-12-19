"""
CS3A, Assignment #9, Contact List Pt 1
Lily Swedlow
"""

import csv
# filename = "contacts.csv"


class Sorter:
    # TODO part 2: change whatever's necessary to sort by first/last name

    @staticmethod
    def float_largest_to_top(lst, size):
        swapped = False
        for i in range(size - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        return swapped

    @staticmethod
    def sort(lst, by):
        size = len(lst)
        while Sorter.float_largest_to_top(lst, size):
            size -= 1


class Contact:
    """
    This class represents a single contact (one person)
    """
    def __init__(self, first_name, last_name, email=None, phone=None):
        """
        This is the initializer for Contact class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def __str__(self):
        """
        Return a str that that shows all contact info
        """
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Email: {self.email}\n"
                f"Phone: {self.phone}\n")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if type(first_name) != str:
            raise TypeError("Invalid first name, should be str")
        if len(first_name) == 0:
            raise ValueError("First name cannot be empty")
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if type(last_name) != str:
            raise TypeError("Invalid last name, should be str")
        if len(last_name) == 0:
            raise ValueError("Last name cannot be empty")
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if type(email) != str and type(email) is not None:
            raise TypeError("Invalid email, should be str")
        if "@" not in email:
            raise ValueError("Email must contain '@'")
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if type(phone) != str and type(phone) is not None:
            raise TypeError("Invalid phone, should be str")
        if int(phone) > 0:
            raise ValueError("Phone must be positive")
        self._phone = phone


class ContactList:
    """
    This class stores multiple contacts.
    """
    BY_FIRST_NAME = 1  # sort/find by first name
    BY_LAST_NAME = 2  # sort/find by last name

    def __init__(self):
        """
        Creates a list of contacts, and also dict's that associated contacts with
        first names and last names
        """
        self._contacts = []

        # TODO part 2: add any necessary code to help search by first/last name

    def clear(self):
        """
        Clear/remove all contacts
        :return:
        """
        self._contacts.clear()

        # TODO part 2: add any necessary code to clear all contacts

    @property
    def contacts(self):
        return self._contacts

    def add(self, contact):
        if type(contact) != Contact:
            raise TypeError("Invalid contact")
        self._contacts.append(contact)

        # TODO part 2: add any necessary code to enable search by first/last name

    def find(self, name, by):
        """
        Find a contact by the given name
        :param name: the first/last name of the contact to lookup, depend on by
        :param by: if BY_FIRST_NAME, name should be interpreted as the first name
                   if BY_LAST_NAME, name should be interpreted as the last name
        :return: an instance of Contact, the first_name/last_name attribute of which
                 matches name; if no match, returns None
        """
        # TODO part 2: add any necessary code to enable search by first/last name

    def __str__(self, by=BY_FIRST_NAME):
        """
        Return a str that contains all contact, sorted by first names or
        last name, depending on the "by" parameter.
        It raises a ValueError if the "by" parameter contains invalid value.
        """
        contact_list = self._contacts
        sep = "\n"
        all_my_contacts = sep.join([str(contact) for contact in contact_list])
        return f"{all_my_contacts}"

        # TODO part 2: add any necessary code to handle sorting by first/last name


def get_choice():
    """
    Repeatedly prompts the user for an integer until they do so.
    :return: An integer choice.
    """
    while True:
        try:
            choice = int(input(
                "\n"
                "****** Contact List ******\n"
                "Please choose from the following actions:\n"
                "  1. Load contacts from file\n"
                "  2. Print all contacts, sorted by first name\n"
                "  3. Print all contacts, sorted by last name\n"
                "  4. Search all contacts by first name\n"
                "  5. Search all contact by last name\n"
                "  6. Quit\n"
                "Please enter your choice: "))
            return choice
        except:
            print("Invalid input")


def line_to_contact(line):
    fields = [f.strip() for f in line.split(",")]
    try:
        if len(fields) < 2:
            raise Exception("Invalid line of code.")
        first_name = (fields[0])
        last_name = (fields[1])
        email = (fields[2])
        phone = int(fields[3])
        return Contact(first_name, last_name, email, phone)
    except:
        print("File input is missing data.")


def load_contacts_from_file(contact_list, filename):
    with open(filename) as file:
        file = csv.reader(file, delimiter=',')
        for line in file:
            try:
                contact_list.add(line_to_contact(line))
            except:
                pass


def load_contacts(contact_list):
    """
    Prompts the user for the name of a file, and load contact from that file.
    """
    filename = input("Enter the name of the file to load: ")
    contact_list.clear()
    try:
        load_contacts_from_file(contact_list, filename)
        if type(filename) != str:
            raise TypeError("Invalid filename, should be str")
        print("Loaded {} contacts from {}".format(len(contact_list.contacts), filename))
    except Exception:
        print(f"Problem loading contacts: [Errno 2] No such file or directory: {filename}")


def print_by_first_name(contact_list):
    print("\n" + contact_list.__str__(ContactList.BY_FIRST_NAME))


def print_by_last_name(contact_list):
    print("\n" + contact_list.__str__(ContactList.BY_LAST_NAME))


def find_contact(contact_list, by):
    name = input("Please enter the name to search: ")
    contact = contact_list.find(name, by)
    print("\n" + str(contact))


def find_by_first_name(contact_list):
    find_contact(contact_list, ContactList.BY_FIRST_NAME)


def find_by_last_name(contact_list):
    find_contact(contact_list, ContactList.BY_LAST_NAME)


def quit(contact_list):
    """
    Do cleanup and exit program; ok to use exit() in this function in this assignment.
    :param contact_list:
    :return: (Never, because it exits the program)
    """
    print("Bye!")
    exit(0)


def main():
    contact_list = ContactList()

    while True:
        choice = get_choice()

        if choice == 1:
            load_contacts(contact_list)
        elif choice == 2:
            print_by_first_name(contact_list)
        elif choice == 3:
            print_by_last_name(contact_list)
        elif choice == 4:
            find_by_first_name(contact_list)
        elif choice == 5:
            find_by_last_name(contact_list)
        elif choice == 6:
            quit(contact_list)
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
