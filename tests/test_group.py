import pytest

from Grupito import *


def test_str():
    stu1 = Student("stu1")
    stu2 = Student("stud2")
    grp = Group([stu1, stu2])
    assert grp.__str__() == "Group([Student('stu1', is_online:False), Student('stud2', is_online:False)])"


def test_size():
    stu1 = Student("stu1")
    stu2 = Student("stud2")

    grp0 = Group([])
    assert grp0.size() == 0

    grp1 = Group([stu1])
    assert grp1.size() == 1

    grp2 = Group([stu1, stu2])
    assert grp2.size() == 2


def add_student():
    project = Project("proj")
    stu1 = Student("stu1")
    stu2 = Student("stud2")
    grp = Group([])

    grp.add_student(stu1)
    assert grp.students == [stu1]

    grp.add_student(stu2)
    assert grp.students == [stu1, stu2]


def test_pop_random_student():
    project = Project("proj")
    stu1 = Student("stu1")
    stu2 = Student("stud2")
    grp = Group([stu1, stu2])
    assert grp.size() == 2

    pop_student1 = grp.pop_random_student()
    assert grp.size() == 1
    assert pop_student1 == stu1 or pop_student1 == stu2

    pop_student2 = grp.pop_random_student()
    assert grp.size() == 0
    assert pop_student1 == stu1 or pop_student1 == stu2
    assert pop_student2 != pop_student1


def test_contain_both():
    project = Project("proj")
    stu1 = Student("stu1")
    stu2 = Student("stud2")
    stu3 = Student("stud3")
    grp = Group([stu1, stu2])
    assert grp.is_contain_both(stu1, stu2)
    assert grp.is_contain_both(stu2, stu1)
    assert not grp.is_contain_both(stu1, stu3)
    assert not grp.is_contain_both(stu2, stu3)


def test_contain_both_exception():
    stu1 = Student("stu1")
    stu2 = Student("stud2")
    grp = Group([stu1, stu2])
    with pytest.raises(IsContainBothEqualException) as ex:
        grp.is_contain_both(stu1, stu1)


def test_online_score():
    stu_online1 = Student("stu_online1", is_online=True)
    stu_online2 = Student("stu_online2", is_online=True)
    stu_offline1 = Student("stu_offline1", is_online=False)
    stu_offline2 = Student("stu_offline2", is_online=False)
    grp_all_offline = Group([stu_offline1, stu_offline2])
    assert grp_all_offline.online_score() == 0
    grp_one_online = Group([stu_offline1, stu_offline2, stu_online1])
    assert grp_one_online.online_score() == 100
    grp_two_online = Group([stu_offline1, stu_offline2, stu_online1, stu_online2])
    assert grp_two_online.online_score() == -200
    grp_only_online = Group([stu_online1, stu_online1])
    assert grp_only_online.online_score() == -2000


def test_history_score():
    stuA = Student("stuA")
    stuB = Student("stuB")
    stuC = Student("stuC")
    histoAB = Group([stuA, stuB])
    histoAC = Group([stuA, stuC])

    grp_sAB_h0 = Group([stuA, stuB])
    assert grp_sAB_h0.history_score(history=[]) == 0

    grp_sAB_hAC = Group([stuA, stuB])
    assert grp_sAB_hAC.history_score(history=[histoAC]) == 0

    grp_sAB_hAB = Group([stuA, stuB])
    assert grp_sAB_hAB.history_score(history=[histoAB]) == -10

    grp_sABC_hAB = Group([stuA, stuB, stuC])
    assert grp_sABC_hAB.history_score(history=[histoAB]) == -10

    grp_sABC_hAB_hAC = Group([stuA, stuB, stuC])
    assert grp_sABC_hAB_hAC.history_score(history=[histoAB, histoAC]) == -20


def test_score():
    stuA = Student("stuA", is_online=False)
    stuB = Student("stuB", is_online=True)
    stuC = Student("stuC", is_online=True)
    histoAB = Group([stuA, stuB])
    histoAC = Group([stuA, stuC])

    # -10 (histo AB) -10 (histo AC) - 200 (B online + C online)
    assert Group([stuA, stuB, stuC]).score(history=[histoAB, histoAC]) == -220
