import random
import sys

from Grupito import Group, Project, Student


class GroupScore(object):
    def __init__(self, group: Group, history: [Group]):
        self.group = group
        self.history = history
        self.update_score()

    def update_score(self) -> int:
        self.score = self.group.score(self.history)
        return self.score

    def __str__(self):
        return f"{self.score}: {self.group}"

    def __repr__(self):
        return self.__str__()


class OutOfRangeException(Exception):
    pass


class GroupGenerator(object):
    def __init__(self, project: Project, desired_group_size: int, all_students: [Student], history: [Group]):
        self.project = project
        self.desired_group_size = desired_group_size
        self.all_students = all_students
        self.history = history
        self.groups = self.random_groups()

    def random_groups(self) -> [GroupScore]:
        all_students_copy = self.all_students.copy()
        groups: [GroupScore] = []
        current_group = Group(students=[])

        while all_students_copy:
            # Select a random student
            student = random.choice(all_students_copy)
            # Remove the group from the list of student
            all_students_copy.remove(student)
            # Add the student to the group
            current_group.add_student(student)
            # If the current group is full or if the end of the iteration => add to groups
            if current_group.size() == self.desired_group_size:
                groups.append(GroupScore(current_group, self.history))
                current_group = Group(students=[])

        if current_group.size() > 0:
            groups.append(GroupScore(current_group, self.history))

        return groups

    def get_worst_groups(self, nb_group_swap: int):
        self.groups.sort(key=lambda grp: grp.score, reverse=False)
        return self.groups[:nb_group_swap]

    @staticmethod
    def swap_random_students(group1: GroupScore, group2: GroupScore):
        # Remove random student
        student1 = group1.group.pop_random_student()
        student2 = group2.group.pop_random_student()
        # Add them to the other group
        group1.group.add_student(student2)
        group2.group.add_student(student1)
        # Update scores
        group1.update_score()
        group2.update_score()

    def iterate(self, nb_group_swap: int):
        if 2 < nb_group_swap > len(self.groups):
            raise OutOfRangeException
        worst_groups = self.get_worst_groups(nb_group_swap)
        while len(worst_groups) >= 2:
            worst1 = random.choice(worst_groups)
            worst_groups.remove(worst1)
            worst2 = random.choice(worst_groups)
            worst_groups.remove(worst2)
            self.swap_random_students(worst1, worst2)

    def range_nb_group_swap(self, nb_iteration) -> [int]:
        swap_range = []
        nb_groups = len(self.groups)
        for i in range(0, nb_iteration):
            ratio_swap = (nb_iteration - i) / nb_iteration
            nb_swap = int(nb_groups * ratio_swap)
            if nb_swap < 2:
                swap_range.append(2)
            else:
                swap_range.append(nb_swap)
        return swap_range

    def gen_groups(self, nb_iteration: int) -> [GroupScore]:
        for nb_group_swap in self.range_nb_group_swap(nb_iteration):
            self.iterate(nb_group_swap)
        return self.groups

    def gen_groups_init_random(self, nb_iteration: int):
        best_groups = None
        best_groups_score = -10 ** 10
        for _i in range(10):

            # Random init group
            groups = self.random_groups()
            # Sum score
            groups_score = 0
            for grp in groups:
                groups_score += grp.score
            # If the groups score is better than the best replace by it
            if groups_score > best_groups_score:
                best_groups = groups
                best_groups_score = groups_score
        return best_groups

    def aa(self):
        self.all_students
