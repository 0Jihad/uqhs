from .models import QSUBJECT, Edit_User, ANNUAL, BTUTOR, CNAME, RESULT_GRADE, OVERALL_ANNUAL, SESSION, ASUBJECTS
from result.utils import grade_counter
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import subject_class_term_Form, name_class_Form
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Avg
import datetime
def home(request):#Step 1:: list of tutor's subjects with class, term
    """
    Home page for every tutor!
    """
    # If a tutor is authenticated then redirect them to the tutor's page
    if request.user.is_authenticated:#a tutor page
        tutor = BTUTOR.objects.filter(accounts=request.user).order_by('Class')
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


def uniqueness(request, pk):
    tutor = BTUTOR.objects.get(pk=pk)
    unique = BTUTOR.objects.filter(accounts__exact=tutor.accounts, term__exact=tutor.term, Class__exact=tutor.Class, subject__exact = tutor.subject, teacher_name__exact = f'{request.user.profile.title}{request.user.profile.last_name} : {request.user.profile.first_name}', session__exact = tutor.session)
    first = BTUTOR.objects.filter(accounts__exact=tutor.accounts, term__exact='1st Term', Class__exact=tutor.Class, subject__exact = tutor.subject, teacher_name__exact = f'{request.user.profile.title}{request.user.profile.last_name} : {request.user.profile.first_name}', session__exact = tutor.session)
    if unique.count() > 1:
        return render(request, 'result/tutor_unique.html', {'tutor':unique, 'ids':tutor})
    elif first.count()== 0:
        others = BTUTOR.objects.filter(accounts__exact=request.user, subject__exact = tutor.subject).order_by('id')
        page = request.GET.get('page', 1)
        paginator = Paginator(others, 30)
        try:
            all_page = paginator.page(page)
        except PageNotAnInteger:
            all_page = paginator.page(1)
        except EmptyPage:
            all_page = paginator.page(paginator.num_pages)
        return render(request, 'result/first_term_record_notify.html', {'all_page':all_page, 'tutor':tutor.subject})
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
                return redirect('teacher_create') 
    else:
        result = name_class_Form()
    return render(request, 'result/name_class_filter.html', {'result': result})  


def sSum(subjects):
    anuual = subjects.aggregate(Sum('agr'))['agr__sum']
    return anuual

def sum_avg(mains):
    if mains.count() !=0:
        subject_scores = round(mains.aggregate(Sum('agr'))['agr__sum'], 1)
        subject_pert = round(mains.aggregate(Avg('agr'))['agr__avg'],2)
    else:
        subject_pert = None
        subject_scores = None
    return [subject_scores, subject_pert]

def detailView(request, pk):##Step 2::  every tutor home detail views 
    tutor = get_object_or_404(BTUTOR, pk=pk)
    mains = QSUBJECT.objects.filter(tutor__exact=tutor).order_by('id')#request.user 
    if request.user.is_authenticated:
        pro = get_object_or_404(Edit_User, user=request.user)
        pro.account_id = pk
        pro.save()
    if mains.count() != 0:
        count_grade = QSUBJECT.objects.filter(tutor__exact=tutor).count()
        grad = grade_counter(mains, tutor.id, tutor.subject.name)
        page = request.GET.get('page', 1)
        paginator = Paginator(mains, 30)
        if tutor.term == '3rd Term' and tutor.model_in != 'annual':
            return redirect('compute_annual', pk=tutor.id)
        try:
            all_page = paginator.page(page)
        except PageNotAnInteger:
            all_page = paginator.page(1)
        except EmptyPage:
            all_page = paginator.page(paginator.num_pages)
    else:
        return redirect('upload_txt', pk=tutor.id)
    return render(request, 'result/qsubject.html',  {'grad' : grad, 'count_grade' : count_grade, 'all_page': all_page, 'subject_scores':sum_avg(mains)[0], 'subject_pert':sum_avg(mains)[1], 'qry' : tutor, 'pk': pk})

def detail_all(request, pk):##Step 2::  every tutor home detail views
    tutor = get_object_or_404(BTUTOR, pk=pk)
    mains = QSUBJECT.objects.filter(tutor__exact=tutor).order_by('id')#request.user
    count_grade = QSUBJECT.objects.filter(tutor__exact=tutor).count()
    grad = grade_counter(mains, tutor.id, tutor.subject.name)
    return render(request, 'result/all_qsubject.html',  {'subject_scores':sum_avg(mains)[0], 'subject_pert':sum_avg(mains)[1], 'grad' : grad, 'count_grade' : count_grade, 'mains': mains, 'qry' : tutor, 'pk': pk})


def annual_view(request, pk):##Step 2::  every tutor home detail views 
    tutor = get_object_or_404(BTUTOR, pk=pk)
    mains = ANNUAL.objects.filter(subject_by__exact=tutor).order_by('id')#request.user
    page = request.GET.get('page', 1)
    paginator = Paginator(mains, 30)
    grad = get_object_or_404(RESULT_GRADE, identifier = tutor.id, subject = tutor.subject.name)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/all_annual.html',  {'subject_scores':sum_avg(mains)[0], 'subject_pert':sum_avg(mains)[1], 'count_grade' : mains.count(), 'all_page': all_page, 'qry' : tutor, 'pk': pk, 'grad': grad})

def all_annual_view(request, pk):##Step 2::  every tutor home detail views
    tutor = get_object_or_404(BTUTOR, pk=pk)
    mains = ANNUAL.objects.filter(subject_by__exact=tutor).order_by('id')#request.user
    grad = get_object_or_404(RESULT_GRADE, identifier = tutor.id, subject = tutor.subject.name)
    return render(request, 'result/all_annual_all.html',  {'subject_scores':sum_avg(mains)[0], 'subject_pert':sum_avg(mains)[1], 'count_grade' : mains.count(), 'mains': mains, 'qry' : tutor, 'pk': pk, 'grad': grad})


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

def qsubject_on_grade(request, pk_code):##Step 2::  every tutor home detail views
    pk=pk_code[:len(pk_code)-2]
    tutor = get_object_or_404(BTUTOR, pk=pk_code[:len(pk_code)-2])
    grad = get_object_or_404(RESULT_GRADE, identifier = tutor.id, subject = tutor.subject.name)
    if tutor.Class == 'JSS 1' or tutor.Class == 'JSS 2' or tutor.Class == 'JSS 3':
        mains = QSUBJECT.objects.filter(tutor__exact=tutor, grade=pk_code[-2])
    else:
        mains = QSUBJECT.objects.filter(tutor__exact=tutor, grade=pk_code[len(pk_code)-2:])
    return render(request, 'result/qsubject.html',  {'subject_scores':sum_avg(mains)[0], 'subject_pert':sum_avg(mains)[1], 'grad' : grad, 'count_grade' : mains.count(), 'all_page': mains, 'qry' : tutor, 'pk': pk})
    
def annual_on_grade(request, pk_code):##Step 2::  every tutor home detail views
    pk=pk_code[:len(pk_code)-2]
    tutor = get_object_or_404(BTUTOR, pk=pk_code[:len(pk_code)-2])
    grad = get_object_or_404(RESULT_GRADE, identifier = tutor.id, subject = tutor.subject.name)
    if tutor.Class == 'JSS 1' or tutor.Class == 'JSS 2' or tutor.Class == 'JSS 3':
        mains = ANNUAL.objects.filter(subject_by__Class=tutor.Class, subject_by__session=tutor.session, subject__exact=tutor.subject, grade=pk_code[-2], session__exact=SESSION.objects.get(pk=1).new )
    else:
        mains = ANNUAL.objects.filter(subject_by__Class=tutor.Class, subject_by__session=tutor.session, subject__exact=tutor.subject, grade=pk_code[len(pk_code)-2:], session__exact=SESSION.objects.get(pk=1).new)
    return render(request, 'result/annual_on_grade.html', {'subject_scores':sum_avg(mains)[0], 'subject_pert':sum_avg(mains)[1], 'grad': grad, 'count_grade' : mains.count(), 'qry': tutor, 'all_page': mains, 'pk':pk})

def broadsheet_on_grade(request, pk_code):##Step 2::  every tutor home detail views
    if request.user.profile.class_in == 'JSS 1' or request.user.profile.class_in == 'JSS 2' or request.user.profile.class_in == 'JSS 3':
        al = OVERALL_ANNUAL.objects.filter(teacher_in__exact=request.user, class_in__exact=request.user.profile.class_in, grade=pk_code[-2])
    else:
        al = OVERALL_ANNUAL.objects.filter(teacher_in__exact=request.user, class_in__exact=request.user.profile.class_in, grade=pk_code[len(pk_code)-2:])
    total_scores = round(al.aggregate(Sum('Avr'))['Avr__sum'], 1)
    avg_pert = round(al.aggregate(Avg('Avr'))['Avr__avg'],2)
    grad = grade_counter(al, request.user.id, 'BroadSheet')
    return render(request, 'result/yearly_apage.html',  {'grad':grad, 'total_scores':total_scores, 'avg_pert':avg_pert, 'all_page': al, 'in_class': al.count(), 'last_name':request.user.profile.last_name, 'first_name':request.user.profile.first_name, 'class_in':request.user.profile.class_in })

def Student_names_list(request):##Step 2::  every tutor home detail views
    mains = CNAME.objects.all()
    counts = mains.count()
    page = request.GET.get('page', 1)

    paginator = Paginator(mains, 200)
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
        paginator = Paginator(mains, 30)
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
        paginator = Paginator(tutors, 30)
        try:
            all_page = paginator.page(page)
        except PageNotAnInteger:
            all_page = paginator.page(1)
        except EmptyPage:
            all_page = paginator.page(paginator.num_pages)
        return render(request, 'result/student_on_all_subjects_detail.html',  {'all_page': all_page, 'count_t': count_t, 'count_s':count_s})
###    
def student_subject_list(request, pk):##Step 2::  every tutor home detail views
    name = CNAME.objects.get(pk=pk)
    mains = QSUBJECT.objects.filter(student_name_id=name.id)
    if len(list(mains.values_list('id'))) != 0:
        ids = list(mains.values_list('id'))[0][0]
    else:
        ids = 0
    counts = mains
    page = request.GET.get('page', 1)

    paginator = Paginator(mains, 20)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/student_subject_list.html',  {'all_page': all_page, 'counts': counts, 'name': name, 'pk': ids, 'cnt': pk})


def all_student_subject_list(request, pk):##Step 2::  every tutor home detail views
    name = CNAME.objects.get(pk=pk)
    mains = QSUBJECT.objects.filter(student_name_id=name.id)
    ids = list(mains.values_list('id'))
    counts = mains
    return render(request, 'result/all_student_subject_list.html',  {'mains': mains, 'counts': counts, 'name': name, 'pk': ids[0][0], 'cnt': pk})

##########################PORTAL MANAGEMENT####################################


def teacher_accounts(request):
    tutors = BTUTOR.objects.all().order_by('Class')
    page = request.GET.get('page', 1)

    paginator = Paginator(tutors, 20)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/all_tutor.html', {'all_page': all_page})

def all_teachers(request):
    tutors = BTUTOR.objects.all().order_by('Class')
    return render(request, 'result/all_teachers.html', {'tutors': tutors})

def results_junior_senior(request, pk):
    cls = ['JSS 1', 'JSS 2', 'JSS 3', 'SS 1', 'SS 2', 'SS 3']
    tutors = BTUTOR.objects.filter(Class__exact=cls[int(pk)]).order_by('Class')
    return render(request, 'result/results_junior_senior.html', {'tutor': tutors, 'cls':cls[int(pk)]})

def all_users(request):#show single candidate profile
    qry = User.objects.all()
    return render(request, 'result/all_users.html', {'qry' : qry})

def student_subject_detail_one_subject(request, pk):#student subject detail(single term)
    many = get_object_or_404(QSUBJECT, pk=pk)
    subjects = QSUBJECT.objects.filter(student_name = many.student_name, tutor__subject__exact=many.tutor.subject)
    anuual = sSum(subjects)
    return render(request, 'result/single_subject_per_student.html',  {'subjects' : subjects, 'name':many, 'anuual':anuual, 'pk':pk}) 

def student_subject_detail_all_subject(request, pk):#student subject detail(single term)
    many = get_object_or_404(QSUBJECT, pk=pk)
    subjects = QSUBJECT.objects.filter(student_name = many.student_name, tutor__Class__exact=many.tutor.Class)
    anuual = sSum(subjects)
    return render(request, 'result/single_subject_per_student.html',  {'subjects' : subjects, 'name':many, 'anuual':anuual, 'pk':pk}) 

def searchs(request):
    query = request.GET.get("q")
    names = CNAME.objects.filter(student_name__icontains = query.upper())
    page = request.GET.get('page', 1)
    paginator = Paginator(names, 30)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/searched_names.html',  {'all_page' : all_page, 'names': names.count()}) 	

def all_search_lists(request, pk):
	query = QSUBJECT.objects.get(pk=pk)
	results = QSUBJECT.objects.filter(student_name__exact = query.student_name, Class__exact = query.tutor.Class)
	return render(request, 'result/all_searced_list.html',  {'results' : results}) 	
   
def broad_sheet_on_page(request):
    al = OVERALL_ANNUAL.objects.filter(teacher_in__exact=request.user, class_in__exact=request.user.profile.class_in, session__exact=SESSION.objects.get(pk=1).new)
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
    al = OVERALL_ANNUAL.objects.filter(teacher_in__exact=user, class_in__exact=user.profile.class_in, session__exact=SESSION.objects.get(pk=1).new)
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

def show_annual(request, pk):
    import time
    from datetime import timedelta
    start_time = time.time()    
    tutor = get_object_or_404(BTUTOR, pk=pk)
    all_t = ANNUAL.objects.filter(subject_by__exact=tutor).order_by('id')
    tutor.model_in =  'annual'
    tutor.save()
    elapsed_time_secs = time.time() - start_time
    msg = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
    print(msg)    
    return render(request, 'result/all_first_second_third.html',  {'all_page': all_t, 'in_class': all_t.count(), 'pk':pk, 'tutor':tutor, 'msg':msg})
	
