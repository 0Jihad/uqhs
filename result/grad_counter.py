# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 06:09:36 2019

@author: AdeolaOlalekan
"""

from .models import RESULT_GRADE
from django.shortcuts import get_object_or_404
def grade_counter(mains, tur):
    grd = RESULT_GRADE.objects.filter(subject__exact = tur.subject.name, identifier__exact = tur.id).count()
    if grd == 0:
        grd = RESULT_GRADE(subject = tur.subject.name, identifier = tur.id)
        grd.save()
    else:
        grd = get_object_or_404(RESULT_GRADE, subject = tur.subject.name, identifier = tur.id)
    grades = list(mains.values_list('grade'))
    grade_list = [n[0] for n in [list(x) for x in grades]]
    set_uni = list(set(grade_list))
    grd_lst = [['A', 'C', 'P', 'F', 'A1', 'B2', 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(0, len(set_uni)):
        if set_uni[i] in grd_lst[0]:
            grd_lst[1][grd_lst[0].index(set_uni[i])] = len([x for x in grade_list if x == set_uni[i]])
    grd.grade_A = grd_lst[1][0]
    grd.grade_C = grd_lst[1][1]
    grd.grade_P = grd_lst[1][2]
    grd.grade_F = grd_lst[1][3]
    grd.grade_A1 = grd_lst[1][4]
    grd.grade_B2 = grd_lst[1][5]
    grd.grade_B3 = grd_lst[1][6]
    grd.grade_C4 = grd_lst[1][7]
    grd.grade_C5 = grd_lst[1][8]
    grd.grade_C6 = grd_lst[1][9]
    grd.grade_D7 = grd_lst[1][10]
    grd.grade_E8 = grd_lst[1][11]
    grd.grade_F9 = grd_lst[1][12]
    grd.save()
    if tur.term == '3rd Term':
        grd.remark = True
        grd.save()
    return grd