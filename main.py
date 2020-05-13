from person import Person
from address_book import AddressBook
import pickle
import os


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


def get_person_info():
    first_name = input("Введите имя: \n")
    second_name = input("Введите фамилию: \n")
    phone = input("Введите телефон: \n")
    address = input("Введите адрес: \n")
    person = Person(first_name, second_name, phone, address)
    return person


@benchmark
def save_address_book_to_file(address_book):
    with open("address_book.txt", 'wb') as f:
        pickle.dump(address_book, f)
        f.flush()
        f.close()


@benchmark
def read_address_book_from_file():
    file_name = "address_book.txt"
    if os.path.exists(file_name):
        file_address_book = open(file_name, 'rb')
        is_file_empty = os.path.getsize(file_name) == 0
        if is_file_empty:
            book = AddressBook()
        else:
            book = pickle.load(file_address_book)
        file_address_book.close()
    else:
        book = AddressBook()
        file_address_book = open(file_name, 'tw')
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


if __name__ == '__main__':
    main()
