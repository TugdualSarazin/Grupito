from Grupito import *


def test_group_score():
    stuA = Student("stuA", is_online=False)
    stuB = Student("stuB", is_online=True)
    stuC = Student("stuC", is_online=True)
    histoAB = Group([stuA, stuB])
    histoAC = Group([stuA, stuC])
    grp = Group([stuA, stuB, stuC])

    grp_score = GroupScore(group=grp, history=[histoAB, histoAC])
    assert grp_score.group == grp
    # -10 (histo AB) -10 (histo AC) - 200 (B online + C online)
    assert grp_score.score == -220


def test_init_random_groups():
    stuA = Student("stuA")
    stuB = Student("stuB")
    stuC = Student("stuC")
    stuD = Student("stuD")

    all_students1 = [stuA, stuB, stuC]
    generator1 = GroupGenerator(project=Project("proj"),
                                desired_group_size=2,
                                all_students=all_students1,
                                history=[])
    groups1 = generator1.groups
    assert len(groups1) == 2
    assert type(groups1[0]) == GroupScore
    assert groups1[0].group.size() == 2
    assert type(groups1[1]) == GroupScore
    assert groups1[1].group.size() == 1

    all_students2 = [stuA, stuB, stuC, stuD]
    generator2 = GroupGenerator(project=Project("proj"),
                                desired_group_size=2,
                                all_students=all_students2,
                                history=[])
    groups2 = generator2.groups
    assert len(groups2) == 2
    assert groups2[0].group.size() == 2
    assert groups2[1].group.size() == 2

    # Should not update the origin students list
    assert len(all_students2) == 4


def test_get_worst_groups():
    gen = GroupGenerator(project=Project("proj"),
                         desired_group_size=2,
                         all_students=[],
                         history=[])
    grpA = GroupScore(Group([Student("stuA")]), [])
    grpA.score = 3
    grpB = GroupScore(Group([Student("stuB")]), [])
    grpB.score = 4
    grpC = GroupScore(Group([Student("stuC")]), [])
    grpC.score = -20
    grpD = GroupScore(Group([Student("stuD")]), [])
    grpD.score = -10
    gen.groups = [grpA, grpB, grpC, grpD]

    assert gen.get_worst_groups(4) == [grpC, grpD, grpA, grpB]
    assert gen.get_worst_groups(2) == [grpC, grpD]
    assert gen.get_worst_groups(0) == []


def test_swap_random_students():
    gen = GroupGenerator(project=Project("proj"),
                         desired_group_size=2,
                         all_students=[],
                         history=[])
    grpA = GroupScore(Group([Student("stuA")]), [])
    grpB = GroupScore(Group([Student("stuB")]), [])
    gen.groups = [grpA, grpB]

    gen.swap_random_students(grpA, grpB)
    assert gen.groups[0].group.students[0].name == "stuB"
    assert gen.groups[1].group.students[0].name == "stuA"

    gen.swap_random_students(grpA, grpB)
    assert gen.groups[0].group.students[0].name == "stuA"
    assert gen.groups[1].group.students[0].name == "stuB"


def test_iterate():
    gen = GroupGenerator(project=Project("proj"),
                         desired_group_size=2,
                         all_students=[],
                         history=[])
    grpA = GroupScore(Group([Student("stuA")]), [])
    grpB = GroupScore(Group([Student("stuB")]), [])
    gen.groups = [grpA, grpB]

    gen.iterate(2)
    assert gen.groups[0].group.students[0].name == "stuB"
    assert gen.groups[1].group.students[0].name == "stuA"

    gen.iterate(2)
    assert gen.groups[0].group.students[0].name == "stuA"
    assert gen.groups[1].group.students[0].name == "stuB"


def test_range_nb_group_swap():
    students10 = [Student("stu1") for _i in range(10)]
    gen = GroupGenerator(project=Project("proj"),
                         desired_group_size=1,
                         all_students=students10,
                         history=[])

    assert gen.range_nb_group_swap(20) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 2]


def test_gen_groups():
    stuA = Student("stuA")
    stuB = Student("stuB")

    gen1 = GroupGenerator(project=Project("proj"),
                          desired_group_size=1,
                          all_students=[stuA, stuB],
                          history=[])
    gen1_stu1 = gen1.groups[0].group.students[0]
    gen1_stu2 = gen1.groups[1].group.students[0]
    # 1 iteration
    groups1 = gen1.gen_groups(1)
    assert groups1[0].group.students[0] == gen1_stu2
    assert groups1[1].group.students[0] == gen1_stu1

    gen2 = GroupGenerator(project=Project("proj"),
                          desired_group_size=1,
                          all_students=[stuA, stuB],
                          history=[])
    gen2_stu1 = gen2.groups[0].group.students[0]
    gen2_stu2 = gen2.groups[1].group.students[0]
    # 0 iteration
    groups2 = gen2.gen_groups(0)
    assert groups2[0].group.students[0] == gen2_stu1
    assert groups2[1].group.students[0] == gen2_stu2


def test_gen_groups_init_random():
    stuA = Student("stuA")
    stuB = Student("stuB")

    gen = GroupGenerator(project=Project("proj"),
                         desired_group_size=1,
                         all_students=[stuA, stuB],
                         history=[])
