# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:54:06 2019

@author: AdeolaOlalekan
"""
import os
from django.views.generic import View
from django.shortcuts import get_object_or_404
import csv
from .utils import Render
from django.http import HttpResponse
from django.db.models import Sum, Avg
from datetime import datetime
from wsgiref.util import FileWrapper
from .models import QSUBJECT, ANNUAL, BTUTOR, CNAME, OVERALL_ANNUAL, TERM, SESSION

module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'test1.txt')
def sample_disply(request):
    #os.chdir(file_path)
    empty_list = open(file_path, "r" )
    return HttpResponse(empty_list, content_type='text/plain')

def sample_down(request):
    #os.chdir(file_path)
    wrapper = FileWrapper(open(file_path, "r" ))
    response=HttpResponse(wrapper, content_type="text/plain")
    response['Content-Disposition'] ='attachment; filename="samples.txt"'
    return response 

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

def extract_broad_sheet(request):
    sd = []
    dim = ['student_name']
    mid = ['eng', 'mat', 'agr', 'bus', 'bst', 'yor', 'nva', 'irs', 'prv', 'ict', 'acc', 'his', 'Agr', 'Avr', 'grade', 'posi']
    al = OVERALL_ANNUAL.objects.filter(teacher_in__exact=request.user, class_in__exact=request.user.profile.class_in, session__exact= SESSION.objects.get(pk=1).new)
    if al.count() != 0:
        sd = []
        x = list(al.values_list('student_name', 'eng', 'mat', 'agr', 'bus', 'bst', 'yor', 'nva', 'irs', 'prv', 'ict', 'acc', 'his', 'Agr', 'Avr', 'grade', 'posi'))
        lst = [list(i[:13]) for i in x]
        lss = [list(i[13:]) for i in x]
        for i in range(0, len(lst)):
            ds = [CNAME.objects.get(pk=x[i][0]).student_name]
            try:
                while True:
                    lst[i][lst[i].index(None)] = 0
            except ValueError:
                pass         
            for r in range(1, len(lst[i])):
                if lst[i][r] != 0:
                    ds += [TERM.objects.get(pk=lst[i][r]).avr]
                    dim += [mid[r-1]]
            sd += [ds+lss[i]]
    return [sd, dim[:3]+['Agr', 'Avr', 'grade', 'posi']]

def export_broadsheet(request):#result download based on login tutor teacher_accounts Subject_model_view
    sd = extract_broad_sheet(request)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="broadsheet.csv"'
    writer = csv.writer(response)
    writer.writerow(sd[1])
    for each in sd[0]:
        writer.writerow(each)
    return response 


def export_third_scores(request, pk):#result download based on login tutor 
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="annua_score.csv"'
    writer = csv.writer(response)
    writer.writerow(['student_name', 'test', 'agn', 'atd', 'total', 'exam', 'third', 'second', 'first', 'anual', 'agr', 'grade', 'anu_posi'])
    tutor = get_object_or_404(BTUTOR, pk=pk)
    subjects = QSUBJECT.objects.filter(tutor__exact=tutor).values_list('student_name', 'test', 'agn', 'atd', 'total', 'exam')
    scores = [list(x) for x in subjects]
    subject = ANNUAL.objects.filter(subject__exact=tutor.subject, subject_by__Class__exact=tutor.Class, term__exact='3rd Term', session__exact= SESSION.objects.get(pk=1).new )
    sets = [x[:] for x in list(subject.values_list('third', 'second', 'first', 'anual', 'agr', 'grade', 'anu_posi')) if x[3] != None]
    annual = [list(x) for x in sets]
    sd = []
    for i in range(0, len(annual)):
        sd += [scores[i]+annual[i]]
    for i in range(0, len(sd)):
    	sd[i][0] = CNAME.objects.get(pk=sd[i][0]).student_name
    for each in sd:
        writer.writerow(each)
    return response   
 
class terms_in_pdf(View):
    def get(self, request):
        tutor = get_object_or_404(BTUTOR, pk=request.user.profile.account_id)
        if tutor.term == '3rd Term':
            mains = ANNUAL.objects.filter(subject_by__Class__exact=tutor.Class, subject__exact=tutor.subject, session__exact= SESSION.objects.get(pk=1).new ).order_by('id')
        else:
            mains = QSUBJECT.objects.filter(tutor__exact=tutor).order_by('id')
        today = datetime.now()
        params = {
            'count_grade': mains.count(),
            'tutor': tutor,
            'request': request,
            'mains': mains,
            'today': today,
            'subject_scores': round(mains.aggregate(Sum('agr'))['agr__sum'],2),
            'subject_pert': round(mains.aggregate(Avg('agr'))['agr__avg'],2)
        }
        if tutor.term == '3rd Term':
            return Render.render('result/anu_pdf.html', params)
        else:
            return Render.render('result/pdf.html', params)
        
class broadsheet_in_pdf(View):
    def get(self, request):
        tutor = get_object_or_404(BTUTOR, pk=request.user.profile.account_id)
        mains = OVERALL_ANNUAL.objects.filter(teacher_in__exact=request.user, class_in__exact=request.user.profile.class_in, session__exact=SESSION.objects.get(pk=1).new)
        today = datetime.now()
        params = {
            'in_class': mains.count(),
            'tutor': tutor,
            'mains': mains,
            'today': today,
            'subject_scores': round(mains.aggregate(Sum('Avr'))['Avr__sum'], 2),
            'subject_pert': round(mains.aggregate(Avg('Avr'))['Avr__avg'],2)
            }
        if  tutor.Class == 'SS 1' or tutor.Class == 'SS 2' or tutor.Class == 'SS 3':
            return Render.render('result/broad_sheet_pdf_s.html', params)
        else:
            return Render.render('result/broad_sheet_pdf_j.html', params)
