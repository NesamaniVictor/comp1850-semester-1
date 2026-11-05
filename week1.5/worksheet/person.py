# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Creates a Person, given values for name and birth.
        """

        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if not isinstance(birth, date):
            raise TypeError("Birth must be a date")

        self.name = name
        self.birth = birth

    def initials(self):
        """
        Returns the initials of the person.
        """
        parts = self.name.split()
        return ''.join([part[0].upper() for part in parts])

    def is_birthday(self):
        """
        Returns True if today is the person's birthday, False otherwise.
        """
        today = date.today()
        return self.birth.month == today.month and self.birth.day == today.day


