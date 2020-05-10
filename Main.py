from Person import Person
from Address_book import AddressBook


def get_person_info():
    first_name = input("Введите имя: \n")
    second_name = input("Введите фамилию: \n")
    phone = input("Введите телефон: \n")
    address = input("Введите адрес: \n")
    person = Person(first_name, second_name, phone, address)
    return person


# тестовые пользователи, которые добавляются в адресную книгу
person1 = Person("Иван", "Иванов", "8 929 999 99 99", "1 street")
person2 = Person("Федор", "Федоров", "8 929 999 99 98", "1 street")
person3 = Person("Вася", "Васильев", "8 929 999 99 97", "1 street")
person4 = Person("Петя", "Васильев", "8 929 999 99 96", "1 street")
book = AddressBook()
book.append(person1)
book.append(person2)
book.append(person3)
book.append(person4)


def main():
    print(
        """
        -- Введите 1 для добавления нового контакта
        -- Введите 2 для удаления существующего
        -- Введите 3 чтобы увидеть все записи в адресной книге
        -- Введите 4 чтобы выйти из программы
        """)

    # раскомминтируйте следующую строку кода и закомминтируете блок с создением тестовых пользователей, если хотите
    # пустую адресную книгу

    # book = AddressBook()

    while True:
        text = input("Введите ваш выбор: \n")
        if text == "1":
            book.append(get_person_info())
        # будет удалять первый найденный контакт с указанной фамилией
        elif text == "2":
            print("В данной адресной книге, найдите номер пользователя, которого хотите удалить\n")
            book.display_address_book()
            user_input = input("Введите номер пользователя, которого хотите удалить: ")
            index_to_delete = int(user_input)
            if len(book) >= index_to_delete > 0:
                deleted = book.pop(index_to_delete - 1)
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



