# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 20:05:17 2018

@author: AdeolaOlalekan
"""

from .models import QSUBJECT, CNAME, BTUTOR, ANNUAL
from django.shortcuts import render, redirect, get_object_or_404
from result.result_views import cader
from result.grader import grades, don_e
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import teacherform, a_student_form_new, student_name

#####################################STAGE 1:::: CREATE_TUTOR ##########################STARTS
@login_required
def create_new_subject_teacher(request):#New teacher form for every new term, class, subjects, subject_per_name
    if request.method == 'POST':
        result = teacherform(request.POST)
        if result.is_valid():
            unique = BTUTOR.objects.filter(user__exact=request.user, term__exact=result.cleaned_data['term'], Class__exact=result.cleaned_data['Class'], subject = result.cleaned_data['subject']).count()
            first = BTUTOR.objects.filter(user__exact=request.user, term__exact='1st Term', Class__exact=result.cleaned_data['Class'], subject = result.cleaned_data['subject']).count()
            if first != 0 and unique == 0 or result.cleaned_data['term'] == '1st Term' and unique == 0:
                new_teacher = BTUTOR(user=request.user, subject = result.cleaned_data['subject'], Class = result.cleaned_data['Class'], term = result.cleaned_data['term'], teacher_name = result.cleaned_data['teacher_name'], cader=cader(result.cleaned_data['Class']))
                new_teacher.save()
                return redirect('upload_txt', pk=new_teacher.id)
            else:
                others = BTUTOR.objects.filter(user__exact=request.user).order_by('id')
                page = request.GET.get('page', 1)
                paginator = Paginator(others, 60)
                try:
                    all_page = paginator.page(page)
                except PageNotAnInteger:
                    all_page = paginator.page(1)
                except EmptyPage:
                    all_page = paginator.page(paginator.num_pages)
                return render(request, 'result/first_term_record_notify.html', {'all_page':all_page})
    else:
        result = teacherform()
        return render(request, 'result/create_new_teacher.html', {'result': result})

#####################################STAGE 1:::: TUTOR ##########################ENDS


######################STAGE 2 ::: UPLOAD SCORES##################STARTS
def bst_avg(dim):
    result = []
    for i in range(0, len(dim)):
        result += [[int(round((sum(dim[i][0:2])/sum(x > 0 for x in dim[i][0:2])+0.1), 0)), int(round((sum(dim[i][2:4])/sum(x > 0 for x in dim[i][2:4])+0.1), 0)), int(round((sum(dim[i][4:6])/sum(x > 0 for x in dim[i][4:6])+0.1), 0)), int(round((sum(dim[i][6:8])/sum(x > 0 for x in dim[i][6:8])+0.1), 0))]]
    return result 



@login_required
def upload_new_subject_scores(request, pk):
    tutor = get_object_or_404(BTUTOR, pk=pk) 
    if request.method == "POST":
        my_file = request.FILES['files'] # get the uploaded file
        if not my_file.name.endswith('.txt'):
            return render(request, 'result/file_extension_not_txt.html')
        file_txt = my_file.read().decode("ISO-8859-1")
        contents = file_txt.split('\n');
        named_scores = [[], [], []]#[compltet_data_for_each_student, scores, name_only]
        for line in contents:
            each_student = [new.strip() for new in line.split(',')]
            named_scores[0] += [each_student]
        serial_no = [named_scores[0].index(x) for x in named_scores[0]]#get name indexes
        valid_input = [n[:] for n in named_scores[0] if len(n) > 2]
        males = serial_no[-1]#last_no on male list
        females = len(valid_input) - males
        tutor.males = males
        tutor.females = females
        tutor.save()
        for i in range(0, len(valid_input)):
            named_scores[1] += [[int(float(ints)) for ints in valid_input[i][1:]]]#[scores[1]
            named_scores[2] += [valid_input[i][0]]# names[2]]
        if len(named_scores[1][0]) == 8:#BST ONLY: Reduced 8 to 4 columns by averaging.
            x_y = bst_avg(named_scores[1])
            named_scores[1] = x_y
        x = cader(tutor.Class)
        raw = []
        for i in range(0, len(named_scores[1])):
            raw += [[i+1]+named_scores[1][i]+[sum(named_scores[1][i][:3])]+[sum([named_scores[1][i][3]+sum(named_scores[1][i][:3])])]]
        agr = [[i[1:] for i in raw]]
        grade = grades([r[-1] for r in raw][:], x)
        posi = don_e([r[-1] for r in raw][:])
        for i in range(0, len(named_scores[2])):
            name = CNAME.objects.filter(student_name__exact=named_scores[2][i], Class__exact=tutor.Class).count()#if name exits else create name
            if name == 0:
                new_name = CNAME(student_name=named_scores[2][i], Class=tutor.Class)#adding new student_name
                new_name.save()
            per_student = QSUBJECT(student_name=CNAME.objects.get(student_name__exact=named_scores[2][i], Class__exact=tutor.Class), test=agr[0][i][0], agn=agr[0][i][1], atd=agr[0][i][2], exam=agr[0][i][3], total=agr[0][i][4], agr=agr[0][i][5], posi=posi[i], grade=grade[i], tutor = tutor, cader = x)
            per_student.save() 
            create_update_annual_records(per_student, tutor)
    else:#
        return render(request, 'result/loader.html', {'pk':pk, 'qry':tutor})
    ######################STAGE 2 ::: UPLOAD SCORES##################ENDS
    return redirect('tutor_summary', pk=pk)#summarise all tutor's uploads
    

def a_student_exist(request, pk):
    tutor = get_object_or_404(BTUTOR, pk=pk)
    if request.method == 'POST':
        result = a_student_form_new(request.POST)
        if result.is_valid():
            exist_student = QSUBJECT(student_name=CNAME.objects.get(student_name__exact=str(result.cleaned_data['student_name']).split(':')[1]), test=result.cleaned_data['test'], agn=result.cleaned_data['agn'], atd=result.cleaned_data['atd'], exam=result.cleaned_data['exam'], tutor = tutor)
            exist_student.save() 
            return redirect('subject_updates_model', pk=exist_student.id)
    else:
        result = a_student_form_new()
        #group = student_Class()
    return render(request, 'result/a_student_form.html', {'result': result})

def new_student_name(request):
    if request.method == 'POST':
        result = student_name(request.POST)
        if result.is_valid():
            new_name = CNAME(student_name=result.cleaned_data['student_name'], Class=result.cleaned_data['Class'])#adding new student_name
            new_name.save() 
            return redirect('student_names')
    else:
        result = student_name()
    return render(request, 'result/a_student_name.html', {'result': result})

######################STAGE 3 ::: CREATE/UPDATE_ANNUAL SCORES##################STARTS

def create_update_annual_records(obj, tutor):
    if tutor.term == '1st Term':
        ann_scr = ANNUAL(student_name=obj.student_name, first = obj.agr, subject_by=tutor, subject=tutor.subject, term = '1st Term')
        ann_scr.save()
    elif tutor.term == '2nd Term':#update 1st term on record
        first = ANNUAL.objects.filter(student_name__exact=obj.student_name, term='1st Term', subject__exact=obj.tutor.subject).count()
        if first == 0:#create new record beging from 2nd term 
            ann_scr = ANNUAL(student_name=obj.student_name, second = obj.agr, subject_by=tutor, subject=tutor.subject, term = '1st Term')
            ann_scr.save()
        else:#update 1st term on record
            ann_scr = get_object_or_404(ANNUAL, student_name__exact=obj.student_name, subject__exact=obj.tutor.subject, term__exact='1st Term')
            ann_scr.second = obj.agr
            ann_scr.save()
    elif tutor.term == '3rd Term':
        first = ANNUAL.objects.filter(student_name__exact=obj.student_name, term='1st Term', subject__exact=obj.tutor.subject).count()
        if first == 0:#create new record beging from 2nd term 
            ann_scr = ANNUAL(student_name=obj.student_name, third = obj.agr, subject_by=tutor, subject=tutor.subject, term = '3rd Term')
            ann_scr.save()
        else:#update 1st term on record
            ann_scr = get_object_or_404(ANNUAL, student_name__exact=obj.student_name, subject__exact=obj.tutor.subject, term__exact='1st Term')
            ann_scr.third = obj.agr
            ann_scr.term = '3rd Term'
            ann_scr.save()
######################STAGE 2 ::: UPLOAD SCORES##################ENDS     
