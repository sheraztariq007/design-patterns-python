from typing import List

from abstracts.abstract_job_description import AbstractJobDescription


class AccountantJobDescription(AbstractJobDescription):
    def __init__(self, name: str, responsibilities: List[str] = []):
        self.name = name
        self.responsibilities = responsibilities

    def add_responsibility(self, responsibility):
        self.responsibilities += responsibility

    def list_responsibilities(self) -> List[str]:
        return self.responsibilities

    def manage_tax(self, tax_id):
        print("Managing tax_id {}   {}".format(tax_id))


