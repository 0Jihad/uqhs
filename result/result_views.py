
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 08:05:55 2019

@author: AdeolaOlalekan
"""

#from django.http import HttpResponse
#return HttpResponse(len(empty_list), content_type='text/plain')
##############################LOGIN BAIL#######################################
from .models import QSUBJECT, TOTAL, ANNUAL, BTUTOR, RESULT_GRADE
from .grad_counter import grade_counter
from django.contrib.auth.decorators import login_required 
from result.grader import grades, don_e
from django.shortcuts import render, get_object_or_404, redirect#, redirect
from django.db.models import Sum, Avg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
        
def cader(qry):
    clas = [['', 'JSS 1', 'JSS 2', 'JSS 3', 'SS 1', 'SS 2', 'SS 3'], ['', 'jss_one', 'jss_two', 'jss_three', 'sss_one', 'sss_two', 'sss_three']]
    x = clas[0].index(qry)
    if x <= 3:
        cader = 'j'
    else:
        cader = 's'
    return cader
@login_required
def subject_total(request, pk):
    tutor = BTUTOR.objects.get(pk=pk)
    if tutor.model_in == 'qsubject':
        mains = QSUBJECT.objects.filter(tutor__exact=tutor).order_by('id')
    else:
        mains = ANNUAL.objects.filter(subject__exact=tutor.subject, subject_by__Class__exact=tutor.Class, term__exact='3rd Term').order_by('id')
    old = TOTAL.objects.filter(subject_by__exact=tutor).count()
    if old == 0:
        qar = TOTAL(subject_by=tutor, subject_scores=mains.aggregate(Sum('agr'))['agr__sum'], subject_pert=round(mains.aggregate(Avg('agr'))['agr__avg'],2), model_in=tutor.model_in)
        qar.save() 
    else:
        qar = get_object_or_404(TOTAL, subject_by__exact=tutor)
        qar.subject_scores = mains.aggregate(Sum('agr'))['agr__sum']
        qar.subject_pert=round(mains.aggregate(Avg('agr'))['agr__avg'],2)
        qar.save()
    page = request.GET.get('page', 1)
    paginator = Paginator(mains, 60)
    many = mains.count()
    grade_counter(mains, tutor)
    grad = get_object_or_404(RESULT_GRADE, identifier = tutor.id, subject = tutor.subject.name)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    if tutor.model_in == 'qsubject':
        return render(request, 'result/qsubject.html', {'count_grade': many, 'grad' : grad, 'all_page': all_page,  'qry' : tutor, 'pk': pk, 'qar':qar})
    else:
        return render(request, 'result/annual.html', {'count_grade': many, 'grad' : grad, 'all_page': all_page,  'qry' : tutor, 'pk': pk, 'qar':qar})

#@login_required
def single_student_update(request, pk):#student
    obj = QSUBJECT.objects.get(pk=pk)
    if obj.tutor != None:
        obj.total = obj.test + obj.agn + obj.atd
        obj.agr = obj.exam + obj.total
        obj.grade = grades([obj.agr], cader(obj.tutor.Class))[0]
        obj.save()
        first = ANNUAL.objects.filter(student_name__exact=obj.student_name, term='1st Term', subject__exact=obj.tutor.subject).count()
        if first == 0:#create new record
            if obj.tutor.term == '1st Term':
                ann_scr = ANNUAL(student_name=obj.student_name, first = obj.agr, subject_by=obj.tutor, subject=obj.tutor.subject, term = '1st Term')
                ann_scr.save()
            elif obj.tutor.term == '2nd Term':
                ann_scr = ANNUAL(student_name=obj.student_name, second = obj.agr, subject_by=obj.tutor, subject=obj.tutor.subject, term = '1st Term')
                ann_scr.save()
            else:
                if obj.tutor.term == '3rd Term':
                    ann_scr = ANNUAL(student_name=obj.student_name, third = obj.agr, subject_by=obj.tutor, subject=obj.tutor.subject, term = '1st Term')
                    ann_scr.save()
        else:#update records
            ann_scr = get_object_or_404(ANNUAL, student_name__exact=obj.student_name, subject__exact=obj.tutor.subject, term__exact='1st Term')
            if obj.tutor.term == '1st Term':
                ann_scr.first = obj.agr
                ann_scr.save()
            elif obj.tutor.term == '2nd Term':
                ann_scr.second = obj.agr
                ann_scr.save()
            else:
                if obj.tutor.term == '3rd Term':
                    ann_scr.third = obj.agr
                    ann_scr.save()
        return redirect('position_updates', pk=obj.tutor.id)
    else:
        return redirect('home')
@login_required
def subject_position_updates(request, pk):#all
    query = QSUBJECT.objects.filter(tutor__exact=BTUTOR.objects.get(pk=pk))
    students = [x[:] for x in list(query.values_list('agr', 'id')) if x[0] != None]
    agr = [r[0] for r in students]###############news
    posi = don_e(agr[:])
    ids = [r[1] for r in students]
    for i in range(0, len(agr)):
        objs = QSUBJECT.objects.get(pk=ids[i])
        objs.posi = posi[i]
        objs.save()
    return redirect('get_total', pk=pk)
        
def many_student_updates(request, pk):#tutor
    query = QSUBJECT.objects.filter(tutor__exact=BTUTOR.objects.get(pk=pk))
    students = list(query.values_list('id'))
    ids = [r[0] for r in students]
    for i in range(0, query.count()):
        obj = QSUBJECT.objects.get(pk=ids[i])
        obj.total = obj.test + obj.agn + obj.atd
        obj.agr = obj.exam + obj.total
        obj.grade = grades([obj.agr], cader(obj.tutor.Class))[0]
        obj.save()
    return redirect('position_updates', pk=pk)

@login_required
def annual_agr(request, pk):
    tutor = get_object_or_404(BTUTOR, pk=pk)
    tutor.model_in = 'annual'
    tutor.save()  
    annual_scores = ANNUAL.objects.filter(subject__exact=tutor.subject, student_name__Class__exact=tutor.Class)
    sets = [x[:] for x in list(annual_scores.values_list('id', 'first', 'second', 'third')) if x[-1] != None]
    empty_list = []
    for i in range(0, len(sets)):
        empty_list += [[r for r in sets[i]]]
        try:
            while True:
                empty_list[i][empty_list[i].index(None)] = 0
        except ValueError:
            pass
        empty_list[i] += [sum(empty_list[i][1:4])]
        empty_list[i] += [(sum(empty_list[i][1:4])+0.1)/sum(x > 0 for x in empty_list[i][1:4])]
    single_list = [[i[0] for i in empty_list], [i[4] for i in empty_list], list(map(round, [i[5] for i in empty_list]))]
    posi = don_e(single_list[2][:])
    grd = grades(single_list[2][:], cader(tutor.Class))  
    for r in range(0, len(single_list[0])):#
        get_student = get_object_or_404(ANNUAL, pk=single_list[0][r])
        get_student.anual = single_list[1][r]
        get_student.agr = single_list[2][r]
        get_student.grade = grd[r]
        get_student.anu_posi = posi[r]
        get_student.save()
        obj = QSUBJECT.objects.get(student_name=get_student.student_name, tutor__term__exact=tutor.term, tutor__subject__exact=tutor.subject)
        obj.annual_scores = {str(tutor.subject.name)[:3]+':'+str(single_list[2][r])+':'+str(grd[r])+':'+str(posi[r])+':---:'+str(single_list[1][r])}
        obj.save()  
    return redirect('get_total', pk=pk)
    
def tutor_model_summary(request, pk):
    mains = QSUBJECT.objects.all()
    count_s = mains.count()
    tutors = [i[0] for i in list(set(list(mains.values_list('tutor')))) if i[0] != None]
    for i in range(0, len(tutors)):#
        t = BTUTOR.objects.get(pk=tutors[i])
        avg = round(QSUBJECT.objects.filter(tutor__subject__exact=t.subject, tutor__Class__exact=t.Class, tutor__term__exact=t.term).aggregate(Avg('agr'))['agr__avg'],2)
        count = QSUBJECT.objects.filter(tutor__subject__exact=t.subject, tutor__Class__exact=t.Class, tutor__term__exact=t.term).count()
        t.model_summary = {str(t.teacher_name)+':'+str(t.subject.name)[:3]+':'+str(t.Class)+':'+str(t.term)+':'+str(count)+':'+str(avg)+'%'}
        t.save()
    count_t = BTUTOR.objects.all().count()
    page = request.GET.get('page', 1)
    paginator = Paginator(BTUTOR.objects.all(), 60)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/student_on_all_subjects_detail.html',  {'all_page': all_page, 'count_t': count_t, 'count_s':count_s, 'pk':pk})