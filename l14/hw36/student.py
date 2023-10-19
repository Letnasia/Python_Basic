import human


class Student(human.Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {self.gender}, {self.age} years old, {self.first_name} {self.last_name}, {self.record_book}\n'

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return NotImplemented

    def __hash__(self):
        return hash(str(self))
