class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ", ".join(self.courses_in_progress)
        finished_courses_string = ", ".join(self.finished_courses)
        for a in self.grades:
            grades_count += len(self.grades[a])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за домашнее задание: {self.average_rating}\n" \
              f"Курсы в процессе обучения: {courses_in_progress_string}\n" \
              f"Законченные курсы: {finished_courses_string}"
        return res


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Такое сравнение некорректно")
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for a in self.grades:
            grades_count += len(self.grades[a])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Такое сравнение некорректно")
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


best_lecturer1 = Lecturer("Vladimir", "Sidorov")
best_lecturer1.courses_attached += ["Python"]

best_lecturer2 = Lecturer("Petr", "Kuznetsov")
best_lecturer2.courses_attached += ["Git"]

best_lecturer3 = Lecturer("Kolya", "Ivanov")
best_lecturer3.courses_attached += ["Python"]

cool_reviewer1 = Reviewer("Some", "Buddy")
cool_reviewer1.courses_attached += ["Python"]
cool_reviewer1.courses_attached += ["Git"]

cool_reviewer2 = Reviewer("Bill", "Gates")
cool_reviewer2.courses_attached += ["Python"]
cool_reviewer2.courses_attached += ["Git"]

student1 = Student("Kirill", "Belousov")
student1.courses_in_progress += ["Python"]
student1.finished_courses += ["Введение в программирование"]

student2 = Student("Mikhail", "Lermontov")
student2.courses_in_progress += ["Git"]
student2.finished_courses += ["Введение в программирование"]

student3 = Student("Ilya", "Anikeev")
student3.courses_in_progress += ["Python"]
student3.finished_courses += ["Введение в программирование"]

student1.rate_hw(best_lecturer1, "Python", 10)
student1.rate_hw(best_lecturer1, "Python", 10)
student1.rate_hw(best_lecturer1, "Python", 10)

student1.rate_hw(best_lecturer2, "Python", 5)
student1.rate_hw(best_lecturer2, "Python", 8)
student1.rate_hw(best_lecturer2, "Python", 7)

student1.rate_hw(best_lecturer1, "Python", 9)
student1.rate_hw(best_lecturer1, "Python", 7)
student1.rate_hw(best_lecturer1, "Python", 8)

student2.rate_hw(best_lecturer2, "Git", 10)
student2.rate_hw(best_lecturer2, "Git", 9)
student2.rate_hw(best_lecturer2, "Git", 8)

student3.rate_hw(best_lecturer3, "Python", 6)
student3.rate_hw(best_lecturer3, "Python", 4)
student3.rate_hw(best_lecturer3, "Python", 8)

cool_reviewer1.rate_hw(student1, "Python", 8)
cool_reviewer1.rate_hw(student1, "Python", 9)
cool_reviewer1.rate_hw(student1, "Python", 10)

cool_reviewer2.rate_hw(student2, "Git", 8)
cool_reviewer2.rate_hw(student2, "Git", 7)
cool_reviewer2.rate_hw(student2, "Git", 9)

cool_reviewer2.rate_hw(student3, "Python", 8)
cool_reviewer2.rate_hw(student3, "Python", 7)
cool_reviewer2.rate_hw(student3, "Python", 9)
cool_reviewer2.rate_hw(student3, "Python", 8)
cool_reviewer2.rate_hw(student3, "Python", 7)
cool_reviewer2.rate_hw(student3, "Python", 9)

print(f"Перечень студентов:\n\n{student1}\n\n{student2}\n\n{student3}")
print()
print()


print(f"Перечень лекторов: \n\n{best_lecturer1}\n\n{best_lecturer2}\n\n{best_lecturer3}")
print()
print()

print(f"Результат сравнения студентов (по средним оценкам за ДЗ): "
      f"{student1.name} {student1.surname} < {student2.name} {student2.surname} = {student1 > student2}")
print()

print(f"Результат сравнения лекторов (по средним оценкам за лекции): "
      f"{best_lecturer1.name} {best_lecturer1.surname} < {best_lecturer2.name} {best_lecturer2.surname} = {best_lecturer1 > best_lecturer2}")
print()

student_list = [student1, student2, student3]

lecturer_list = [best_lecturer1, best_lecturer2, best_lecturer3]


def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()
