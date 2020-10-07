# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Grupito import GroupGenerator, Project
from Grupito.group import Group
from Grupito.student import Student

adriana = Student('Adriana Aguirre Such')
alexander = Student('Alexander Pilipenko', is_online=True)
alireza = Student('Alireza Jamshidian mojaver', is_online=True)
alvaro = Student('Alvaro Cerezo Carrizo')
arina = Student('Arina Novikova')
dongxuan = Student('Dongxuan Zhu', is_online=True)
hebah = Student('Hebah qatanany')
inigo = Student('Iñigo Esteban Marina')
ivan = Student('Ivan Reyes Cano', is_online=True)
juan_pablo = Student('Juan Pablo Pintado Miranda', is_online=True)
kevin = Student('Kevin Aragón', is_online=True)
diana = Student('Konstantina Roussi')
kshama = Student('Kshama Patil', is_online=True)
laura = Student('Laura Guimarães')
leyla = Student('Leyla Saadi')
mario = Student('Mario José', is_online=True)
marta = Student('Marta Maria Galdys')
matteo = Student('Matteo Murat', is_online=True)
miguel = Student('Miguel Tinoco Hdz', is_online=True)
nadh_ha_naseer = Student('Nadh Ha Naseer')
riccardo = Student('Riccardo Palazzolo Henkes')
sasan = Student('Sasan Bahrami', is_online=True)
simone = Student('Simone Grasso')
sinay = Student('Sinay Coskun')
sridhar = Student('Sridhar Subramani')
stefania = Student('Stefania-Maria Kousoula', is_online=True)
tugdual = Student('Tugdual Sarazin')

students = [adriana, alexander, alireza, alvaro, arina, dongxuan, hebah, inigo, ivan, juan_pablo, kevin, diana,
            kshama, laura, leyla, mario, marta, matteo, miguel, nadh_ha_naseer, riccardo, sasan, simone, sinay, sridhar, stefania,
            tugdual]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nb_online = 0
    for stu in students:
        if stu.is_online:
            nb_online += 1
    print(f"students: {len(students)}")
    print(f"online students: {nb_online}")
    generator = GroupGenerator(project=Project("proj"),
                               desired_group_size=4,
                               all_students=students,
                               history=[])

    groups = generator.gen_groups_init_random(nb_iteration=100000)
    for grp in groups:
        print(grp)
