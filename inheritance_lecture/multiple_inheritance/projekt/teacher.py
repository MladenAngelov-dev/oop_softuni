from projekt.employee import Employee
from projekt.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."

