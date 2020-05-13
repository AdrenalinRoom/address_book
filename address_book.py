NUM_WIDTH = 5
SECOND_NAME_WIDTH = 20
FIRST_NAME_WIDTH = 15
PHONE_WIDTH = 20
ADDRESS_WIDTH = 30


class AddressBook(list):

    def display_address_book(self):
        print(
            AddressBook.format_column("#", NUM_WIDTH),
            AddressBook.format_column("Фамилия", SECOND_NAME_WIDTH),
            AddressBook.format_column("Имя", FIRST_NAME_WIDTH),
            AddressBook.format_column("Телефон", PHONE_WIDTH),
            AddressBook.format_column("Адрес", ADDRESS_WIDTH)
        )
        for i, person in enumerate(self):
            print(
                AddressBook.format_column(str(i + 1), NUM_WIDTH),
                AddressBook.format_column(person.get_second_name(), SECOND_NAME_WIDTH),
                AddressBook.format_column(person.get_first_name(), FIRST_NAME_WIDTH),
                AddressBook.format_column(person.get_phone(), PHONE_WIDTH),
                AddressBook.format_column(person.get_address(), ADDRESS_WIDTH)
            )

    @staticmethod
    def format_column(value, column_width):
        str_length = len(value)
        if str_length == column_width:
            return value
        elif str_length > column_width:
            return value[:column_width]
        else:
            return value + " " * (column_width - str_length)
