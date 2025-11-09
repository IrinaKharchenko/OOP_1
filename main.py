class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return "Ошибка (не является лектором)"
        if course not in lecturer.courses_attached:
            return "Ошибка (лектор не прикреплен к этому курсу)"
        if (course not in self.finished_courses) and (course not in self.courses_in_progress):
            return "Ошибка (студент не изучает/не изучал этот курс)"
        if course not in lecturer.grades:
            lecturer.grades[course] = []
        lecturer.grades[course] += [grade]

    def avg_grades(self):
        s_grades = 0
        q_grades = 0
        for course_name, values in self.grades.items():
            s_grades += sum(values)
            q_grades += len(values)
        if q_grades == 0:
            return "Нет оценок"
        return s_grades / q_grades

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg_grades()} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'

    def __eq__(self, other):
        return self.avg_grades() == other.avg_grades()

    def __gt__(self, other):
        return self.avg_grades() > other.avg_grades()

    def __lt__(self, other):
        return self.avg_grades() < other.avg_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            return "Ошибка"

    def avg_lect_grades(self):
        s_lect_grades = 0
        q_lect_grades = 0
        for course_name, values in self.grades.items():
            s_lect_grades += sum(values)
            q_lect_grades += len(values)
        if q_lect_grades == 0:
            return "Нет оценок"
        return s_lect_grades / q_lect_grades

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_lect_grades()}'

    def __eq__(self, other):
        return self.avg_lect_grades() == other.avg_lect_grades()

    def __gt__(self, other):
        return self.avg_lect_grades() > other.avg_lect_grades()

    def __lt__(self, other):
        return self.avg_lect_grades() < other.avg_lect_grades()


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Ольга', 'Алёхина', 'Ж')

#You also have twisted name and surname of student (see upper row).
#I've changed it for proper results.

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'C++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

#You've used cyrillic "С" instead of latin in one row when gave attributes to objects for checking the code.
#I've changed it because it had not let to get a proper result.

print(lecturer.grades)  # {'Python': [7]}

print(student)

print(lecturer)

print(reviewer)

lecturer_1 = Lecturer("А.", "Синявский")
lecturer_2 = Lecturer("Г", "Свиридов")
lecturer_1.courses_attached = ['Python', 'C++']
lecturer_2.courses_attached = ['Python', 'C++']
lecturer_1.grades["Python"] = [8]
lecturer_2.grades["Python"] = [10]
print(lecturer_1 == lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2)

st_1 = Student("R.", "Grimes", "Male")
st_2 = Student("D", "Dixon", "Male")
st_1.grades["Python"] = [9]
st_2.grades["Python"] = [8]
print(st_1 == st_2)
print(st_1 > st_2)
print(st_1 < st_2)
