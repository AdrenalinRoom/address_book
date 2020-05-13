
class Person:

    def __init__(self, first_name, second_name, phone, address):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__phone = phone
        self.__address = address

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_second_name(self, second_name):
        self.__second_name = second_name

    def get_second_name(self):
        return self.__second_name

    def set_phone(self, phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address
