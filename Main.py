from Person import Person
from Address_book import AddressBook
import pickle
import os


def get_person_info():
    first_name = input("Введите имя: \n")
    second_name = input("Введите фамилию: \n")
    phone = input("Введите телефон: \n")
    address = input("Введите адрес: \n")
    person = Person(first_name, second_name, phone, address)
    return person


def save_address_book_to_file(address_book):
    with open("address_book.txt", 'wb') as f:
        pickle.dump(address_book, f)
        f.flush()
        f.close()


def read_address_book_from_file():
    file_address_book = open("address_book.txt", 'rb')
    is_file_empty = os.path.getsize("address_book.txt") == 0
    if is_file_empty:
        book = AddressBook()
    else:
        book = pickle.load(file_address_book)
    file_address_book.close()
    return book


def main():
    print(
        """
        -- Введите 1 для добавления нового контакта
        -- Введите 2 для удаления существующего
        -- Введите 3 чтобы увидеть все записи в адресной книге
        -- Введите 4 чтобы выйти из программы
        """)
    book = read_address_book_from_file()

    while True:
        text = input("Введите ваш выбор: \n")
        if text == "1":
            book.append(get_person_info())
            save_address_book_to_file(book)
        elif text == "2":
            print("В данной адресной книге, найдите номер пользователя, которого хотите удалить\n")
            book.display_address_book()
            user_input = input("Введите номер пользователя, которого хотите удалить: ")
            index_to_delete = int(user_input)
            if len(book) >= index_to_delete > 0:
                deleted = book.pop(index_to_delete - 1)
                save_address_book_to_file(book)
                print("Пользователь {} {} удален".format(deleted.get_second_name(), deleted.get_first_name()))
            else:
                print("Такого пользователя не существует")
        elif text == "3":
            book.display_address_book()
        elif text == "4":
            print("Программа завершена")
            break
        else:
            print("Введите корректную команду")


main()



