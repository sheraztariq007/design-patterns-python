from typing import List

from abstracts.abstract_job_description import AbstractJobDescription


class CEOJobDescription(AbstractJobDescription):
    def __init__(self, name: str, responsibilities: List[str] = []):
        self.responsibilities = responsibilities
        self.name = name


    def add_responsibility(self, responsibility):
        self.responsibilities.append(responsibility)

    def list_responsibilities(self):
        return self.responsibilities
