# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 20:05:17 2018

@author: AdeolaOlalekan
"""
from django.contrib.auth.models import User
from .models import QSUBJECT, CNAME, BTUTOR, ANNUAL, TERM, OVERALL_ANNUAL
from django.shortcuts import render, redirect, get_object_or_404
from result.result_views import cader
from result.grader import grades, don_e
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import teacherform, a_student_form_new, student_name
from datetime import datetime
from .grad_counter import grade_counter
from django.db.models import Sum, Avg
#####################################STAGE 1:::: CREATE_TUTOR ##########################STARTS 
@login_required
def create_new_subject_teacher(request):#New teacher form for every new term, class, subjects, subject_per_name
    if request.method == 'POST':
        result = teacherform(request.POST)
        if result.is_valid():
            unique = BTUTOR.objects.filter(accounts__exact=request.user, term__exact=result.cleaned_data['term'], Class__exact=result.cleaned_data['Class'], subject = result.cleaned_data['subject']).count()
            first = BTUTOR.objects.filter(accounts__exact=request.user, term__exact='1st Term', Class__exact=result.cleaned_data['Class'], subject = result.cleaned_data['subject']).count()
            if first != 0 and unique == 0 or result.cleaned_data['term'] == '1st Term' and unique == 0:
                new_teacher = BTUTOR(accounts=request.user, subject = result.cleaned_data['subject'], Class = result.cleaned_data['Class'], term = result.cleaned_data['term'], teacher_name = result.cleaned_data['teacher_name'], teacher_in = result.cleaned_data['teacher_in'], cader=cader(result.cleaned_data['Class']), session=result.cleaned_data['session'])
                new_teacher.save()
                return redirect('upload_txt', pk=new_teacher.id)
            else:
                others = BTUTOR.objects.filter(accounts__exact=request.user).order_by('id')
                page = request.GET.get('page', 1)
                paginator = Paginator(others, 30)
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
        
    else:#
        return render(request, 'result/loader.html', {'pk':pk, 'qry':tutor})
    ######################STAGE 2 ::: UPLOAD SCORES##################ENDS
    return redirect('tutor_summary', pk=pk)#summarise all tutor's uploads
    

def a_student_exist(request, pk):
    tutor = get_object_or_404(BTUTOR, pk=pk)
    if request.method == 'POST':
        result = a_student_form_new(request.POST)
        if result.is_valid():
            exist_student = QSUBJECT(student_name=CNAME.objects.get(student_name__exact=str(result.cleaned_data['student_name']).split(':')[1]), test=result.cleaned_data['test'], agn=result.cleaned_data['agn'], atd=result.cleaned_data['atd'], exam=result.cleaned_data['exam'], tutor = tutor, session = tutor.session)
            exist_student.save() 
            return redirect('subject_updates_model', pk=exist_student.id)
    else:
        result = a_student_form_new()
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
@login_required
def compute_annual(request, pk):
    tutor = get_object_or_404(BTUTOR, pk=pk)
    if tutor.model_in == 'qsubject' or tutor.model_in == 'annual':
        subject = QSUBJECT.objects.filter(tutor__subject__exact=tutor.subject, tutor__Class__exact=tutor.Class, tutor__term__exact='3rd Term')
        student_name_ids = [list(i[:]) for i in list(subject.values_list('student_name_id'))]
        for i in range(0, len(student_name_ids)):
            student_name = CNAME.objects.get(pk=student_name_ids[i][0], Class = tutor.Class)
            sub1 = QSUBJECT.objects.filter(student_name=student_name, tutor__Class__exact=tutor.Class, tutor__subject__exact=tutor.subject, tutor__term__exact='1st Term')
            if sub1.count() != 0:
                first = QSUBJECT.objects.get(student_name=student_name, tutor__Class__exact=tutor.Class, tutor__subject__exact=tutor.subject, tutor__term__exact='1st Term')
                f = first.agr
            else:
                f = None# No first term
                first = None
            sub2 = QSUBJECT.objects.filter(student_name=student_name, tutor__Class__exact=tutor.Class, tutor__subject__exact=tutor.subject, tutor__term__exact='2nd Term')
            if sub2.count() != 0:
                second = QSUBJECT.objects.get(student_name=student_name, tutor__Class__exact=tutor.Class, tutor__subject__exact=tutor.subject, tutor__term__exact='2nd Term')
                s = second.agr
            else:
                s = None# No second term
                second = None
            
            third = QSUBJECT.objects.get(student_name=student_name, tutor__Class__exact=tutor.Class, tutor__subject__exact=tutor.subject, tutor__term__exact='3rd Term')
            dim = [f, s, third.agr]
            try:
                while True:
                    dim[dim.index(None)] = 0
            except ValueError:
                pass
            sd = [sum(dim), round((sum(dim[:])+0.1)/sum(x > 0 for x in dim[:]), 2)]
            if ANNUAL.objects.filter(subject_by__exact = tutor, student_name__exact=student_name, subject__exact=tutor.subject).count() == 0:
                ANNUAL(subject_by = tutor, student_name=student_name, subject=tutor.subject, first = first, second = second, third = third, anual = sd[0], agr = sd[1]).save()
            else:
                get_filt = ANNUAL.objects.get(subject_by = tutor, student_name=student_name, subject=tutor.subject)
                get_filt.first = first
                get_filt.second = second
                get_filt.third = third
                get_filt.save()
            if TERM.objects.filter(student_name__exact=student_name, class_in__exact=tutor.Class, terms_by__exact = tutor, subject__exact=tutor.subject.name).count() == 0:
                term_scores = TERM.objects.create(student_name=student_name, class_in=tutor.Class, terms_by = tutor, subject=tutor.subject.name, first=first, second=second, third=third)
            else:
                term_scores = TERM.objects.get(student_name=student_name, class_in=tutor.Class, terms_by = tutor, subject=tutor.subject.name)
            term_scores.save()
            if OVERALL_ANNUAL.objects.filter(student_name__exact=student_name, class_in__exact=tutor.Class, teacher_in__exact=tutor.teacher_in).count() == 0:
                subj = OVERALL_ANNUAL.objects.create(student_name=student_name, class_in=tutor.Class, teacher_in=tutor.teacher_in, eng = None, mat = None, agr = None, bus = None, bst = None, yor = None, nva = None, irs = None, prv = None, ict = None, acc = None, his = None)
            else:
                subj = get_object_or_404(OVERALL_ANNUAL, student_name=student_name, class_in=tutor.Class, teacher_in=tutor.teacher_in)
            term_scores.avr = sd[1]
            subj.save()
            term_scores.save()
            class_records(tutor, subj, term_scores)
            #third.annual_scores = {str(tutor.subject.name)[:3]+':'+str(first.agr)+':'+str(first.grade)+':'+str(first.posi)+':---:'+str(second.agr)+':'+str(second.grade)+':'+str(second.posi)+':---:'+str(third.agr)+':'+str(third.grade)+':'+str(third.posi)}
            #third.save()
        anu = ANNUAL.objects.filter(subject_by__Class=tutor.Class, subject__exact=tutor.subject, subject_by__session=tutor.session)
        name_ids = [list(i[:]) for i in list(anu.values_list('id', 'agr'))]
        scores = [round(x[1], 0) for x in name_ids]
        posi = don_e(scores[:])
        grd = grades(scores[:], cader(tutor.Class)) 
        for r in range(0, len(name_ids)):#
            get_student = get_object_or_404(ANNUAL, pk=name_ids[r][0])
            get_student.grade = grd[r]
            get_student.anu_posi = posi[r]
            get_student.save()
    all_t = TERM.objects.filter(terms_by__exact=tutor, class_in__exact=tutor.Class, subject__exact=tutor.subject.name).order_by('id')
    tutor.model_in =  'annual'
    tutor.save()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_t, 30)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/only.html',  {'all_page': all_page, 'in_class': all_t.count(), 'pk':pk, 'tutor':tutor})

    ######################STAGE 2 ::: UPLOAD SCORES##################ENDS  
def show_annual(request, pk):
    tutor = get_object_or_404(BTUTOR, pk=pk)
    all_t = TERM.objects.filter(terms_by__exact=tutor, class_in__exact=tutor.Class, subject__exact=tutor.subject.name).order_by('id')
    tutor.model_in =  'annual'
    tutor.save()
    return render(request, 'result/all_only.html',  {'all_page': all_t, 'in_class': all_t.count(), 'pk':pk, 'tutor':tutor})


def class_records(tutor, subj, term_scores):
    if tutor.subject.name == 'English':
        subj.eng = term_scores
    elif tutor.subject.name == 'Mathematics':
        subj.mat = term_scores
    elif tutor.subject.name == 'Agric. Sc.' and tutor.Class == 'JSS 1' or tutor.Class == 'JSS 2' or tutor.Class == 'JSS 3':
        subj.agr = term_scores
    elif tutor.subject.name == 'Business Studies' or tutor.subject.name == 'Litrature' or tutor.subject.name == 'Commerce' or tutor.subject.name == 'Physics':
        subj.bus = term_scores
    elif tutor.subject.name == 'Basic Science and Technology' or tutor.subject.name == 'Economics' or tutor.subject.name == 'Biology':
        subj.bst = term_scores
    elif tutor.subject.name == 'Geography' or tutor.subject.name == 'Yoruba' or tutor.subject.name == 'Agric. Sc.':
        subj.yor = term_scores
    elif tutor.subject.name == 'Civic Education' or tutor.subject.name == 'National Value':
        subj.nva = term_scores
    elif tutor.subject.name == 'Islamic Studies':
        subj.irs = term_scores
    elif tutor.subject.name == 'Electrical' or tutor.subject.name == 'Garment Making' or tutor.subject.name == 'Catering' or tutor.subject.name == 'Pre-Vocation':
        subj.prv = term_scores
    elif tutor.subject.name == 'Government' or tutor.subject.name == 'Information Technology':
        subj.ict = term_scores
    elif tutor.subject.name == 'Account' or tutor.subject.name == 'Chemistry' or tutor.subject.name == 'Arabic':
        subj.acc = term_scores
    elif tutor.subject.name == 'History':
        subj.his = term_scores
    subj.session = str(datetime.now().year)
    subj.save()
    
def broad_sheet(request):
    al = OVERALL_ANNUAL.objects.filter(teacher_in__exact=request.user, class_in__exact=request.user.profile.class_in, session__exact=str(datetime.now().year))
    if al.count() != 0:
        x = list(al.values_list('id', 'eng', 'mat', 'agr', 'bus', 'bst', 'yor', 'nva', 'irs', 'prv', 'ict', 'acc', 'his'))
        lst = [list(i[:]) for i in x]
        for i in range(0, len(lst)):
            ds = []
            try:
                while True:
                    lst[i][lst[i].index(None)] = 0
            except ValueError:
                pass         
            for r in range(1, len(lst[i])):
                if lst[i][r] != 0:
                    ds += [TERM.objects.get(pk=lst[i][r]).avr]
                    if i == 0:
                        teacher_id = BTUTOR.objects.get(pk=TERM.objects.get(pk=lst[i][r]).third.tutor.id)
                        teacher_id.class_teacher_id = request.user.id
                        teacher_id.save()
            gets = OVERALL_ANNUAL.objects.get(pk=lst[i][0])
            gets.Agr = round(sum(ds), 2)
            gets.Avr = round(sum(ds)/len(ds), 2)
            gets.save()
            
        name_ids = [list(i[:]) for i in list(al.values_list('id', 'Avr'))]
        scores = [round(x[1], 0) for x in name_ids]
        posi = don_e(scores[:])
        grd = grades(scores[:], cader(gets.class_in)) 
        for x in range(0, len(name_ids)):#
            get_student = get_object_or_404(OVERALL_ANNUAL, pk=name_ids[x][0])
            get_student.grade = grd[x]
            get_student.posi = posi[x]
            get_student.save()
        page = request.GET.get('page', 1)
        paginator = Paginator(al, 30)
        total_scores = round(al.aggregate(Sum('Avr'))['Avr__sum'], 1)
        avg_pert = round(al.aggregate(Avg('Avr'))['Avr__avg'],2)
        grad = grade_counter(al, request.user.id, 'BroadSheet')
        try:
            all_page = paginator.page(page)
        except PageNotAnInteger:
            all_page = paginator.page(1)
        except EmptyPage:
            all_page = paginator.page(paginator.num_pages)
    else:
        return redirect('home')
    if request.user.profile.class_in == 'SS 1' or request.user.profile.class_in == 'SS 2' or request.user.profile.class_in == 'SS 3':
        return render(request, 'result/broadsheet.html',  {'date': datetime.now(), 'grad':grad, 'total_scores':total_scores, 'avg_pert':avg_pert, 'all_page': all_page, 'in_class': al.count(), 'last_name':request.user.profile.last_name, 'first_name':request.user.profile.first_name, 'class_in':request.user.profile.class_in })
    else:
        return render(request, 'result/jyearly.html',  {'date': datetime.now(), 'grad':grad, 'total_scores':total_scores, 'avg_pert':avg_pert, 'all_page': all_page, 'in_class': al.count(), 'last_name':request.user.profile.last_name, 'first_name':request.user.profile.first_name, 'class_in':request.user.profile.class_in })

def broad_sheet_on_page(request):
    al = OVERALL_ANNUAL.objects.filter(teacher_in__exact=request.user, class_in__exact=request.user.profile.class_in, session__exact=str(datetime.now().year))
    if al.count() != 0:
        total_scores = round(al.aggregate(Sum('Avr'))['Avr__sum'], 1)
        avg_pert = round(al.aggregate(Avg('Avr'))['Avr__avg'],2)
        grad = grade_counter(al, request.user.id, 'BroadSheet')
    else:
        return redirect('home')
    if request.user.profile.class_in == 'SS 1' or request.user.profile.class_in == 'SS 2' or request.user.profile.class_in == 'SS 3':
        return render(request, 'result/syearly_apage.html',  {'date': datetime.now(), 'grad':grad, 'total_scores':total_scores, 'avg_pert':avg_pert, 'all_page': al, 'in_class': al.count(), 'last_name':request.user.profile.last_name, 'first_name':request.user.profile.first_name, 'class_in':request.user.profile.class_in })
    else:
        return render(request, 'result/jyearly_apage.html',  {'date': datetime.now(), 'grad':grad, 'total_scores':total_scores, 'avg_pert':avg_pert, 'all_page': al, 'in_class': al.count(), 'last_name':request.user.profile.last_name, 'first_name':request.user.profile.first_name, 'class_in':request.user.profile.class_in })

def broad_sheet_views(request, pk):
    user = get_object_or_404(User, pk=get_object_or_404(BTUTOR, pk=pk).class_teacher_id)
    al = OVERALL_ANNUAL.objects.filter(teacher_in__exact=user, class_in__exact=user.profile.class_in, session__exact=datetime.now().year)
    if al.count() != 0:
        total_scores = round(al.aggregate(Sum('Avr'))['Avr__sum'], 1)
        avg_pert = round(al.aggregate(Avg('Avr'))['Avr__avg'],2)
        grad = grade_counter(al, request.user.id, 'BroadSheet')
    else:
        return redirect('home')   
    if user.profile.class_in == 'SS 1' or user.profile.class_in == 'SS 2' or user.profile.class_in == 'SS 3':
        return render(request, 'result/syearly_apage.html',  {'date': datetime.now(), 'grad':grad, 'total_scores':total_scores, 'avg_pert':avg_pert, 'all_page': al, 'in_class': al.count(), 'last_name':user.profile.last_name, 'first_name':user.profile.first_name, 'class_in':user.profile.class_in })
    else:
        return render(request, 'result/jyearly_apage.html',  {'date': datetime.now(), 'grad':grad, 'total_scores':total_scores, 'avg_pert':avg_pert, 'all_page': al, 'in_class': al.count(), 'last_name':user.profile.last_name, 'first_name':user.profile.first_name, 'class_in':user.profile.class_in })
