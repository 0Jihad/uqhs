# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:06:57 2019

@author: AdeolaOlalekan
"""

import os
sd = [['Saheed', 80], ['Sadeeq', 81], ['Oladejo', 82], ['Afeez', 83], ['Adeyeri', 84], ['Olanrewaju', 85], ['Azeez', 86], ['Abbas', 87], ['Ejalonibu', 88], ['Oladele', 89], ['Oladoje', 90], ['Adisa', 91], ['Ridwanullah', 92], ['Zainu', 93], ['Olawale', 94], ['Tawakaltu', 95], ['Oseolohun', 96], ['Adedokun', 97], ['Adepoju', 98], ['Ogundepo', 99], ['Habeeb', 100], ['Oladimeji', 101], ['Olapade', 102], ['Adetona', 103], ['Adeleke', 104], ['Lawal', 105], ['Mikail', 106]]
def text_rename():
    #JS = [['AGR', 97, 97, 94], ['ARB', 92, 96, 96], ['BST', 87, 88, 87], ['BUS', 85, 86, 85], ['ENG', 80, 81, 82], ['HIS', 98, 98, 81], ['IRS', 92, 92, 93], ['MATH', 83, 84, 84], ['NAV', 90, 91, 91], ['PRV', 94, 95, 95], ['YOR', 89, 89, 89], ['ACC', 91, 102, 102], ['AGR', 95, 95, 95], ['ARB', 93, 93, 93], ['BIO', 106, 106, 106], ['CHE', 101, 101], ['CIV', 90, 104, 104], ['COM', 85, 86, 86], ['CTR', 97, 105, 105], ['ECO', 102, 102, 102], ['ELE', 87, 100, 100], ['ENG', 80, 82, 82], ['GEO', 83, 83, 83], ['GOV', 90, 82, 104], ['GRM', 98, 98, 98], ['ICT', 88, 88, 88], ['IRS', 93, 96, 96], ['LIT', 80, 81, 82], ['MATH', 99, 84, 99], ['PHY', 99, 100, 100], ['YOR', 103, 103, 103]]
    CL = [['JSS 1', 97, 92, 87, 85, 80, 98, 92, 83, 90, 94, 89], ['JSS 2', 97, 96, 88, 86, 81, 98, 92, 84, 91, 95, 89], ['JSS 3', 94, 96, 87, 85, 82, 81, 93, 84, 91, 95, 89], ['SSS 1', 91, 95, 93, 106, 101, 90, 85, 97, 102, 87, 80, 83, 90, 98, 88, 93, 80, 99, 99, 103], ['SSS 2', 102, 95, 93, 106, 101, 104, 86, 105, 102, 100, 82, 83, 82, 98, 88, 96, 81, 84, 100, 103], ['SSS 3', 102, 95, 93, 106, 101, 104, 86, 105, 102, 100, 82, 83, 104, 98, 88, 96, 82, 99, 100, 103]]
    
    dcs = []
    basepath = 'C:/office/jango_env/uqi/result/all_scores/'
    for entry in os.listdir(basepath):
        sd = []#6
        tr = []
        for files in os.listdir(os.path.join(basepath, entry)):
            os.chdir(os.path.join(basepath, entry))
            print(files)
            sp = files.split('_')
            X = [i for i in CL if i[0] == sp[0]][0]
            if sp[0] == X[0]: #class
                #import os
                old_file = os.path.join(os.path.join(basepath, entry), files)
                new_file = os.path.join(os.path.join(basepath, entry), str(X[len(tr)+1]) + '_' + sp[0] + '_' + sp[1][-1] + '_' + sp[1][:3] + '.txt')
                os.rename(old_file, new_file)
                if sp[1][-1] == '3':
                    tr += [0]
                if sp[1][:3] == 'YOR' and sp[1][3:] == '3':
                    tr = []
                    sd += [files]
                            
                else:
                    print(sp)
    return dcs

#path = os.path.join('C:/office/jango_env/uqi/result/all_scores', 'JSS 1')#


for i in range(0, len(ids)):
     x = QSUBJECT.objects.get(pk=ids[i])
     if REGISTERED_ID.objects.filter(student_name__exact=x.student_name, student_class__exact=x.tutor.Class) !=0:
         get = REGISTERED_ID.objects.get(student_name=x.student_name, student_class=x.tutor.Class)
         x.student_id=get.student_id
         x.save()
     else:
         del(ids[i])


@login_required
def explor_annual(request, pk):
    start_time = time.time()
    tutor = get_object_or_404(BTUTOR, pk=pk)
    return HttpResponse(ANNUAL.objects.filter(subject_by__exact=tutor).delete(), content_type='text/plain')
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
            student_name_id_second = [i[0] for i in list(QSUBJECT.objects.filter(tutor__exact=tutor2).values_list('student_name_id'))]
            student_name_id_third = [i[0] for i in list(QSUBJECT.objects.filter(tutor__exact=tutor).values_list('student_name_id'))]
            #return HttpResponse([student_name_id_first, student_name_id_second, student_name_id_third], content_type='text/plain')
            if len(student_name_id_first) != 0 and len(student_name_id_second) != 0 and len(student_name_id_third) != 0:
                first_only = [i for i in student_name_id_third if i in student_name_id_first]
                second_only = [i for i in student_name_id_third if i in student_name_id_second]
                common_in_terms = [x for x in student_name_id_third if x in second_only and x in first_only]
                if tutor.model_in ==  'annual':
                    ANNUAL.objects.filter(subject_by__exact=tutor).delete()
                if len(common_in_terms) != 0:
                    for i in range(0, len(common_in_terms)):
                        first = QSUBJECT.objects.get(student_name_id=common_in_terms[i], tutor__exact=tutor1)
                        second = QSUBJECT.objects.get(student_name_id=common_in_terms[i], tutor__exact=tutor2)
                        third = QSUBJECT.objects.get(student_name_id=common_in_terms[i], tutor__exact=tutor)
                        dim = [first.agr, second.agr, third.agr]
                        sd = [sum(dim), round((sum(dim[:])+0.1)/sum(x > 0 for x in dim[:]), 2)]
                        annual_records(tutor, first, second, third, common_in_terms[i], sd)
                third_term_only = list(set(student_name_id_third) - set(common_in_terms))
                if len(third_term_only) != 0:
                    for i in range(0, len(third_term_only)):
                        third = QSUBJECT.objects.get(student_name_id=third_term_only[i], tutor__exact=tutor)
                        annual_records(tutor, None, None, third, third_term_only[i], [third.agr, third.agr])
                if request.user.profile.class_in != None:
                    class_records(tutor, student_name_id_third)
                name_ids = [list(r[:]) for r in list(ANNUAL.objects.filter(subject_by__exact=tutor).values_list('id', 'Agr')) if r[1] != None]
                scores = [round(x[1], 0) for x in name_ids]
                posi = do_positions(scores[:])
                grd = do_grades(scores[:], cader(tutor.Class)) 
                for r in range(0, len(name_ids)):#
                    get_student = get_object_or_404(ANNUAL, pk=name_ids[r][0])
                    get_student.Grade = grd[r]
                    get_student.Posi = posi[r]
                    get_student.save()
                all_t = ANNUAL.objects.filter(subject_by__exact=tutor).order_by('id')
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

def annual_records(tutor, first, second, third, pk, sd):
    student_name = CNAME.objects.get(pk=pk)
    if ANNUAL.objects.filter(subject_by__exact = tutor, student_name__exact=student_name).count() == 0:
        annual = ANNUAL(subject_by = tutor, student_name=student_name, first = first, second = second, third = third, anual = sd[0], Agr = sd[1])
        annual.save()
    else:
        annual = ANNUAL.objects.get(subject_by = tutor, student_name=student_name)
        annual.first = first
        annual.second = second
        annual.third = third
        annual.anual = sd[0]
        annual.Agr = sd[1]
        annual.save()
    #if OVERALL_ANNUAL.objects.filter(student_name__exact=student_name, class_in__exact=tutor.Class, teacher_in__exact=Edit_User.objects.get(class_in=tutor.Class).user, session__exact=tutor.session).count() == 0:
        #
    #else:
        #subj = get_object_or_404(OVERALL_ANNUAL, student_name=student_name, class_in=tutor.Class, teacher_in=Edit_User.objects.get(class_in=tutor.Class).user,  session=tutor.session)
    #subj.save()
    third.annual_scores = {str(tutor.subject.name)[:3]+':'+str(first.agr)+':'+str(first.grade)+':'+str(first.posi)+':---:'+str(second.agr)+':'+str(second.grade)+':'+str(second.posi)+':---:'+str(third.agr)+':'+str(third.grade)+':'+str(third.posi)}
    third.save()  
            
def broad_sheets(request):
    eng_tutor = BTUTOR.objects.get(pk=list(set([x[0] for x in list(ANNUAL.objects.filter(subject_by__term__exact='3rd Term', subject_by__Class__exact=request.user.profile.class_in, subject_by__session__exact = SESSION.objects.get(pk=1).new, subject_by__subject__exact=ASUBJECTS.objects.get(name='ENG')).values_list('subject_by'))]))[0])
    student_name_ids = [list(x) for x in list(ANNUAL.objects.filter(subject_by__exact=eng_tutor).values_list('id', 'student_name'))]
    for i in range(0, len(student_name_ids)):
        subj = OVERALL_ANNUAL.objects.create(student_name=get_object_or_404(ANNUAL, pk=student_name_ids[i][0]).student_name, class_in=eng_tutor.Class, teacher_in=request.user,  session=eng_tutor.session, eng = get_object_or_404(ANNUAL, pk=student_name_ids[i][0]))
        subj.save()
    print('Complited')
    a_class = list(set([x[0] for x in list(ANNUAL.objects.filter(subject_by__term__exact='3rd Term', subject_by__Class__exact=request.user.profile.class_in, subject_by__session__exact = SESSION.objects.get(pk=1).new).exclude(subject_by__subject__exact=ASUBJECTS.objects.get(name='ENG')).values_list('subject_by'))]))
    for r in range(0, len(a_class)):
        tutor = BTUTOR.objects.get(pk=a_class[r])
        student_name_id = [x[0] for x in list(ANNUAL.objects.filter(subject_by__exact=tutor).values_list('id'))]
        if tutor.subject.name == 'MAT':
            print('MAT')
            for i in range(0, len(student_name_id)):
                subj = get_object_or_404(OVERALL_ANNUAL, eng__third__student_id=get_object_or_404(ANNUAL, pk=student_name_id[i]).third.student_id)
                subj.mat = get_object_or_404(ANNUAL, pk=student_name_id[i])
                subj.save()
            print('Complited')
        elif tutor.subject.name == 'AGR' and tutor.Class == 'JSS 1' or tutor.Class == 'JSS 2' or tutor.Class == 'JSS 3':
            print('AGR')
            for i in range(0, len(student_name_id)):
                subj = get_object_or_404(OVERALL_ANNUAL, eng__third__student_id=get_object_or_404(ANNUAL, pk=student_name_id[i]).third.student_id)
                subj.agr = get_object_or_404(ANNUAL, pk=student_name_id[i])
                subj.save()
            print('Complited')
        elif tutor.subject.name == 'BUS' or tutor.subject.name == 'LIT' or tutor.subject.name == 'COM' or tutor.subject.name == 'PHY':
            print('BUS')
            for i in range(0, len(student_name_id)):
                if OVERALL_ANNUAL.objects.filter(eng__third__student_id__exact=get_object_or_404(ANNUAL, pk=student_name_id[i]).third.student_id).count() !=0:
                    subj = get_object_or_404(OVERALL_ANNUAL, eng__third__student_id=get_object_or_404(ANNUAL, pk=student_name_id[i]).third.student_id)
                    subj.bus = get_object_or_404(ANNUAL, pk=student_name_id[i])
                    subj.save()
                else:
                    print(get_object_or_404(ANNUAL, pk=student_name_id[i]).third.student_id)
            print('Complited')
        elif tutor.subject.name == 'BST' or tutor.subject.name == 'ECO' or tutor.subject.name == 'BIO':
            print('BST')
            for i in range(0, len(student_name_id)):
                subj = get_object_or_404(OVERALL_ANNUAL, eng__third__student_id=get_object_or_404(ANNUAL, pk=student_name_id[i]).third.student_id)
                subj.bst = get_object_or_404(ANNUAL, pk=student_name_id[i])
                subj.save()
            print('Complited')
        elif tutor.subject.name == 'GEO' or tutor.subject.name == 'YOR' or tutor.subject.name == 'AGR':
            for i in range(0, len(student_name_id)):
                subj = get_object_or_404(OVERALL_ANNUAL, eng__third__student_id=get_object_or_404(ANNUAL, pk=student_name_id[i]).third.student_id)
                subj.yor = get_object_or_404(ANNUAL, pk=student_name_id[i])
                subj.save()
            print('Complited')
        elif tutor.subject.name == 'CIV' or tutor.subject.name == 'NAV':
            print('NAV')
            for i in range(0, len(student_name_id)):
                subj = get_object_or_404(OVERALL_ANNUAL, eng__third__student_id=get_object_or_404(ANNUAL, pk=student_name_id[i]).third.student_id)
                subj.nva = get_object_or_404(ANNUAL, pk=student_name_id[i])
                subj.save()
            print('Complited')
        elif tutor.subject.name == 'IRS':
            print('IRS')
            for i in range(0, len(student_name_id)):
                subj = get_object_or_404(OVERALL_ANNUAL, eng__third__student_id=get_object_or_404(ANNUAL, pk=student_name_id[i]).third.student_id)
                subj.irs = get_object_or_404(ANNUAL, pk=student_name_id[i])
                subj.save()
            print('Complited')  
        elif tutor.subject.name == 'ELE' or tutor.subject.name == 'GRM' or tutor.subject.name == 'CTR' or tutor.subject.name == 'PRV':
            print('PRV')
            for i in range(0, len(student_name_id)):
                subj = get_object_or_404(OVERALL_ANNUAL, eng__third__student_id=get_object_or_404(ANNUAL, pk=student_name_id[i]).third.student_id)
                subj.prv = get_object_or_404(ANNUAL, pk=student_name_id[i])
                subj.save()
            print('Complited')
        elif tutor.subject.name == 'GOV' or tutor.subject.name == 'ICT':
            for i in range(0, len(student_name_id)):
                subj = get_object_or_404(OVERALL_ANNUAL, eng__third__student_id=get_object_or_404(ANNUAL, pk=student_name_id[i]).third.student_id)
                subj.ict = get_object_or_404(ANNUAL, pk=student_name_id[i])
                subj.save()
            print('Complited')
        elif tutor.subject.name == 'ACC' or tutor.subject.name == 'CHE' or tutor.subject.name == 'ARB':
            print('ARB')
            for i in range(0, len(student_name_id)):
                subj = get_object_or_404(OVERALL_ANNUAL, eng__third__student_id=get_object_or_404(ANNUAL, pk=student_name_id[i]).third.student_id)
                subj.acc = get_object_or_404(ANNUAL, pk=student_name_id[i])
                subj.save()
            print('Complited')
        elif tutor.subject.name == 'HIS':
            print('HIS')
            for i in range(0, len(student_name_id)):
                subj = get_object_or_404(OVERALL_ANNUAL, eng__third__student_id=get_object_or_404(ANNUAL, pk=student_name_id[i]).third.student_id)
                subj.his = get_object_or_404(ANNUAL, pk=student_name_id[i])
                subj.save()
            print('Complited')
    return redirect('broadsheet_last_stage')


def pre_broad_sheet(request):
    al = OVERALL_ANNUAL.objects.filter(teacher_in__exact=request.user, class_in__exact=request.user.profile.class_in, session__exact=SESSION.objects.get(pk=1).new)
    return render(request, 'result/pre_broadsheet.html',  {'date': datetime.now(), 'in_class': al, 'last_name':request.user.profile.last_name, 'first_name':request.user.profile.first_name, 'class_in':request.user.profile.class_in })
   
def broadsheet_last_stage(request):
    al = ANNUAL.objects.filter(subject_by__Class__exact=request.user.profile.class_in, session__exact = SESSION.objects.get(pk=1).new)
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
            
        name_ids = [list(i[:]) for i in list(al.values_list('id', 'AVR'))]
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
        grad = []
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
  

['acc', 'agr', 'bst', 'bus', 'eng', 'his', 'ict', 'irs', 'mat', 'nva', 'prv', 'yor']

def class_subjects(request, valid_subj):
    annuals = ANNUAL.objects.select_related('subject_by').filter(subject_by__subject__name__in= valid_subj, subject_by__Class__exact=request.user.profile.class_in, subject_by__session__exact = session)
    if annuals.count() != 0:
        subj_list = sorted(list(set([x.subject_by.subject.name for x in annuals])))
        valid_subj = valid_subj
        compared = [i for i in subj_list if i not in valid_subj]
        if len(compared) == 0:
            print('Satisfied!')
        else:
            completed = subj_list + compared
            subj_list = sorted(completed)
        listed = [[x for x in annuals if x.subject_by.subject==get_object_or_404(ASUBJECTS, name=i)] for i in subj_list]
        nulls = [[None]*list(set([len(i) for i in listed]))[-1] for i in list(set([len(i) for i in listed])) if i == 0]
        for r in range(len(nulls)):
            for i in range(len(listed)):
                if len(listed) == 0:
                    listed[i] = listed[i] + nulls[r]
        return listed
    else:
        return redirect('home')


def extract_records(request):
    al = OVERALL_ANNUAL.objects.select_related('teacher_in').filter(teacher_in__exact=request.user, class_in__exact=request.user.profile.class_in, session__exact=session)
    if request.user.profile.class_in == 'JSS 1' or request.user.profile.class_in == 'JSS 2' or request.user.profile.class_in == 'JSS 3':
        listed = class_subjects(request, ['AGR', 'ARB', 'BST', 'BUS', 'ENG', 'HIS', 'IRS', 'MAT', 'NAV', 'PRV', 'YOR'])
        [OVERALL_ANNUAL.objects.create(student_name=e.student_name, class_in=e.subject_by.Class, teacher_in=request.user,  session=e.subject_by.session, agr = a, acc = c, bst = b, bus = u, eng = e, his = h, irs = i, mat = m, nva = n, prv = p, yor = y).save() for (a,c,b,u,e,h,i,m, n, p, y) in zip(listed[0],listed[1],listed[2],listed[3],listed[4],listed[5],listed[6],listed[7],listed[8],listed[9],listed[10])]
        annual_id = [list(x) for x in list(al.values_list('id', 'agr', 'acc', 'bst', 'bus', 'eng', 'his', 'irs', 'mat', 'nva', 'prv', 'yor')) if x != None]

    else:
        Sci = class_subjects(request, ['CHE', 'BIO', 'PHY', 'ENG', 'ICT', 'IRS', 'MAT', 'CIV', 'GEO'])#Sciences
        Art = class_subjects(request, ['ACC', 'BIO', 'CIV', 'ENG', 'GOV', 'IRS', 'LIT', 'MAT', 'YOR'])#Arts
        Com = class_subjects(request, ['AGR', 'ARB', 'CIV', 'COM', 'ECO', 'ENG', 'GOV', 'IRS', 'MAT'])#Comercials
        listed = [x+y+z for x,y,z,i in zip(Sci, Art,Com)]
        ent = ANNUAL.objects.select_related('subject_by').filter(subject_by__subject__name__in= ['ELE', 'CTR', 'GRM'], subject_by__Class__exact=request.user.profile.class_in, subject_by__session__exact = session)
        all_ent = [x for x in ent if x.student_name in [i.student_name for i in listed[3]]]
        listed = listed + all_ent#margged_list
        [OVERALL_ANNUAL.objects.create(student_name=d.student_name, class_in=d.subject_by.Class, teacher_in=request.user,  session=d.subject_by.session, acc = a, bst = b, bus = c, eng = d, ict = e, irs = f, mat = g, nva = h, prv = i, yor = j).save() for (a,b,c,d,e,f,g, h, i, j) in zip(listed[0],listed[1],listed[2],listed[3],listed[4],listed[5],listed[6],listed[7],listed[8],listed[9])]
        annual_id = [list(x) for x in list(al.values_list('id', 'acc', 'bst', 'bus', 'eng', 'ict', 'irs', 'mat', 'nva', 'prv', 'yor')) if x != None]

    return annual_id


heading = []   
head = ['student_name']
if len(head) == 12:
    heading += [head+['ANU', 'AVG', 'GRD', 'POS']]
    head = ['student_name']
def xtra(i):
    global head
    if i == None:
        return None
    else:
         if QSUBJECT.objects.get(pk=i).tutor.subject.name not in head:
             head += ['1st', '2nd', '3rd', QSUBJECT.objects.get(pk=i).tutor.subject.name]
         return QSUBJECT.objects.get(pk=i).agr#3rd
def lkup(x):
    if x == None:
        return None
    else:
        return [xtra(i) for i in list(ANNUAL.objects.filter(pk=x.id).values_list('first', 'second', 'third'))[0]]
class broadsheet_in_pdf(View):
    def get(self, request):
        al = OVERALL_ANNUAL.objects.select_related('teacher_in').filter(teacher_in__exact=request.user, class_in__exact=request.user.profile.class_in, session__exact=SESSION.objects.get(pk=1).new)
        today = datetime.now()
        params = {
            'in_class': al.count(),
            'mains': al.order_by('order'),
            'today': today,
            'subject_scores': round(al.aggregate(Sum('AVR'))['AVR__sum'], 2),
            'subject_pert': round(al.aggregate(Avg('AVR'))['AVR__avg'],2),
            'request':request
            }
        if  request.user.profile.class_in == 'SSS 1' or request.user.profile.class_in == 'SSS 2' or request.user.profile.class_in == 'SSS 3':
           if request.user.profile.account_id == '0':
                return Render.render('result/broad_sheet_pdf_s.html', params)
           else:
                return Render.render('result/broad_sheet_pdf_s_1.html', params)
        else:
            if request.user.profile.account_id == '0':
                return Render.render('result/broad_sheet_pdf_j.html', params)
            else:
                return Render.render('result/broad_sheet_pdf_j_1.html', params)
def broad_pages(request, pk):
    user = Edit_User.objects.get(user = request.user)
    user.account_id = int(pk)
    user.save()
    print(request.user.profile.account_id)
    return redirect('broadsheets')

def xtra(i):#retrieve agr or return None
    if i == None:
        return None
    else:
         return QSUBJECT.objects.get(pk=i).agr#3rd
         
def lkup(x):#retrieve 1st, 2nd, 3rd or return None
    if x == None:
        return [None, None, None]
    else:
        return [xtra(i) for i in list(ANNUAL.objects.filter(pk=x.id).values_list('first', 'second', 'third'))[0]]
def agr(y):#retrieve Agr or return None
    if y == None:
        return None
    else:
        return y.Agr
  
def broadsheets(request):
    al = OVERALL_ANNUAL.objects.select_related('teacher_in').filter(teacher_in__exact=request.user, class_in__exact=request.user.profile.class_in, session__exact=SESSION.objects.get(pk=1).new).order_by('order')
    if len(al)!= 0:
        avg = [round(al.aggregate(Sum('AVR'))['AVR__sum'], 2), round(al.aggregate(Avg('AVR'))['AVR__avg'],2), al.count(), request.user.profile.class_in, 'BROADSHEET']
        if request.user.profile.class_in == 'JSS 1' or request.user.profile.class_in == 'JSS 2' or request.user.profile.class_in == 'JSS 3':
            header = ['student_name', '1st', '2nd', '3rd', 'Arb', '1st', '2nd', '3rd', 'Agr', '1st', '2nd', '3rd', 'Bst', 'ANU', 'AVG', 'GRD', 'POS']
            data = [[[x.student_name.full_name]+lkup(x.acc)+[agr(x.acc)]+lkup(x.agr)+[agr(x.agr)]+lkup(x.bst)+[agr(x.bst)]+[x.AGR]+[x.AVR]+[x.GRD]+[x.POS]][0] for x in al]
            cont1 = [['Subject cont..', '1st', '2nd', '3rd', 'His', '1st', '2nd', '3rd', 'Eng', '1st', '2nd', '3rd', 'Irs', 'ANU', 'AVG', 'GRD', 'POS']]+[[[x.student_name.full_name]+lkup(x.ict)+[agr(x.ict)]+lkup(x.eng)+[agr(x.eng)]+lkup(x.irs)+[agr(x.irs)]+[x.AGR]+[x.AVR]+[x.GRD]+[x.POS]][0] for x in al]
            cont2 = [['Subject cont..', '1st', '2nd', '3rd', 'Nav', '1st', '2nd', '3rd', 'Prv', '1st', '2nd', '3rd', 'Yor', 'ANU', 'AVG', 'GRD', 'POS']]+[[[x.student_name.full_name]+lkup(x.nva)+[agr(x.nva)]+lkup(x.prv)+[agr(x.prv)]+lkup(x.yor)+[agr(x.yor)]+[x.AGR]+[x.AVR]+[x.GRD]+[x.POS]][0] for x in al]
            cont3 = [['Subject cont..', '1st', '2nd', '3rd', 'Bus', '1st', '2nd', '3rd', 'Mat', '1st', '2nd', '3rd', 'None', 'ANU', 'AVG', 'GRD', 'POS']]+[[[x.student_name.full_name]+lkup(x.bus)+[agr(x.bus)]+lkup(x.mat)+[agr(x.mat)]+[None, None, None, None]+[x.AGR]+[x.AVR]+[x.GRD]+[x.POS]][0] for x in al]
        else:
            header = ['student_name', '1st', '2nd', '3rd', 'Arb', '1st', '2nd', '3rd', 'Lit', '1st', '2nd', '3rd', 'Bio', 'ANU', 'AVG', 'GRD', 'POS']
            data = [[[x.student_name.full_name]+lkup(x.acc)+[agr(x.acc)]+lkup(x.bus)+[agr(x.bus)]+lkup(x.bst)+[agr(x.bst)]+[x.AGR]+[x.AVR]+[x.GRD]+[x.POS]][0] for x in al]
            cont1 = [['Subject cont..', '1st', '2nd', '3rd', 'Ict', '1st', '2nd', '3rd', 'Eng', '1st', '2nd', '3rd', 'Irs', 'ANU', 'AVG', 'GRD', 'POS']]+[[[x.student_name.full_name]+lkup(x.ict)+[agr(x.ict)]+lkup(x.eng)+[agr(x.eng)]+lkup(x.irs)+[agr(x.irs)]+[x.AGR]+[x.AVR]+[x.GRD]+[x.POS]][0] for x in al]
            cont2 = [['Subject cont..', '1st', '2nd', '3rd', 'Civ', '1st', '2nd', '3rd', 'Ent', '1st', '2nd', '3rd', 'Yor', 'ANU', 'AVG', 'GRD', 'POS']]+[[[x.student_name.full_name]+lkup(x.nva)+[agr(x.nva)]+lkup(x.prv)+[agr(x.prv)]+lkup(x.yor)+[agr(x.yor)]+[x.AGR]+[x.AVR]+[x.GRD]+[x.POS]][0] for x in al]
            cont3 = [['Subject cont..', '1st', '2nd', '3rd', 'None', '1st', '2nd', '3rd', 'Mat', '1st', '2nd', '3rd', 'None', 'ANU', 'AVG', 'GRD', 'POS']]+[[[x.student_name.full_name]+lkup(x.agr)+[agr(x.agr)]+lkup(x.mat)+[agr(x.mat)]+[None, None, None, None]+[x.AGR]+[x.AVR]+[x.GRD]+[x.POS]][0] for x in al]
        data = data+cont1+cont2+cont3
        df = pd.DataFrame(data)
        df.columns = header
        sd = []
        for i in range(4):
            if i!=0:
                sd+=[None]
            sd = sd+[i+1 for i in range(al.count())]
        df.index = sd
        df.to_csv(os.path.join(settings.MEDIA_ROOT, 'csvs/'+request.user.profile.class_in+'_'+str(SESSION.objects.get(pk=1).new)+'.csv'), encoding='ISO-8859-1')
        #path =  #'C:/office/jango_env/uqi/result'
        os.chdir(settings.MEDIA_ROOT)
        with open(os.path.join(settings.MEDIA_ROOT, 'csvs/'+request.user.profile.class_in+'_'+str(SESSION.objects.get(pk=1).new)+'.csv'), "r") as csvfile:
            data = list(csv.reader(csvfile)) 
        return building(request, [data, avg])
    else:
        return redirect('home')
    
    
def export_subject_scores(request, pk):#result download based on login tutor
    tutor = get_object_or_404(BTUTOR, pk=pk)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename={subject}-{Class}-{term}-scores.csv".format(subject=tutor.subject,Class=tutor.Class,term = tutor.term)
    writer = csv.writer(response)
    writer.writerow(['student_name', 'test', 'agn', 'atd', 'total', 'exam', 'agr', 'grade', 'posi'])
    subject = QSUBJECT.objects.filter(tutor__exact=tutor).values_list('student_name', 'test', 'agn', 'atd', 'total', 'exam', 'agr', 'grade', 'posi')
    sd = [list(x) for x in subject]
    for i in range(0, len(sd)):
    	sd[i][0] = CNAME.objects.get(pk=sd[i][0]).last_name +' '+ CNAME.objects.get(pk=sd[i][0]).first_name
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
            ds = [CNAME.objects.get(pk=x[i][0]).last_name +' '+ CNAME.objects.get(pk=x[i][0]).first_name]
            try:
                while True:
                    lst[i][lst[i].index(None)] = 0
            except ValueError:
                pass         
            for r in range(1, len(lst[i])):
                if lst[i][r] != 0:
                    ds += [ANNUAL.objects.get(pk=lst[i][r]).Agr]
                    dim += [mid[r-1]]
            sd += [ds+lss[i]]
    return [sd, dim[:3]+['Agr', 'Avr', 'grade', 'posi']]

def export_broadsheet(request):#result download based on login tutor teacher_accounts Subject_model_view
    sd = extract_broad_sheet(request)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename={Class}/{Session}-broadsheet.csv".format(class_in=request.user.profile.class_in, session = SESSION.objects.get(pk=1).new)
    writer = csv.writer(response)
    writer.writerow(sd[1])
    for each in sd[0]:
        writer.writerow(each)
    return response 


def export_third_scores(request, pk):#result download based on login tutor 
    tutor = get_object_or_404(BTUTOR, pk=pk)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename={subject}-{Class}-{term}-scores.csv".format(subject=tutor.subject,Class=tutor.Class,term = tutor.term)
    writer = csv.writer(response)
    writer.writerow(['student_name', 'test', 'agn', 'atd', 'total', 'exam', 'third', 'second', 'first', 'anual', 'Agr', 'Grade', 'Posi'])
    previous = BTUTOR.objects.filter(Class__exact = tutor.Class, subject__exact = tutor.subject, session__exact=tutor.session).exclude(term__exact='3rd Term')
    
    previous_id = sorted([i[0] for i in list(previous.values_list('id'))])
    
    third = [list(x[:]) for x in QSUBJECT.objects.filter(tutor__exact=tutor).values_list('student_name', 'test', 'agn', 'atd', 'total', 'exam', 'agr')]
    second = [list(i[:]) for i in QSUBJECT.objects.filter(tutor__exact=get_object_or_404(BTUTOR, pk=previous_id[1])).values_list('student_name', 'agr') if i[0] in [i[0] for i in third]]
    first = [list(i[:]) for i in QSUBJECT.objects.filter(tutor__exact=get_object_or_404(BTUTOR, pk=previous_id[0])).values_list('student_name', 'agr') if i[0] in [i[0] for i in third]]
    annual = [list(x[:]) for x in list(ANNUAL.objects.filter(subject_by__exact=tutor).values_list('student_name', 'anual', 'Agr', 'Grade', 'Posi'))]
    
    first = [x for x in first if x[0] in [i[0] for i in third]]
    second = [x for x in second if x[0] in [i[0] for i in third]]
    annual = [x for x in annual if x[0] in [i[0] for i in third]]
    
    names_in_three_terms = [x for x in [i[0] for i in third] if x in [i[0] for i in second] and x in [i[0] for i in first]]
    second_third_only = list(set([i[0] for i in third]) - set(names_in_three_terms))
    
    scores_in_three_terms = [x for x in third if x[0] in names_in_three_terms]
    second_third_only_r = [x for x in third if x[0] in second_third_only]
    
    scores_in_annual = [x for x in annual if x[0] in names_in_three_terms]
    scores_in_annual_r = [x for x in annual if x[0] in second_third_only]
    
    list_com = [t + [s[1]] + [f[1]] + a[1:] for t,s,f,a in zip(scores_in_three_terms, second, first, scores_in_annual)]
    
    second = [x for x in second if x[0] in second_third_only]
    if len(second) != 0:
        list_com_r = [t + [s[1]] + [f[1]] + a[1:] for t,s,f,a in zip(second_third_only_r, second, [[None, None]]*len(second_third_only), scores_in_annual_r)]
    else:
        list_com_r = [t + [s[1]] + [f[1]] + a[1:] for t,s,f,a in zip(second_third_only_r, [[None, None]]*len(second_third_only), [[None, None]]*len(second_third_only), scores_in_annual_r)]
    
    union = sorted([x for x in list_com + list_com_r if x[0] in [i[0] for i in third]])
    
    for each in union:
        each[0] = CNAME.objects.get(pk=each[0]).last_name +' '+ CNAME.objects.get(pk=each[0]).first_name
        writer.writerow(each)
    return response   
        
    
class terms_in_pdf(View):
    def get(self, request):
        tutor = get_object_or_404(BTUTOR, pk=int(str(request.user.profile.account_id.split('_')[0])))
        if tutor.term == '3rd Term':
            if int(str(request.user.profile.account_id.split('_')[1])) !=0:
                mains = ANNUAL.objects.filter(subject_by__exact=tutor, third__gender = int(str(request.user.profile.account_id.split('_')[1]))).order_by('student_name')
            else:
                mains = ANNUAL.objects.filter(subject_by__exact=tutor).order_by('student_name')
            x = round(mains.aggregate(Sum('Agr'))['Agr__sum'],2)
            y = round(mains.aggregate(Avg('Agr'))['Agr__avg'],2)
            all_count = ANNUAL.objects.filter(subject_by__exact=tutor).count()
            all_x = round(ANNUAL.objects.filter(subject_by__exact=tutor).aggregate(Sum('Agr'))['Agr__sum'],2)
            all_y = round(ANNUAL.objects.filter(subject_by__exact=tutor).aggregate(Avg('Agr'))['Agr__avg'],2)
        else:
            if int(str(request.user.profile.account_id.split('_')[1])) !=0:
                mains = QSUBJECT.objects.filter(tutor__exact=tutor, gender = int(str(request.user.profile.account_id.split('_')[1]))).order_by('student_name')
            else:
                mains = QSUBJECT.objects.filter(tutor__exact=tutor).order_by('student_name')
            x = round(mains.aggregate(Sum('agr'))['agr__sum'],2)
            y = round(mains.aggregate(Avg('agr'))['agr__avg'],2)
            all_count = QSUBJECT.objects.filter(tutor__exact=tutor).count()
            all_x = round(QSUBJECT.objects.filter(tutor__exact=tutor).aggregate(Sum('agr'))['agr__sum'],2)
            all_y = round(QSUBJECT.objects.filter(tutor__exact=tutor).aggregate(Avg('agr'))['agr__avg'],2)
        today = datetime.now()
        params = {
            'count_grade': mains.count(),
            'tutor': tutor,
            'request': request,
            'mains': mains,
            'today': today,
            'subject_scores': x,
            'subject_pert': y,
            'all_count': all_count,
            'all_x': all_x,
            'all_y' : all_y
        }
        if tutor.term == '3rd Term':
            return Render.render('result/anu_pdf.html', params)
        else:
            return Render.render('result/pdf.html', params)
        

