import functools


class Student:
    def __init__(self, name, surname, age):
        self.__student_name__ = name
        self.__surname__ = surname
        self.__age__ = age
        self.__year__ = 1

    def get_name(self):
        return self.__student_name__

    def get_surname(self):
        return self.__surname__

    def get_age(self):
        return self.__age__

    def print_info(self):
        print(f"{self.__surname__} {self.__student_name__[0].upper()}. {self.__age__} {self.__year__} year")

    def promote(self):
        self.__year__ += 1


def compare(student1, student2):
    if student1.get_age() != student2.get_age():
        return student1.get_age() - student2.get_age()
    else:
        if student1.get_surname().lower() > student2.get_surname().lower():
            return 1
        else:
            return -1


class Group:
    def __init__(self):
        self.__students__ = []

    def add_student(self, student):
        self.__students__.append(student)

    def print_group(self):
        for student in self.__students__:
            student.print_info()

    def sort(self):
        self.__students__ = sorted(self.__students__, key=functools.cmp_to_key(compare))

    def promote(self):
        for student in self.__students__:
            student.promote()


group = Group()
group.add_student(Student("James", "Potter", 21))
group.add_student(Student("Thomas", "Anderson", 21))
group.add_student(Student("Nick", "Fury", 20))

group.print_group()
print("--------------------------------------------------")

group.sort()
group.promote()

group.print_group()
