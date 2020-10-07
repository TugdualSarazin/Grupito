from Grupito import Skill, Group


class Project(object):
    def __init__(self, name, skills: [Skill] = [], groups: [Group] = []):
        self.name = name
        self.skills = skills
        self.groups = groups
