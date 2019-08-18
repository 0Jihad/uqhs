from .models import QSUBJECT, CNAME, BTUTOR, ANNUAL, OVERALL_ANNUAL, Edit_User, SESSION
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from result.utils import do_grades, do_positions, grade_counter, cader
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Sum, Avg
 #return HttpResponse(student_name_id_third, content_type='text/plain')

@login_required
def explor_annual(request, pk):
    import time
    from datetime import timedelta
    start_time = time.time()
    tutor = get_object_or_404(BTUTOR, pk=pk)
    previous = BTUTOR.objects.filter(Class__exact = tutor.Class, subject__exact = tutor.subject, session__exact=tutor.session).exclude(term__exact='3rd Term')
    if previous.count() == 2:
        previous_id = [i[0] for i in list(previous.values_list('id'))]
        previous_id = sorted(previous_id)
        tutor1 = get_object_or_404(BTUTOR, pk=previous_id[0])
        tutor2 = get_object_or_404(BTUTOR, pk=previous_id[1])
        if Edit_User.objects.filter(class_in__exact=tutor.Class).count() == 1:
            tutor.teacher_in=Edit_User.objects.get(class_in=tutor.Class).user
            tutor.save()
            student_name_id_first = [i[0] for i in list(QSUBJECT.objects.filter(tutor__exact=tutor1).values_list('student_name_id'))]
            student_name_id_second = [i[0] for i in list(QSUBJECT.objects.filter(tutor__exact=tutor1).values_list('student_name_id'))]
            student_name_id_third = [i[0] for i in list(QSUBJECT.objects.filter(tutor__exact=tutor).values_list('student_name_id'))]
            if len(student_name_id_first) != 0 and len(student_name_id_second) != 0 and len(student_name_id_third) != 0:
                first_only = [i for i in student_name_id_third if i in student_name_id_first]
                second_only = [i for i in student_name_id_third if i in student_name_id_second]
                common_in_terms = [x for x in student_name_id_third if x in second_only and x in first_only]
                if len(common_in_terms) != 0:
                    for i in range(0, len(common_in_terms)):
                        student_name = CNAME.objects.get(pk=common_in_terms[i])
                        first = QSUBJECT.objects.get(student_name_id=common_in_terms[i], tutor__exact=tutor1)
                        second = QSUBJECT.objects.get(student_name_id=common_in_terms[i], tutor__exact=tutor2)
                        third = QSUBJECT.objects.get(student_name_id=common_in_terms[i], tutor__exact=tutor)
                        dim = [first.agr, second.agr, third.agr]
                        sd = [sum(dim), round((sum(dim[:])+0.1)/sum(x > 0 for x in dim[:]), 2)]
                        if ANNUAL.objects.filter(subject_by = tutor, student_name_id__exact=common_in_terms[i]).count() == 0:
                            annual = ANNUAL(subject_by = tutor, student_name=student_name, subject=tutor.subject, first = first, second = second, third = third, anual = sd[0], Agr = sd[1])
                            annual.save()
                        else:
                            annual = ANNUAL.objects.get(subject_by = tutor, student_name_id=common_in_terms[i], subject=tutor.subject)
                            annual.first = first
                            annual.second = second
                            annual.third = third
                            annual.anual = sd[0]
                            annual.Agr = sd[1]
                            annual.save()
                        if OVERALL_ANNUAL.objects.filter(student_name_id__exact=common_in_terms[i], class_in__exact=tutor.Class, teacher_in__exact=Edit_User.objects.get(class_in=tutor.Class).user, session__exact=tutor.session).count() == 0:
                            subj = OVERALL_ANNUAL.objects.create(student_name=student_name, class_in=tutor.Class, teacher_in=Edit_User.objects.get(class_in=tutor.Class).user,  session=tutor.session, eng = None, mat = None, agr = None, bus = None, bst = None, yor = None, nva = None, irs = None, prv = None, ict = None, acc = None, his = None)
                        else:
                            subj = get_object_or_404(OVERALL_ANNUAL, student_name_id=common_in_terms[i], class_in=tutor.Class, teacher_in=Edit_User.objects.get(class_in=tutor.Class).user,  session=tutor.session)
                        subj.save()
                        if request.user.profile.class_in != None:
                            class_records(tutor, subj, annual)
                        third.annual_scores = {str(tutor.subject.name)[:3]+':'+str(first.agr)+':'+str(first.grade)+':'+str(first.posi)+':---:'+str(second.agr)+':'+str(second.grade)+':'+str(second.posi)+':---:'+str(third.agr)+':'+str(third.grade)+':'+str(third.posi)}
                        third.save()
                third_term_only = list(set(student_name_id_third) - set(common_in_terms))
                if len(third_term_only) != 0:
                    for i in range(0, len(third_term_only)):
                        student_name = CNAME.objects.get(pk=third_term_only[i])
                        third = QSUBJECT.objects.get(student_name_id=third_term_only[i], tutor__exact=tutor)
                        if ANNUAL.objects.filter(subject_by = tutor, student_name_id__exact=third_term_only[i]).count() == 0:
                            annual = ANNUAL(subject_by = tutor, student_name=student_name, subject=tutor.subject, third = third, anual = third.agr, Agr = third.agr)
                            annual.save()
                        else:
                            annual = ANNUAL.objects.get(subject_by = tutor, student_name_id=third_term_only[i], subject=tutor.subject)
                            annual.third = third
                            annual.anual = third.agr
                            annual.Agr = third.agr
                            annual.save()
                        if OVERALL_ANNUAL.objects.filter(student_name_id__exact=third_term_only[i], class_in__exact=tutor.Class, teacher_in__exact=Edit_User.objects.get(class_in=tutor.Class).user, session__exact=tutor.session).count() == 0:
                            subj = OVERALL_ANNUAL.objects.create(student_name=student_name, class_in=tutor.Class, teacher_in=Edit_User.objects.get(class_in=tutor.Class).user,  session=tutor.session, eng = None, mat = None, agr = None, bus = None, bst = None, yor = None, nva = None, irs = None, prv = None, ict = None, acc = None, his = None)
                        else:
                            subj = get_object_or_404(OVERALL_ANNUAL, student_name_id=third_term_only[i], class_in=tutor.Class, teacher_in=Edit_User.objects.get(class_in=tutor.Class).user,  session=tutor.session)
                        if request.user.profile.class_in != None:
                            class_records(tutor, subj, annual)
                        third.annual_scores = {str(tutor.subject.name)[:3]+':'+str(third.agr)+':'+str(third.grade)+':'+str(third.posi)}
                        third.save()
                name_ids = [list(r[:]) for r in list(ANNUAL.objects.filter(subject_by__exact=tutor).values_list('id', 'Agr')) if r[1] != None]
                scores = [round(x[1], 0) for x in name_ids]
                #return HttpResponse(ANNUAL.objects.filter(subject_by__exact=tutor), content_type='text/plain')
                posi = do_positions(scores[:])
                grd = do_grades(scores[:], cader(tutor.Class)) 
                for r in range(0, len(name_ids)):#
                    get_student = get_object_or_404(ANNUAL, pk=name_ids[r][0])
                    get_student.Grade = grd[r]
                    get_student.Posi = posi[r]
                    get_student.save()
                all_t = ANNUAL.objects.filter(subject_by__Class=tutor.Class, subject__exact=tutor.subject, subject_by__session__exact=tutor.session).order_by('id')
                tutor.model_in =  'annual'
                tutor.save()
                elapsed_time_secs = time.time() - start_time
                msg = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
                print(msg) 
                page = request.GET.get('page', 1)
                paginator = Paginator(all_t, 30)
                try:
                    all_page = paginator.page(page)
                except PageNotAnInteger:
                    all_page = paginator.page(1)
                except EmptyPage:
                    all_page = paginator.page(paginator.num_pages)
                return render(request, 'result/first_second_third.html',  {'all_page': all_page, 'in_class': all_t.count(), 'pk':pk, 'tutor':tutor, 'msg':msg})
            else:
                return redirect('home')
        else:
            return HttpResponse("Class teacher for this class is yet to be allocated, contact admin.", status=400)
    else:
        return redirect('home')
        
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
    subj.save()

def pre_broad_sheet(request):
    al = OVERALL_ANNUAL.objects.filter(teacher_in__exact=request.user, class_in__exact=request.user.profile.class_in, session__exact=SESSION.objects.get(pk=1).new)
    return render(request, 'result/pre_broadsheet.html',  {'date': datetime.now(), 'in_class': al, 'last_name':request.user.profile.last_name, 'first_name':request.user.profile.first_name, 'class_in':request.user.profile.class_in })
   
def broad_sheet(request):
    al = OVERALL_ANNUAL.objects.filter(teacher_in__exact=request.user, class_in__exact=request.user.profile.class_in, session__exact = SESSION.objects.get(pk=1).new)
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
                    ds += [ANNUAL.objects.get(pk=lst[i][r]).Agr]
                    if i == 0:
                        teacher_id = BTUTOR.objects.get(pk=ANNUAL.objects.get(pk=lst[i][r]).third.tutor.id)
                        teacher_id.class_teacher_id = request.user.id
                        teacher_id.save()
            gets = OVERALL_ANNUAL.objects.get(pk=lst[i][0])
            gets.Agr = round(sum(ds), 2)
            gets.Avr = round(sum(ds)/len(ds), 2)
            gets.save()
            
        name_ids = [list(i[:]) for i in list(al.values_list('id', 'Avr'))]
        scores = [round(x[1], 0) for x in name_ids]
        posi = do_positions(scores[:])
        grd = do_grades(scores[:], cader(gets.class_in)) 
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
