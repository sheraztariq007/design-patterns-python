from abstracts.AbstractDepartment import AbstractDepartment


class ShippingDepartment(AbstractDepartment):

    def __init__(self):
        self._name = None

    def set_name(self, name):
        self._name = name

    def get_name(self) -> str:
        return self._name
