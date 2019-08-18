from .models import QSUBJECT, ASUBJECTS, BTUTOR, SESSION
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import subjectforms, subject_class_term_Form
from django.contrib.auth.decorators import login_required
from result.utils import cader

def create_subjects(request):#New teacher form for every new term, class, subjects
    if request.method == 'POST':
        result = subjectforms(request.POST)
        if result.is_valid():
            check = ASUBJECTS.objects.filter(name__exact=result.cleaned_data['name'])
            if len(check) == 0: 
                new_subject = ASUBJECTS(name=result.cleaned_data['name'])
                new_subject.save()
                return redirect('teacher_create')
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
        SUB_NAME = ASUBJECTS.objects.get(pk=pk)
        subject = QSUBJECT.objects.filter(tutor__subject__exact=ASUBJECTS.objects.get(pk=pk)).order_by('id')
        count_grade = QSUBJECT.objects.filter(tutor__subject__exact=ASUBJECTS.objects.get(pk=pk)).count()
    page = request.GET.get('page', 1)
    paginator = Paginator(subject, 30)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/subject_in_all.html',  {'count_grade' : count_grade, 'all_page': all_page, 'pk' : pk, 'SUB_NAME':SUB_NAME})
@login_required
def create_new_subject_teacher(request):# teacher form for every new term, class, subjects, subject_per_name
    if request.method == 'POST':
        result = subject_class_term_Form(request.POST)
        if result.is_valid():
            unique = BTUTOR.objects.filter(accounts__exact=request.user, term__exact=result.cleaned_data['term'], Class__exact=result.cleaned_data['Class'], subject__exact = result.cleaned_data['subject'], teacher_name__exact = f'{request.user.profile.title}{request.user.profile.last_name} : {request.user.profile.first_name}', session__exact = SESSION.objects.get(pk=1).new).count()
            first = BTUTOR.objects.filter(accounts__exact=request.user, term__exact='1st Term', Class__exact=result.cleaned_data['Class'], subject__exact = result.cleaned_data['subject'], teacher_name__exact = f'{request.user.profile.title}{request.user.profile.last_name} : {request.user.profile.first_name}', session__exact = SESSION.objects.get(pk=1).new).count()
            if first != 0 and unique == 0 or result.cleaned_data['term'] == '1st Term' and unique == 0:
                new_teacher = BTUTOR(accounts=request.user, subject = result.cleaned_data['subject'], Class = result.cleaned_data['Class'], term = result.cleaned_data['term'], cader=cader(result.cleaned_data['Class']), teacher_name = f'{request.user.profile.title}{request.user.profile.last_name} : {request.user.profile.first_name}', session = SESSION.objects.get(pk=1).new)
                new_teacher.save()
                return redirect('upload_txt', pk=new_teacher.id)
            else:
                others = BTUTOR.objects.filter(accounts__exact=request.user, subject__exact = result.cleaned_data['subject']).order_by('id')
                page = request.GET.get('page', 1)
                paginator = Paginator(others, 30)
                try:
                    all_page = paginator.page(page)
                except PageNotAnInteger:
                    all_page = paginator.page(1)
                except EmptyPage:
                    all_page = paginator.page(paginator.num_pages)
                return render(request, 'result/first_term_record_notify.html', {'all_page':all_page, 'tutor':result.cleaned_data['subject']})
    else:
        result = subject_class_term_Form()
        return render(request, 'result/create_new_teacher.html', {'result': result})
