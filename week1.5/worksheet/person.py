# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    def __init__(self,name,birth):
        '''
        Create a person,given name and birth 
        '''
        if not isinstance(name,str):
            raise TypeError("Name must be a string")

        if not isinstance(birth,date):
            raise TypeError("Birth must be date")

        if name == "":
            raise ValueError("Name is empty")

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        chars = self.name.split()
        ans = ""
        for char in chars:
            ans += char[0]

        return ans.upper()

    def is_birthday(self):
        today = date.today()

        if self.birth.month == today.month and self.birth.day == today.day:
            return True
        else:
            return False

