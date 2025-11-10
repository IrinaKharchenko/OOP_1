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


#You also have twisted name and surname of student (see upper row).
#I've changed it for proper results.

#You've used cyrillic "С" instead of latin in one row when gave attributes to objects for checking the code.
#I've changed it because it had not let to get a proper result.


lecturer_1 = Lecturer("Андрей", "Синявский")
lecturer_2 = Lecturer("Григорий", "Свиридов")
lecturer_1.courses_attached = ['Python', 'Java']
lecturer_2.courses_attached = ['Java', 'C++']
lecturer_1.grades["Python"] = [8]
lecturer_1.grades["Java"] = [5]
lecturer_2.grades["Java"] = [10]
lecturer_2.grades["C++"] = [7]

reviewer_1 = Reviewer("Кэрол", "Пелетье")
reviewer_2 = Reviewer("Мэгги", "Грин")
reviewer_1.courses_attached = ['C++', "Python"]
reviewer_2.courses_attached = ['Python', "C++"]

student_1 = Student("Карл", "Граймс", "М")
student_2 = Student("Дороти", "Спаркс", "Ж")
student_1.courses_in_progress = ['Java']
student_2.courses_in_progress = ['C++']
student_1.finished_courses = ['Python']
student_2.finished_courses = ['Python']
student_1.grades = {'Python' : [10], 'Java' : [6], 'C++' : [6]}
student_2.grades = {'Python' : [9], 'Java' : [6], 'C++' : [10]}



print(student_1)

print(student_2)

print(lecturer_1)

print(lecturer_2)

print(reviewer_1)

print(reviewer_2)


print(lecturer_1 == lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2)


print(student_1 == student_2)
print(student_1 > student_2)
print(student_1 < student_2)


def total_person_grade(person_list, course_list):
    total_grades = {}
    for course_name in course_list:
        grade_list = []
        for person in person_list:
            if course_name in person.grades:
                grade_list.extend(person.grades[course_name])
        if len(grade_list) == 0:
            total_grades[course_name] = 'Ошибка'
        else:
            total_grades[course_name] = sum(grade_list) / len(grade_list)
    return total_grades


print(total_person_grade([student_1, student_2], ['Python', 'C++', 'Java']))

print(total_person_grade([lecturer_1, lecturer_2], ['Python', 'C++', 'Java']))

