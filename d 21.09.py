class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in self.courses_in_progress and
                course in lecturer.courses_attached and
                1 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return sum(all_grades) / len(all_grades)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() <= other._calculate_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() == other._calculate_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return sum(all_grades) / len(all_grades)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() <= other._calculate_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() == other._calculate_avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress and
                1 <= grade <= 10):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Функции для подсчета средних оценок
def calculate_avg_hw_grade(students, course):
    grades = []
    for student in students:
        if course in student.grades:
            grades.extend(student.grades[course])
    if not grades:
        return 0
        return sum(grades) / len(grades)


def calculate_avg_lecture_grade(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades.extend(lecturer.grades[course])
    if not grades:
        return 0
    return sum(grades) / len(grades)



student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Anna', 'Smith', 'female')
student2.courses_in_progress += ['Python', 'Java']
student2.finished_courses += ['Основы программирования']


lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python', 'Git']

lecturer2 = Lecturer('John', 'Doe')
lecturer2.courses_attached += ['Python', 'Java']


reviewer1 = Reviewer('Mike', 'Johnson')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Sarah', 'Connor')
reviewer2.courses_attached += ['Python', 'Java']

оценки
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 8)

reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Java', 7)

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Git', 9)

student2.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Java', 9)


print("=== СТУДЕНТЫ ===")
print(student1)
print()
print(student2)
print()

print("=== ЛЕКТОРЫ ===")
print(lecturer1)
print()
print(lecturer2)
print()

print("=== РЕВЬЮЕРЫ ===")
print(reviewer1)
print()
print(reviewer2)
print()


print("=== СРАВНЕНИЕ СТУДЕНТОВ ===")
print(f"student1 > student2: {student1 > student2}")
print(f"student1 < student2: {student1 < student2}")
print(f"student1 == student2: {student1 == student2}")
print()

print("=== СРАВНЕНИЕ ЛЕКТОРОВ ===")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")
print()

# подсчета средних оценок
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]


