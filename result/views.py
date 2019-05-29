
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
from result.grader import grades
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Avg
from result.posi import don_e
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def update_csv(request, pk):
    non_zero = BTUTOR.objects.filter(pk=pk)
    query = QSUBJECT.objects.filter(tutor__exact=None, logged_in=request.user)#new updates by the logged in teacher
    if len(non_zero) != 0:#empty qeryset will populate error
          qry = get_object_or_404(BTUTOR, pk=pk)
          clas = [['', 'JSS 1', 'JSS 2', 'JSS 3', 'SS 1', 'SS 2', 'SS 3'], ['', 'jss_one', 'jss_two', 'jss_three', 'sss_one', 'sss_two', 'sss_three']]
          x = clas[0].index(qry.Class)
          if x <= 3:
              cader = 'j'
          else:
              cader = 's'#TUTORMODEL.objects.get(pk=subject_code)#teacher pk must be used uniqely for single subject of that teacher
          if len(query) != 0: #QuerySet must not return None for the update
             students = list(query.values_list('id', 'student_name', 'logged_in', 'agr'))#unique student ids
             ids = [r[0] for r in students]###############news
             scores = [x[-1] for x in students]
             grade = grades(scores, cader)#######
             for i in range(0, len(students)):
                 obj = get_object_or_404(QSUBJECT, pk=ids[i])#unique student id
                 obj.tutor = get_object_or_404(BTUTOR, pk=pk)
                 obj.grade = grade[i]
                 obj.cader = cader
                 obj.save()
                 if qry.term == '1st Term':
                     ann_scr = ANNUAL(student_name=obj.student_name, first = obj.agr, subject_by=qry, subject=qry.subject, logged_in=request.user, term = '1st Term')
                     ann_scr.save()
                 elif qry.term == '2nd Term':
                     first = ANNUAL.objects.filter(student_name__exact=obj.student_name, term='1st Term', subject_by__Class__exact=qry.Class, subject_by__subject__exact=qry.subject, subject_by__user__exact=request.user).count()
                     if first == 0:#create new record beging from 2nd term 
                         ann_scr = ANNUAL(student_name=obj.student_name, second = obj.agr, subject_by=qry, subject=qry.subject, term = '2nd Term')
                         ann_scr.save()
                     else:#update 1st term on record
                         ann_scr = get_object_or_404(ANNUAL, student_name_id=obj.student_name_id, subject_by__user__exact=request.user, subject_by__subject__exact=qry.subject)
                         ann_scr.second = obj.agr
                         ann_scr.save()
                 elif qry.term == '3rd Term':
                     first = ANNUAL.objects.filter(student_name__exact=obj.student_name, term='1st Term', subject_by__Class__exact=qry.Class, subject_by__subject__exact=qry.subject, subject_by__user__exact=request.user).count()                     
                     if first == 0: 
                         ann_scr = ANNUAL(student_name=obj.student_name, third = obj.agr, subject_by=qry, subject=qry.subject, term = '3rd Term')
                         ann_scr.save()
                     else:#update 1st term on record
                         ann_scr = get_object_or_404(ANNUAL, student_name_id=obj.student_name_id, subject_by__user__exact=request.user, subject_by__subject__exact=qry.subject)
                         ann_scr.third = obj.agr
                         ann_scr.save()
             mains = QSUBJECT.objects.filter(tutor__term__exact=qry.term, tutor__Class__exact=qry.Class, tutor__teacher_name__exact=qry.teacher_name, tutor__user__exact=request.user).order_by('id')
             grade_counter(mains, qry)
             subject_total(mains, qry)
             return redirect('tutor_summary', pk=pk)
          else:
              mains = QSUBJECT.objects.filter(tutor__term__exact=qry.term, tutor__Class__exact=qry.Class, tutor__teacher_name__exact=qry.teacher_name, tutor__user__exact=request.user).order_by('id')      
              count_grade = QSUBJECT.objects.filter(tutor__term__exact=qry.term, tutor__Class__exact=qry.Class, tutor__teacher_name__exact=qry.teacher_name, tutor__user__exact=request.user).count()
              grad = get_object_or_404(RESULT_GRADE, identifier=pk)
              page = request.GET.get('page', 1)
              paginator = Paginator(mains, 60)
              try:
                  all_page = paginator.page(page)
              except PageNotAnInteger:
                  all_page = paginator.page(1)
              except EmptyPage:
                  all_page = paginator.page(paginator.num_pages)
              return render(request, 'result/qsubject.html', {'count_grade': count_grade, 'grad' : grad, 'all_page': all_page,  'qry' : qry, 'pk': pk})
      
    else:
        return render(request, 'result/invalid_pk.html')
  
def subject_total(mains, qry):
    check = TOTAL.objects.filter(subject_by__exact=qry, subject__exact=qry.subject, term__exact=qry.term, subject_by__user__exact=qry.user)
    if len(check) == 0: 
        qar = TOTAL(subject_by=qry, subject=qry.subject, subject_scores=mains.aggregate(Sum('agr'))['agr__sum'], subject_pert=round(mains.aggregate(Avg('agr'))['agr__avg'],2), term=qry.term)
        qar.save()
    else:
        if qry.model_in != 'annual':
            qar = get_object_or_404(TOTAL, subject_by__term__exact=qry.term, subject_by__Class__exact=qry.Class, subject_by__teacher_name__exact=qry.teacher_name, subject_by__user__exact=qry.user)
            qar.subject_scores=mains.aggregate(Sum('agr'))['agr__sum']
            qar.subject_pert=round(mains.aggregate(Avg('agr'))['agr__avg'],2)
            qar.save()
        else:
            sets = [x[:] for x in list(mains.values_list('first', 'second', 'third', 'agr')) if x[-4] != None]
            sd = [list(x) for x in sets]
            qar = get_object_or_404(TOTAL, subject_by__term__exact=qry.term, subject_by__Class__exact=qry.Class, subject_by__teacher_name__exact=qry.teacher_name, subject_by__user__exact=qry.user)
            qar.subject_scores=sum([i[-1] for i in sd])
            qar.subject_pert=round(sum([i[-1] for i in sd])/len([i[-1] for i in sd]),2)
    return qar

@login_required
def annual_agr(request, pk):
    qry = get_object_or_404(BTUTOR, pk=pk)
    qry.model_in = 'annual'
    qry.save()
    clas = [['', 'JSS 1', 'JSS 2', 'JSS 3', 'SS 1', 'SS 2', 'SS 3'], ['', 'jss_one', 'jss_two', 'jss_three', 'sss_one', 'sss_two', 'sss_three']]
    x = clas[0].index(qry.Class)
    if x <= 3:
        cader = 'j'
    else:
        cader = 's'   
    annual_scores = ANNUAL.objects.filter(subject_by__user__exact=request.user, subject_by__Class__exact=qry.Class, subject_by__subject__exact=qry.subject)
    sets = [x[:] for x in list(annual_scores.values_list('id', 'first', 'second', 'third')) if x[-3] != None]
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
    grd = grades(single_list[2][:], cader)
    
    #from django.http import HttpResponse
    #return HttpResponse(len(posi), content_type='text/plain')
    for r in range(0, len(single_list[0])):
        get_student = ANNUAL.objects.get(pk=single_list[0][r])
        get_student.anual = single_list[1][r]
        get_student.agr = single_list[2][r]
        get_student.grade = grd[r]
        get_student.anu_posi = posi[r]
        get_student.save()
    annual_scores = ANNUAL.objects.filter(subject_by__user__exact=request.user, subject_by__Class__exact=qry.Class, subject_by__subject__exact=qry.subject).order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(annual_scores, 60)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    count_grade = len(single_list[0])
    grade_counter(annual_scores, qry)
    grad = qry.graded
    qar = subject_total(annual_scores, qry)
    return render(request, 'result/annual.html',  {'grad' : grad, 'count_grade' : count_grade, 'all_page': all_page, 'qar': qar, 'qry' : qry, 'pk': pk})
    
def tutor_model_summary(request, pk):
    mains = QSUBJECT.objects.all()
    count_s = mains.count()
    tutors = [i[0] for i in list(set(list(mains.values_list('tutor'))))]
    for i in range(0, len(tutors)):
    	t = BTUTOR.objects.get(pk=tutors[i])
    	t.model_summary = {str(t.teacher_name)+':'+str(t.subject.name)+':'+str(t.Class)+':'+str(t.term)+':'+str(QSUBJECT.objects.filter(tutor__subject__exact=t.subject, tutor__Class__exact=t.Class, tutor__term__exact=t.term).count())}
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