from typing import Optional


class Company:
    def __init__(self, employee_count: int, parent: Optional['Company'] = None):
        self.validate_employee_count(employee_count)
        self.validate_parent(parent)
        self._employee_count = employee_count
        self._parent = parent

    def set_parent(self, parent: Optional['Company'] = None):
        self.validate_parent(parent)
        self._parent = parent

    def get_parent(self):
        return self._parent

    def set_employee_count(self, employee_count: int):
        self.validate_employee_count(employee_count)
        self._employee_count = employee_count

    def get_employee_count(self):
        return self._employee_count

    def validate_parent(self, parent: Optional['Company'] = None):
        if not isinstance(parent, None | Company):
            raise TypeError("Company must be an instance of Company class")
        if parent is self:
            raise ValueError("Can`t be parent for itself")

    def validate_employee_count(self, count: int):
        if not isinstance(count, int):
            raise TypeError("Count must be an integer")
        if count <= 0:
            raise ValueError("Count must be greater than zero")
