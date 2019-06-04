# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 00:51:16 2019

@author: AdeolaOlalekan
"""
from .models import QSUBJECT, Edit_User, ASUBJECTS, TOTAL, ANNUAL, BTUTOR, CNAME, RESULT_GRADE
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import csv
#from result.model_views import cader
from .grad_counter import grade_counter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import login_form, ProfileForm, tutor_class_Form, student_names, subjectforms, subject_class_term_Form, name_class_Form
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required#, @permission_required
from django.contrib.auth.forms import AdminPasswordChangeForm#, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from django.db.models import Sum
from django.forms import modelformset_factory
from result.result_views import tot
####################################STAGE 1::::#########TUTOR GET LOG IN OR SIGN UP##########################################   


def loggin(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = auth.authenticate(username=username, password=password)
        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('admin_page')
        else:
            return redirect('home')
    else:
        form = login_form()
    return render(request, 'registration/log_in.html', {'form': form})

def logout(request):
    auth.logout(request)
    return render(request,'registration/logout.html')

def admin_page(request):
    if not request.user.is_authenticated:
        return redirect('logins')
    return render(request, 'registration/admin.html')

################################UPDATING USER ACCOUNT###############################################
@login_required
def password(request):
    PasswordForm = AdminPasswordChangeForm
    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logins')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'registration/password.html', {'form': form})



##################################DOWNLOAD MANAGMENTS##############################################    
def export_name_text(request, pk):#result download based on login tutor
    response = HttpResponse(content_type='text')
    response['Content-Disposition'] = 'attachment; filename="student_names.txt"'
    writer = csv.writer(response)
    #writer.writerow(['student_name'])
    tutor = get_object_or_404(BTUTOR, pk=pk)
    subject = QSUBJECT.objects.filter(tutor__exact=tutor).values_list('student_name')
    sd = [list(x) for x in subject]
    for i in range(0, len(sd)):
    	sd[i][0] = CNAME.objects.get(pk=sd[i][0]).student_name
    for each in sd:
        writer.writerow(each)
    return response  

def export_subject_scores(request, pk):#result download based on login tutor
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scores.csv"'
    writer = csv.writer(response)
    writer.writerow(['student_name', 'test', 'agn', 'atd', 'total', 'exam', 'agr', 'grade', 'posi'])
    tutor = get_object_or_404(BTUTOR, pk=pk)
    subject = QSUBJECT.objects.filter(tutor__exact=tutor).values_list('student_name', 'test', 'agn', 'atd', 'total', 'exam', 'agr', 'grade', 'posi')
    sd = [list(x) for x in subject]
    for i in range(0, len(sd)):
    	sd[i][0] = CNAME.objects.get(pk=sd[i][0]).student_name
    for each in sd:
        writer.writerow(each)
    return response    

def export_annual_scores(request, pk):#result download based on login tutor
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="annual.csv"'
    writer = csv.writer(response)
    writer.writerow(['student_name', 'first', 'second', 'third', 'anual', 'agr', 'grade', 'anu_posi'])
    tutor = get_object_or_404(BTUTOR, pk=pk)
    subject = ANNUAL.objects.filter(subject__exact=tutor.subject, subject_by__Class__exact=tutor.Class, term__exact='3rd Term')
    sets = [x[:] for x in list(subject.values_list('student_name', 'first', 'second', 'third', 'anual', 'agr', 'grade', 'anu_posi')) if x[3] != None]
    sd = [list(x) for x in sets]
    for i in range(0, len(sd)):
    	sd[i][0] = CNAME.objects.get(pk=sd[i][0]).student_name
    for each in sd:
        writer.writerow(each)
    return response    
###############################################################################
def create_subjects(request):#New teacher form for every new term, class, subjects
    if request.method == 'POST':
        result = subjectforms(request.POST)
        if result.is_valid():
            check = ASUBJECTS.objects.filter(name__exact=result.cleaned_data['name'])
            if len(check) == 0: 
                new_subject = ASUBJECTS(name=result.cleaned_data['name'])
                new_subject.save()
                check = ASUBJECTS.objects.all().order_by('id')
                return render(request, 'result/created_subject.html', {'check':check})
            else:
                check = ASUBJECTS.objects.all().order_by('id')
                return render(request, 'result/created_subject.html', {'check' : check})
    else:
        result = subjectforms()
    return render(request, 'result/create_new_subject.html', {'result': result})
#########################################################
def created_subjects(request, pk):#New teacher form for every new term, class, subjects
    if pk == '0':
        check = ASUBJECTS.objects.all().order_by('id')
        return render(request, 'result/created_subject.html', {'check':check})
        
    else:
        subject = QSUBJECT.objects.filter(tutor__subject__exact=ASUBJECTS.objects.get(pk=pk)).order_by('id')
        count_grade = QSUBJECT.objects.filter(tutor__subject__exact=ASUBJECTS.objects.get(pk=pk)).count()
    page = request.GET.get('page', 1)
    paginator = Paginator(subject, 60)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/subject_in_all.html',  {'count_grade' : count_grade, 'all_page': all_page, 'pk' : pk})




def home(request):#Step 1:: list of tutor's subjects with class, term
    """
    Home page for every tutor!
    """
    # If a tutor is authenticated then redirect them to the tutor's page
    if request.user.is_authenticated:#a tutor page
        tutor = BTUTOR.objects.filter(user=request.user).order_by('Class')
        #mains = QSUBJECT.objects.filter(term__term__exact=qry.term, term__Class__exact=qry.Class, term__teacher_name__exact=qry.teacher_name).order_by('grade')
        return render(request, 'result/tutor.html', {'tutor':tutor})
    else:#general login page
        return redirect('logins') 


def subject_home(request, pk_code):#Step 1:: list of tutor's subjects with class, term
    """
    Home page for every subject!
    """
    if pk_code[len(pk_code)-2:] == 'C1':
        tutor = BTUTOR.objects.filter(Class__exact=BTUTOR.objects.get(pk=pk_code[:len(pk_code)-2]).Class).order_by('Class')
    elif pk_code[len(pk_code)-2:] == 'T1':
        tutor = BTUTOR.objects.filter(term__exact=BTUTOR.objects.get(pk=pk_code[:len(pk_code)-2]).term).order_by('Class')
    else:
        tutor = BTUTOR.objects.filter(subject__exact=BTUTOR.objects.get(pk=pk_code[:len(pk_code)-2]).subject).order_by('Class')
    if tutor.count() != 0:    
        return render(request, 'result/tutor_class_filter.html', {'tutors':tutor})
    else:
        return redirect('home') 
    
def subject_class_term_filter(request):#New teacher form for every new term, class, subjects
    if request.method == 'POST':
        result = subject_class_term_Form(request.POST)
        if result.is_valid():
            if result.cleaned_data['subject'] != None and result.cleaned_data['Class'] == None and result.cleaned_data['term'] == None:
                tutor = BTUTOR.objects.filter(subject__exact=ASUBJECTS.objects.get(name=result.cleaned_data['subject']))
            elif result.cleaned_data['Class'] != None and result.cleaned_data['term'] == None and result.cleaned_data['subject'] == None:
                tutor = BTUTOR.objects.filter(Class__exact=result.cleaned_data['Class'])
            elif result.cleaned_data['term'] != None and result.cleaned_data['subject'] == None and result.cleaned_data['subject'] == None:
                tutor = BTUTOR.objects.filter(term__exact=result.cleaned_data['term'])
            elif result.cleaned_data['subject'] != None and result.cleaned_data['Class'] != None and result.cleaned_data['term'] == None:
                tutor = BTUTOR.objects.filter(subject__exact=ASUBJECTS.objects.get(name=result.cleaned_data['subject']), Class__exact=result.cleaned_data['Class'])
            elif result.cleaned_data['Class'] != None and result.cleaned_data['term'] != None and result.cleaned_data['subject'] == None:
                tutor = BTUTOR.objects.filter(Class__exact=result.cleaned_data['Class'], term__exact=result.cleaned_data['term'])
            elif result.cleaned_data['term'] != None and result.cleaned_data['subject'] != None and result.cleaned_data['subject'] == None:
                tutor = BTUTOR.objects.filter(subject__exact=ASUBJECTS.objects.get(name=result.cleaned_data['subject']), term__exact=result.cleaned_data['term'])
            else:
                if result.cleaned_data['term'] != None and result.cleaned_data['subject'] != None and result.cleaned_data['subject'] != None:
                    tutor = BTUTOR.objects.filter(subject__exact=result.cleaned_data['subject'], term__exact=result.cleaned_data['term'], Class__exact=result.cleaned_data['Class'])
                else:
                    tutor = BTUTOR.objects.all()
            if tutor.count() != 0:    
                return render(request, 'result/tutor_class_filter.html', {'tutors':tutor})
            else:
                return redirect('home') 
    else:
        result = subject_class_term_Form()
    return render(request, 'result/class_filter.html', {'result': result})


def sSum(subjects):
    anuual = subjects.aggregate(Sum('agr'))['agr__sum']
    return anuual


def student_name_class_filter(request):#New teacher form for every new term, class, subjects
    if request.method == 'POST':
        result = name_class_Form(request.POST)
        if result.is_valid():
            student_class = CNAME.objects.get(pk=int(int(str(result.cleaned_data['student_name']).split(':')[0])))
            if student_class.Class == result.cleaned_data['Class']:
                subjects = QSUBJECT.objects.filter(student_name_id__exact=int(str(result.cleaned_data['student_name']).split(':')[0]))
                anuual = sSum(subjects)
                return render(request, 'result/single_subject_per_student.html', {'subjects':subjects, 'name': student_class, 'anuual':anuual})
            else:
                return redirect('student_name_class_filter') 
    else:
        result = name_class_Form()
    return render(request, 'result/class_filter.html', {'result': result})  


def tutor_class_filter(request):#New teacher form for every new term, class, subjects
    if request.method == 'POST':
        result = tutor_class_Form(request.POST)
        if result.is_valid():
            tutor = BTUTOR.objects.filter(teacher_name__exact=BTUTOR.objects.get(pk=int(str(result.cleaned_data['tutor']).split(':')[0])).teacher_name, cader__exact=result.cleaned_data['cader'])
            return render(request, 'result/tutor_class_filter.html', {'tutors':tutor})
        else:
            return redirect('tutor_class_filter') 
    else:
        result = tutor_class_Form()
    return render(request, 'result/class_filter.html', {'result': result}) 
            
def Teacher_model_result_grades(request, pk):##Step 2::  every tutor home detail views
    grad = get_object_or_404(RESULT_GRADE, identifier=pk)
    grad.save()

def detailView(request, pk):##Step 2::  every tutor home detail views
    tutor = get_object_or_404(BTUTOR, pk=pk)
    mains = QSUBJECT.objects.filter(tutor__exact=tutor).order_by('id')#request.user
    count_grade = QSUBJECT.objects.filter(tutor__exact=tutor).count()
    grade_counter(mains, tutor)
    grad = get_object_or_404(RESULT_GRADE, identifier = tutor.id, subject = tutor.subject.name)
    page = request.GET.get('page', 1)
    paginator = Paginator(mains, 60)
    tot(mains, pk)
    qar = get_object_or_404(TOTAL, subject_by__exact=tutor)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/qsubject.html',  {'grad' : grad, 'count_grade' : count_grade, 'all_page': all_page, 'qar': qar, 'qry' : tutor, 'pk': pk})


def annual_view(request, pk):##Step 2::  every tutor home detail views
    tutor = get_object_or_404(BTUTOR, pk=pk)
    mains = ANNUAL.objects.filter(subject_by__Class__exact=tutor.Class, subject__exact=tutor.subject).order_by('id')#request.user
    count_grade = ANNUAL.objects.filter(subject_by__Class__exact=tutor.Class, subject__exact=tutor.subject).count()
    if tutor.term == '3rd Term':
        return redirect('get_total', pk=pk)
    page = request.GET.get('page', 1)
    paginator = Paginator(mains, 60)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/annual_view.html',  {'count_grade' : count_grade, 'all_page': all_page, 'qry' : tutor, 'pk': pk})

def name_per_subject(request, pk):#student subject detail(single term)
    many = QSUBJECT.objects.filter(student_name_id__exact=pk)
    if many.count() != 0:
        ids = list(many.values_list('id'))
        one_by_one = get_object_or_404(QSUBJECT, pk=ids[-1][0])
    else:
        one_by_one = get_object_or_404(QSUBJECT, pk=pk)
    return render(request, 'result/subject_per_name.html',  {'qry': one_by_one, 'many': many})  



def student_in_None(request):#student subject detail(single term)
    subjects = QSUBJECT.objects.filter(tutor__id__exact=None)
    count_grade = subjects.count()
    paginator = Paginator(subjects, 60)
    page = request.GET.get('page', 1)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/qsubject_none.html',  {'all_page' : all_page, 'count_grade':count_grade})    



def group_by_grade(request, pk_code):##Step 2::  every tutor home detail views
    pk=pk_code[:len(pk_code)-2]
    tutor = get_object_or_404(BTUTOR, pk=pk_code[:len(pk_code)-2])
    total = get_object_or_404(TOTAL, subject_by__exact=tutor)
    grad = get_object_or_404(RESULT_GRADE, identifier=pk)
    if grad.remark == False:
        if tutor.Class == 'JSS 1' or tutor.Class == 'JSS 2' or tutor.Class == 'JSS 3':
            mains = QSUBJECT.objects.filter(tutor__exact=tutor, grade=pk_code[-2])
        else:
            mains = QSUBJECT.objects.filter(tutor__exact=tutor, grade=pk_code[len(pk_code)-2:])
    elif grad.remark == True:
        mains = ANNUAL.objects.filter(subject__exact=tutor.subject, student_name__Class__exact=tutor.Class, grade=pk_code[-2])
    count_grade = mains.count()
    paginator = Paginator(mains, 60)
    page = request.GET.get('page', 1)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    if grad.remark == False:
        return render(request, 'result/qsubject.html',  {'grad' : grad, 'count_grade' : count_grade, 'all_page': all_page, 'qar': total, 'qry' : tutor, 'pk': pk})
    elif grad.remark == True:
        return render(request, 'result/annual.html', {'grad': grad, 'count_grade' : count_grade, 'qar' : total, 'qry': tutor, 'all_page': all_page, 'pk':pk})

def list_tutor_subjects(request, pk):##Step 2::  every tutor home detail views
    qry = BTUTOR.objects.get(pk=pk)
    mains = QSUBJECT.objects.filter(tutor__subject__exact=qry.subject)
    counts = mains
    page = request.GET.get('page', 1)

    paginator = Paginator(mains, 60)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/list_tutor_subjects.html',  {'all_page': all_page, 'counts': counts, 'qry':qry})

def Student_names_list(request):##Step 2::  every tutor home detail views
    mains = CNAME.objects.all()
    counts = mains.count()
    page = request.GET.get('page', 1)

    paginator = Paginator(mains, 60)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/student_name_list.html',  {'all_page': all_page, 'counts': counts})

def student_on_all_subjects_list(request, pk):##Step 2::  every tutor home detail views
    
    if pk == '0':
        mains = QSUBJECT.objects.all().order_by('posi')
        tutors = len([i[0] for i in list(set(list(mains.values_list('tutor'))))])
        counts = mains.count()
        page = request.GET.get('page', 1)
        paginator = Paginator(mains, 60)
        try:
            all_page = paginator.page(page)
        except PageNotAnInteger:
            all_page = paginator.page(1)
        except EmptyPage:
            all_page = paginator.page(paginator.num_pages)
        return render(request, 'result/student_on_all_subjects_list.html',  {'all_page': all_page, 'counts': counts, 'tutors':tutors})
    else:
        tutors = BTUTOR.objects.all()
        mains = QSUBJECT.objects.all().order_by('posi')
        count_s = mains.count()
        count_t = tutors.count()
        page = request.GET.get('page', 1)
        paginator = Paginator(tutors, 60)
        try:
            all_page = paginator.page(page)
        except PageNotAnInteger:
            all_page = paginator.page(1)
        except EmptyPage:
            all_page = paginator.page(paginator.num_pages)
        return render(request, 'result/student_on_all_subjects_detail.html',  {'all_page': all_page, 'count_t': count_t, 'count_s':count_s})
    
def student_subject_list(request, pk):##Step 2::  every tutor home detail views
    name = CNAME.objects.get(pk=pk)
    mains = QSUBJECT.objects.filter(student_name_id=name.id)
    ids = list(mains.values_list('id'))
    counts = mains
    page = request.GET.get('page', 1)

    paginator = Paginator(mains, 60)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/student_subject_list.html',  {'all_page': all_page, 'counts': counts, 'name': name, 'pk': ids[0][0]})

def student_subject_detail_one_subject(request, pk):#student subject detail(single term)
    many = get_object_or_404(QSUBJECT, pk=pk)
    subjects = QSUBJECT.objects.filter(student_name_id = many.student_name_id, tutor__subject__exact=many.tutor.subject)
    anuual = sSum(subjects)
    return render(request, 'result/single_subject_per_student.html',  {'subjects' : subjects, 'name':many, 'anuual':anuual, 'pk':pk}) 

def student_subject_detail_all_subject(request, pk):#student subject detail(single term)
    many = get_object_or_404(QSUBJECT, pk=pk)
    subjects = QSUBJECT.objects.filter(student_name_id = many.student_name_id)
    anuual = sSum(subjects)
    return render(request, 'result/single_subject_per_student.html',  {'subjects' : subjects, 'name':many, 'anuual':anuual, 'pk':pk}) 

##########################PORTAL MANAGEMENT####################################


def teacher_accounts(request):
    tutors = BTUTOR.objects.all().order_by('Class')
    page = request.GET.get('page', 1)

    paginator = Paginator(tutors, 60)
    try:
        tutor = paginator.page(page)
    except PageNotAnInteger:
        tutor = paginator.page(1)
    except EmptyPage:
        tutor = paginator.page(paginator.num_pages)
    return render(request, 'result/all_tutor.html', {'tutor': tutor})


def results_junior_senior(request, pk):
    cls = ['JSS 1', 'JSS 2', 'JSS 3', 'SS 1', 'SS 2', 'SS 3']
    tutors = BTUTOR.objects.filter(Class__exact=cls[int(pk)]).order_by('Class')
    return render(request, 'result/results_junior_senior.html', {'tutor': tutors})
   
def confirm_deletion(request, pk):#delete single candidate
    qry = get_object_or_404(QSUBJECT, pk=pk)
    return render(request, 'result/confirm_delete_a_student.html', {'qry' : qry, 'pk': pk})

def student_record_delete(request, pk):#delete single candidate
    get_student = ANNUAL.objects.get(student_name=get_object_or_404(QSUBJECT, pk=pk).student_name)
    get_student.third = None
    get_student.term = None
    get_object_or_404(QSUBJECT, pk=pk).delete()
    return redirect('home')

def confirm_deletions(request, pk):#delete single subject
    qry = get_object_or_404(BTUTOR, pk=pk)
    qery =  QSUBJECT.objects.filter(tutor__term__exact=qry.term, tutor__Class__exact=qry.Class, tutor__teacher_name__exact=qry.teacher_name, tutor__user__exact=request.user)
    return render(request, 'result/confirm_deletes_a_class.html', {'qery' : qery, 'pk': pk, 'qry' : qry})

def delete_all(request, pk):#delete single subject
    qry = get_object_or_404(BTUTOR, pk=pk)
    QSUBJECT.objects.filter(tutor__term__exact=qry.term, tutor__Class__exact=qry.Class, tutor__teacher_name__exact=qry.teacher_name, tutor__user__exact=request.user).delete()
    TOTAL.objects.filter(subject_by__exact=qry, subject__exact=qry.subject, term__exact=qry.term).delete()
    #RESULT_GRADE.objects.get(identifier=pk#).delete()
    qry.delete()
    return redirect('home')

def confirm_deletion_anu(request, pk):
    qry = get_object_or_404(ANNUAL, pk=pk)
    return render(request, 'result/confirm_delete_anuual.html', {'qry' : qry, 'pk': pk})   
def annual_record_delete(request, pk):#delete single candidate
    qry = get_object_or_404(ANNUAL, pk=pk)
    qry.delete()
    return redirect('home')


def term_summary(request, pk):#student subject detail(all terms)
    terms = QSUBJECT.objects.filter(tutor__user__exact=request.user, student_name=pk).values_list('id')
    sub = get_object_or_404(QSUBJECT, id=terms[0][0])#one subject
    anu = ANNUAL.objects.filter(student_name = pk, subject=sub.tutor.subject, subject_by__user__exact=request.user)
    if len(terms) == 3:
        first = QSUBJECT.objects.filter(id=terms[0][0])
        second = QSUBJECT.objects.filter(id=terms[1][0])
        #third = QSUBJECT.objects.filter(id=terms[2][0]) 
    elif len(terms) == 2:
        first = QSUBJECT.objects.filter(id=terms[0][0])
        second = QSUBJECT.objects.filter(id=terms[1][0])
    else:
        first = QSUBJECT.objects.filter(id=terms[0][0])
    return render(request, 'result/term_summary.html',  {'anu' : anu, 'first' : first, 'second' : second})#, 'third' : third})
def three_term_records(request, pk):
    qry = get_object_or_404(BTUTOR, pk=pk)
    anu = ANNUAL.objects.filter(subject_by__exact=qry, subject_by__user__exact=request.user)
    page = request.GET.get('page', 1)

    paginator = Paginator(anu, 60)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/all_three_term.html', {'all_page': all_page, 'qry' : qry, 'pk': pk})

def user_example(request):
   f = open('/uqi/result/templates/result/ft_jss_1.txt', 'r')
   file_content = f.read()
   f.close()
   return HttpResponse(file_content, content_type='text/plain')
    
#################################################################################
def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    user.is_staff = True
    if request.method == "POST":
        profile = Edit_User.objects.get(user = user)
        form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            user.last_name = form.cleaned_data['last_name']
            user.first_name = form.cleaned_data['first_name']
            user.save()
            profile.last_name = form.cleaned_data['last_name']
            profile.first_name = form.cleaned_data['first_name']
            profile.bio = form.cleaned_data['bio']
            profile.phone = form.cleaned_data['phone']
            profile.city = form.cleaned_data['city']
            profile.country = form.cleaned_data['country']
            profile.organization = form.cleaned_data['organization']
            profile.location = form.cleaned_data['location']
            profile.birth_date = form.cleaned_data['birth_date']
            profile.department = form.cleaned_data['department']
            if 'photo' in request.FILES:
                profile.photo = request.FILES['photo']
            profile.email_confirmed = True
            profile.save()
            #form.save()
            return redirect('logins')                
    else:
        form = ProfileForm(instance=user.profile)
    return render(request, 'result/profile_update.html', {'form': form}) 

@login_required   
def student_name_edit(request, pk):#editing student_name /every tutor home detail views<a href="{% url 'edit_annual' pk=scr.id %}">
    qrn = get_object_or_404(QSUBJECT, pk=pk)
    if request.method == 'POST':
        result = student_names(request.POST)
        if result.is_valid():
            qry = get_object_or_404(CNAME, student_name=qrn.student_name)
            qry.student_name = result.cleaned_data['student_name']
            qry.save()
            return redirect('home')
    else:
        result = student_names()
    return render(request, 'result/edit_student_name.html', {'result': result, 'qrn':qrn})


class edit_annual(UpdateView):#New teacher form for every new term, class, subjects
    model = ANNUAL
    fields = ['student_name', 'first', 'second', 'third']
    success_url = reverse_lazy('home')

class Teacher_model_view(UpdateView):#New teacher form for every new term, class, subjects
    model = BTUTOR
    fields = ['user', 'teacher_name', 'subject', 'Class', 'term', 'males', 'females']
    success_url = reverse_lazy('home') 
    
class Subject_model_view(UpdateView):#New teacher form for every new term, class, subjects
    model = QSUBJECT
    fields = ['student_name', 'test', 'agn', 'atd', 'total', 'exam', 'agr', 'grade', 'posi', 'tutor']
    
#@login_required

def manage_subject_updates(request, pk):
    tutor = BTUTOR.objects.get(pk=pk)
    ext = tutor.males+tutor.females - QSUBJECT.objects.filter(tutor__exact=tutor).count()
    QsubjectFormSet = modelformset_factory(QSUBJECT, exclude=('Class', 'logged_in', 'total', 'agr', 'grade', 'posi', 'gender', 'created', 'updated', 'cader', 'model_in',), extra=ext)
    if request.method == "POST":
        formset = QsubjectFormSet(request.POST, queryset=QSUBJECT.objects.filter(tutor__exact=tutor),)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    form.save()
            return redirect('many_subject_updates', pk=pk)
    else:
        formset = QsubjectFormSet(queryset=QSUBJECT.objects.filter(tutor__exact=tutor))
    return render(request, 'result/qsubject_formset.html', {'formset': formset, 'pk':pk, 'tutor' : tutor})

###############################################################################
@login_required
def profiles(request, pk):#show single candidate profile
    qry = get_object_or_404(Edit_User, pk=pk)
    return render(request, 'result/profiles.html', {'qry' : qry})
#@login_required
class ProfileUpdate(UpdateView):
    model = Edit_User
    fields = ['first_name', 'last_name', 'bio', 'phone', 'city', 'department', 'location', 'birth_date', 'country', 'organization']
    success_url = reverse_lazy('home')
@login_required
def new_profiles_pic(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST' and request.FILES['myfile']:
        profile = Edit_User.objects.get(user = user)
        profile.photo = request.FILES['myfile']
        profile.save()
        return redirect('pro_detail', pk=pk)
    return render(request, 'result/picture.html')  

def flexbox(request):
    return render(request, 'result/flexbox.html')