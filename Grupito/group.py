import itertools
import random

from Grupito import Student


class IsContainBothEqualException(Exception):
    pass


class Group(object):
    def __init__(self, students: [Student]):
        self.students: [Student] = students

    def __str__(self) -> str:
        student_names = ', '.join(map(lambda s: str(s), self.students))
        return f"Group([{student_names}])"

    def __repr__(self) -> str:
        return self.__str__()

    def size(self) -> int:
        return len(self.students)

    def add_student(self, student: Student):
        self.students.append(student)

    def pop_random_student(self) -> Student:
        student = random.choice(self.students)
        self.students.remove(student)
        return student

    def is_contain_both(self, student1, student2) -> bool:
        if student1 == student2:
            raise IsContainBothEqualException
        return student1 in self.students and student2 in self.students

    def online_score(self) -> int:
        nb_online = 0
        for student in self.students:
            if student.is_online:
                nb_online += 1
        if self.size() == nb_online:
            return -1000*nb_online
        elif nb_online == 0:
            return 0
        elif nb_online == 1:
            return 100
        else:
            return -100*nb_online

    # TODO should be: def history_score(self, history: [Group]) -> int:
    # TODO: opti create a user history
    def history_score(self, history) -> int:
        score = 0
        for his in history:
            for s1, s2 in itertools.combinations(self.students, 2):
                #print(his, s1, s2)
                if s1 != s2 and his.is_contain_both(s1, s2):
                    score -= 10

        return score

    # TODO should be: def score(self, history [Group]) -> int:
    def score(self, history) -> int:
        return self.online_score() + self.history_score(history)
