from typing import List

class School:
    def __init__(self, grade: str, class_name: str, num_students: int):
        self.grade = grade
        self.class_name = class_name
        self.num_students = num_students
        self.homeworks = []

    def create_homework(self, title: str, description: str, deadline: str):
        homework = Homework(title, description, deadline)
        self.homeworks.append(homework)

    def assign_homework(self, homework: Homework):
        for school_class in self.__class__.__bases__:
            if isinstance(school_class, School):
                school_class.receive_homework(homework)

    def follow_progress(self) -> float:
        completed = 0
        for school_class in self.__class__.__bases__:
            if isinstance(school_class, School):
                completed += school_class.get_completed_homeworks_count()
        return completed / self.num_students

class Homework:
    def __init__(self, title: str, description: str, deadline: str):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = []

    def mark_completed(self, student_name: str):
        self.completed.append(student_name)

class Grade1:
    @classmethod
    def receive_homework(cls, homework: Homework):
        cls.homeworks.append(homework)

    @classmethod
    def get_completed_homeworks_count(cls) -> int:
        completed = 0
        for homework in cls.homeworks:
            completed += len(homework.completed)
        return completed

    homeworks = []

class ClassA(Grade1, School):
    pass

# Create a Grade 1, Class A with 20 students
class_a = ClassA("Grade 1", "Class A", 20)

# Create a new homework assignment
class_a.create_homework("Math Homework", "Complete page 30-31 in the math book", "2023-04-10")

# Assign the homework assignment to all classes in Grade 1
class_a.assign_homework(class_a.homeworks[0])

# Mark some students as completed the homework assignment
class_a.homeworks[0].mark_completed("Alice")
class_a.homework