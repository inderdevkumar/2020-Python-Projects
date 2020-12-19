class Sorter:
    """
    This is the bubble sort presented in lectures, the only difference is
    that the two functions are now static methods of a class.
    """

    @staticmethod
    def float_largest_to_top(lst, size, by):
        swapped = False
        for i in range(size - 1):
            if by == 2:
                if lst[i].last_name > lst[i + 1].last_name:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True
            else:
                if lst[i].first_name > lst[i + 1].first_name:
                    lst[i], lst[i+1] = lst[i+1],lst[i]
                    swapped = True
        return swapped

    @staticmethod
    def sort(lst, by):
        size = len(lst)
        while Sorter.float_largest_to_top(lst, size, by):
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
        return (f"Name:  {self.first_name} {self.last_name}\n"
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
        if email is not None:
            if type(email) != str:
                raise TypeError("Invalid type for email")
            if "@" not in email:
                raise ValueError("Invalid email")
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if phone is not None and type(phone) != str:
            raise TypeError("Invalid type for phone")
        if phone is not None:
            if int(phone) <= 0:
                raise ValueError("Phone number cannot be negative")
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

    def clear(self):
        """
        Clear/remove all contacts
        :return:
        """
        self._contacts.clear()

    @property
    def contacts(self):
        return self._contacts

    def add(self, contact):
        """
        Add a single contact (one person) to the internal data structures
        raise TypeError if contact is not an instance of class Contact
        """
        if type(contact) != Contact:
            raise TypeError(f"Type is {type(contact).__class__.__name__}, not Contact")

        self._contacts.append(contact)

    def find(self, name, by):
        """
        Find a contact by the given name
        """
        # middle = 0
        start = 0
        end = len(self._contacts) -1
    
        if by == self.BY_FIRST_NAME:
            first_name = str(name)
            while start <= end:
                middle = (start + end) // 2
                if first_name > self._contacts[middle].first_name:
                    start = middle + 1
                elif first_name < self._contacts[middle].first_name:
                    end = middle - 1
                elif first_name == self._contacts[middle].first_name:
                    pass
                else:
                    return self._contacts[middle]
    
        if by == self.BY_LAST_NAME:
            last_name = str(name)
            while start <= end:
                middle = (start + end) // 2
                if last_name > self._contacts[middle].last_name:
                    start = middle + 1
                elif last_name < self._contacts[middle].last_name:
                    end = middle - 1
                elif last_name == self._contacts[middle].last_name:
                    pass
                else:
                    return self._contacts[middle]
    
    
        def __str__(self, by=BY_FIRST_NAME):
            """
            Return a str that contains all contact, sorted by first names or
            last name, depending on the "by" parameter.
            It raises a ValueError if the "by" parameter contains invalid value.
            """
            Sorter.sort(self.contacts, by)
            return "\n".join([str(c) for c in self._contacts])
    
    
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
  contact = Contact(fields[0], fields[1])

  if len(fields) > 2:
      contact.email = fields[2]
if len(fields) > 3:
    contact.phone = fields[3]

return contact


def load_contacts_from_file(contact_list, filename):
    with open(filename) as f:
        for line in f:
            try:
                contact = line_to_contact(line)
                contact_list.add(contact)
            except Exception as e:
                print(f"Line '{line}' causes exception: {e}")


def load_contacts(contact_list):
    """
    Prompts the user for the name of a file, and load contact from that file.
    """
    filename = input("Enter the name of the file to load: ")
    contact_list.clear()

    try:
        load_contacts_from_file(contact_list, filename)
        print("Loaded {} contacts from {}".format(len(contact_list.contacts), filename))
    except Exception as e:
        print("Problem loading contacts: {}".format(e))


def print_by_first_name(contact_list):
    print("\n" + contact_list.__str__(ContactList.BY_FIRST_NAME))


def print_by_last_name(contact_list):
    print("\n" + contact_list.__str__(ContactList.BY_LAST_NAME))


def find_contact(contact_list, by):
    name = input("Please enter the name to search: ")
    contact = contact_list.find(name, by)
    # for entry in contact:
    #     print(entry.__str__())
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
    menu = {
        1: load_contacts,
        2: print_by_first_name,
        3: print_by_last_name,
        4: find_by_first_name,
        5: find_by_last_name,
        6: quit
    }

    while True:
        choice = get_choice()
        try:
            func = menu[choice]
            func(contact_list)
        except IndexError:
            print("Invalid choice")


if __name__ == '__main__':
    main()
