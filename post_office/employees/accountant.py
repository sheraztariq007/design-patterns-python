from typing import List

from abstracts.abstract_employee import AbstractEmployee
from abstracts.abstract_job_description import AbstractJobDescription
from post_office.job_descriptions.accountant_job_description import AccountantJobDescription


class Accountant(AbstractEmployee):
    def __init__(self, name: str, address: str, hobbies: List[str], responsibilities: List[str]):
        self.name = name
        self.address = address
        self.hobbies = hobbies
        self.responsibilities = responsibilities

    def get_job_description(self) -> AbstractJobDescription:
        accountant_job_description = AccountantJobDescription(name="Accountant Job",
                                                              responsibilities=self.responsibilities)
        return accountant_job_description
