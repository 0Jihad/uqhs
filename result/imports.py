######################STAGE 2 ::: UPLOAD SCORES##################STARTS
from .forms import a_student_form_new, student_name
from collections import Counter
from .models import QSUBJECT, CNAME, BTUTOR
from django.shortcuts import render, redirect, get_object_or_404
from result.utils import do_grades, do_positions, cader
from django.contrib.auth.decorators import login_required
def bst1_plus_bst2(dim):
    result = []
    for i in range(0, len(dim)):
        result += [[int(round((sum(dim[i][0:2])/sum(x > 0 for x in dim[i][0:2])+0.1), 0)), int(round((sum(dim[i][2:4])/sum(x > 0 for x in dim[i][2:4])+0.1), 0)), int(round((sum(dim[i][4:6])/sum(x > 0 for x in dim[i][4:6])+0.1), 0)), int(round((sum(dim[i][6:8])/sum(x > 0 for x in dim[i][6:8])+0.1), 0))]]
    return result 

def check(inp):
    try:
        inp = inp.replace(',', '.')
        num_float = float(inp)
        num_int = int(num_float)
        return num_int == num_float
    except ValueError:
        return False

@login_required
def upload_new_subject_scores(request, pk):
    import time
    from datetime import timedelta
    from django.contrib import messages
    start_time = time.time()
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
            output = [check(s) for s in valid_input[i]]
            if len(output) == 9:
                if output != [False, True, True, True, True, True, True, True, True]:
                    return render(request, 'result/InputTypeError.html', {'int':i, 'invalid': valid_input[i]})
            elif len(output) == 5:
                if output != [False, True, True, True, True]:
                    return render(request, 'result/InputTypeError.html', {'int':i, 'invalid': valid_input[i]})
            else:
                return render(request, 'result/InputTypeError.html', {'int':i, 'invalid': valid_input[i]}) 
                

            named_scores[1] += [[int(float(ints)) for ints in valid_input[i][1:]]]#[scores[1]
            named_scores[2] += [valid_input[i][0]]# names[2]]
        if len(named_scores[1][0]) == 8:#BST ONLY: Reduced 8 to 4 columns by averaging.
            x_y = bst1_plus_bst2(named_scores[1])
            named_scores[1] = x_y
        x = cader(tutor.Class)
        raw = []
        for i in range(0, len(named_scores[1])):
            raw += [[i+1]+named_scores[1][i]+[sum(named_scores[1][i][:3])]+[sum([named_scores[1][i][3]+sum(named_scores[1][i][:3])])]]
        agr = [[i[1:] for i in raw]]
        grade = do_grades([r[-1] for r in raw][:], x)
        posi = do_positions([r[-1] for r in raw][:])
        #####################REPEATED NAMES######################################
        word_counts = Counter(named_scores[2])
        top_three = word_counts.most_common()
        xy = [list(i[:]) for i in top_three]
        sd = []
        for i in range(0, len(xy)):
            if xy[i][1] > 1:
                sd += [xy[i]]
        if len(sd) != 0:
            for i in range(0, len(sd)):  
                for r in range(0, sd[i][1]):
                    for s in named_scores[2]:
                        if s == sd[i][0]:
                            named_scores[2][named_scores[2].index(sd[i][0])] = named_scores[2][named_scores[2].index(sd[i][0])]+str(named_scores[2].index(sd[i][0]))
        #####################REPEATED NAMES######################################
        for i in range(0, len(named_scores[2])):
            name = CNAME.objects.filter(student_name__exact=named_scores[2][i]).count()#if name exits else create name
            if name == 0:
                new_name = CNAME(student_name=named_scores[2][i].upper())#adding new student_name
                new_name.save()
            per_student = QSUBJECT(student_name=CNAME.objects.get(student_name__exact=named_scores[2][i]), test=agr[0][i][0], agn=agr[0][i][1], atd=agr[0][i][2], exam=agr[0][i][3], total=agr[0][i][4], agr=agr[0][i][5], posi=posi[i], grade=grade[i], tutor = tutor, cader = x)
            per_student.save() 
        elapsed_time_secs = time.time() - start_time
        msg = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
        print(msg)
        messages.success(request, msg)
        
    else:#
        return render(request, 'result/loader.html', {'pk':pk, 'qry':tutor})
    ######################STAGE 2 ::: UPLOAD SCORES##################ENDS
    return redirect('tutor_summary', pk=pk)#summarise all tutor's uploads

@login_required
def upload_a_student_subject(request, pk):
    tutor = get_object_or_404(BTUTOR, pk=pk)
    if request.method == 'POST':
        result =  a_student_form_new(request.POST)
        if result.is_valid():
            exist_student = QSUBJECT(student_name=CNAME.objects.get(student_name__exact=result.cleaned_data['student_name']), test=result.cleaned_data['test'], agn=result.cleaned_data['agn'], atd=result.cleaned_data['atd'], exam=result.cleaned_data['exam'], tutor = tutor)
            exist_student.save() 
            return redirect('subject_updates_model', pk=exist_student.id)
    else:
        result = a_student_form_new()
    return render(request, 'result/a_student_form.html', {'result': result, 'pk': pk})

def upload_a_name(request, pk):
    if request.method == 'POST':
        result = student_name(request.POST)
        if result.is_valid():
            new_name = CNAME(student_name=result.cleaned_data['student_name'].upper())#adding new student_name
            new_name.save() 
            return redirect('a_student_exist', pk=pk)
    else:
        result = student_name()
    return render(request, 'result/a_student_name.html', {'result': result})
