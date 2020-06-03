from person import Person
from address_book import AddressBook
import pytest


@pytest.fixture()
def setup():
    person1 = Person("Иван", "Иванов", "8 929 999 99 99", "1 street")
    return person1


@pytest.mark.usefixtures("setup")
class TestAB:
    def test_create_person(self, setup):
        assert setup.get_first_name() == "Иван"

    def test_add_person_to_address_book(self, setup):
        book = AddressBook()
        book.append(setup)
        assert len(book) == 1

    def test_change_person_info(self, setup):
        setup.set_first_name("Васян")
        assert setup.get_first_name() == "Васян"

    def test_delete_person_from_address_book(self, setup):
        book = AddressBook()
        book.append(setup)
        book.remove(setup)
        assert setup not in book





