from abstracts.abstract_office import AbstractOffice

from abstracts.abstract_employee import AbstractEmployee
from post_office.employees.accountant import Accountant
from post_office.employees.ceo import CEO


class PostOffice(AbstractOffice):

    def create_ceo(self) -> AbstractEmployee:
        hobbies = ["playing chess"]
        responsibilities = ["some stuff that a ceo do"]
        ceo = CEO("Joe Doe", "Oklahoma", hobbies=hobbies, responsibilities=responsibilities)

        return ceo

    def create_accountant(self) -> AbstractEmployee:
        hobbies = ["playing chess"]
        responsibilities = ["some stuff that a account do"]
        accountant = Accountant("Mark Doe", "Oklahoma", hobbies=hobbies, responsibilities=responsibilities)

        return accountant
