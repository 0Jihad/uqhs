
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 08:05:55 2019

@author: AdeolaOlalekan
"""

#from django.http import HttpResponse
#return HttpResponse(len(empty_list), content_type='text/plain')
##############################LOGIN BAIL#######################################
from .models import QSUBJECT, BTUTOR#, RESULT_GRADE#, CNAME
#from .grad_counter import grade_counter
from django.contrib.auth.decorators import login_required 
from result.grader import grades, don_e
from django.shortcuts import render, redirect#, redirect
from django.db.models import Avg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
        
def cader(qry):
    clas = [['', 'JSS 1', 'JSS 2', 'JSS 3', 'SS 1', 'SS 2', 'SS 3'], ['', 'jss_one', 'jss_two', 'jss_three', 'sss_one', 'sss_two', 'sss_three']]
    x = clas[0].index(qry)
    if x <= 3:
        cader = 'j'
    else:
        cader = 's'
    return cader

#@login_required
def single_student_update(request, pk):#student
    obj = QSUBJECT.objects.get(pk=pk)
    if obj.tutor != None:
        obj.total = obj.test + obj.agn + obj.atd
        obj.agr = obj.exam + obj.total
        obj.grade = grades([obj.agr], cader(obj.tutor.Class))[0]
        obj.save()
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
    return redirect('subject_view', pk=pk)
        
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
    paginator = Paginator(BTUTOR.objects.all(), 30)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/student_on_all_subjects_detail.html',  {'all_page': all_page, 'count_t': count_t, 'count_s':count_s, 'pk':pk})


