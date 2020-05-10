from Person import Person
from Address_book import AddressBook

person1 = Person("Иван", "Иванов", "8 929 999 99 99", "1 street")
assert person1.get_first_name() == "Иван"
person2 = Person("Федор", "Федоров", "8 929 999 99 98", "1 street")

book = AddressBook()

book.append(person1)
assert len(book) == 1

book.append(person2)
assert len(book) == 2

book.remove(person1)
assert person1 not in book

book.display_address_book()

person1.set_first_name("Васян")
assert person1.get_first_name() == "Васян"


# book.modify_person(person1)
# assert person1.get_first_name() == "Ваня"

# person1.description()
# person2.description()



