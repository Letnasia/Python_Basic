class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Human: {self.gender}, {self.age}, {self.first_name} {self.last_name} '


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {self.gender}, {self.age} years old, {self.first_name} {self.last_name}, {self.record_book}\n'


class TooManyStudents(Exception):
    pass


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise TooManyStudents()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.discard(student)

    def find_student(self, last_name):
        for stud in self.group:
            if stud.last_name == last_name:
                return stud

    def __str__(self):
        all_students = ''
        for stud in self.group:
            all_students += str(stud)
        return f'Number:{self.number}\n{all_students}'


gr = Group('PD1')
gr.add_student(Student('Male', 30, 'Steve', 'Jobs', 'AN142'))
gr.add_student(Student('Female', 25, 'Liza', 'Taylor', 'AN145'))
gr.add_student(Student('Male', 27, 'Ivan', 'Popov', 'AN140'))
gr.add_student(Student('Female', 23, 'Eva', 'Ivanova', 'AN141'))
gr.add_student(Student('Male', 27, 'Jack', 'Smith', 'AN146'))
gr.add_student(Student('Male', 24, 'Paul', 'Dorton', 'AN148'))
gr.add_student(Student('Female', 27, 'Julia', 'Popova', 'AN149'))
gr.add_student(Student('Male', 25, 'Ivan', 'Ivanov', 'AN141'))
gr.add_student(Student('Male', 27, 'Igor', 'Molotov', 'AN150'))
gr.add_student(Student('Female', 22, 'Lora', 'Martinez', 'AN143'))
gr.add_student(Student('Male', 24, 'John', 'Black', 'AN147'))

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'
gr.delete_student('Taylor')
print(gr)  # Only one student
gr.delete_student('Taylor')  # No error!