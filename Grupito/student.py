class Student(object):
    def __init__(self, name, is_online=False):
        self.name = name
        self.is_online = is_online

    def __str__(self) -> str:
        #return f"Student('{self.name}', is_online:{self.is_online})"
        if self.is_online:
            return self.name+'(online)'
        return self.name

    def __repr__(self) -> str:
        return self.__str__()

