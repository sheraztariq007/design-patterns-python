from typing import List

from abstracts.abstract_employee import AbstractEmployee
from abstracts.abstract_job_description import AbstractJobDescription
from post_office.job_descriptions.ceo_job_description import CEOJobDescription


class CEO(AbstractEmployee):
    def __init__(self, name: str, address: str, hobbies: List[str], responsibilities: List[str]):
        self.name = name
        self.address = address
        self.hobbies = hobbies
        self.responsibilities = responsibilities

    def get_job_description(self) -> AbstractJobDescription:
        responsibilities = [
            "Have to attend meeting",
            "Interview new employee",
            "Manage new projects"
        ]

        self.responsibilities  += responsibilities

        job_description = CEOJobDescription(name="CEO Job Description", responsibilities=self.responsibilities)

        return job_description
