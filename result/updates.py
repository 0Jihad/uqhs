from django.contrib.auth.models import User
from .models import QSUBJECT, CNAME, BTUTOR, Edit_User#, SESSION
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.forms import modelformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import ProfileForm, student_names
from result.utils import do_grades, do_positions, cader

def edit_user(request, pk):##mark for remove
    user = User.objects.get(pk=pk)
    user.is_staff = True
    if request.method == "POST":
        profile = Edit_User.objects.get(user = user)
        form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            user.last_name = form.cleaned_data['last_name']
            user.first_name = form.cleaned_data['first_name']
            user.save()
            profile.title = form.cleaned_data['title']
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
            profile.save()
            if request.user.is_authenticated:
                return redirect('home')
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

class Teacher_model_view(UpdateView):#New teacher form for every new term, class, subjects
    model = BTUTOR
    fields = ['accounts', 'teacher_name', 'subject', 'Class', 'term', 'males', 'females', 'teacher_in', 'session']
    success_url = reverse_lazy('home') 
   
class Subject_model_view(LoginRequiredMixin, UpdateView):#New teacher form for every new term, class, subjects
    model = QSUBJECT
    fields = ['student_name', 'test', 'agn', 'atd', 'total', 'exam', 'agr', 'grade', 'posi', 'tutor']
    
class Cname_edit(LoginRequiredMixin, UpdateView):#New teacher form for every new term, class, subjects
    model = CNAME
    fields = ['student_name']
    
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

############################################################################### student_in_None
@login_required
def profiles(request, pk):#show single candidate profile
    qry = get_object_or_404(Edit_User, user=get_object_or_404(User, pk=pk))
    return render(request, 'result/profiles.html', {'qry' : qry, 'pk':pk})


#@login_required
class ProfileUpdate(UpdateView):
    model = Edit_User
    fields = ['first_name', 'last_name', 'bio', 'phone', 'city', 'department', 'location', 'birth_date', 'country', 'organization', 'class_in', 'photo']
    success_url = reverse_lazy('home')

@login_required
def profile_picture(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST' and request.FILES['myfile']:
        profile = Edit_User.objects.get(user = user)
        if profile.photo.name:#if there is file name entry, delete it
            import os
            from django.conf import settings
                       #we delete the previous image
            os.remove(os.path.join(settings.MEDIA_ROOT,str(profile.photo.name)))
        profile.photo = request.FILES['myfile']
        profile.save()
        return redirect('pro_detail', pk=pk)
    return render(request, 'result/picture.html')  

class Users_update(UpdateView):#New teacher form for every new term, class, subjects
    model = User
    fields = '__all__'
    success_url = reverse_lazy('all_accounts')


def many_student_updates(request, pk):#tutor
    query = QSUBJECT.objects.filter(tutor__exact=BTUTOR.objects.get(pk=pk))
    students = list(query.values_list('id'))
    ids = [r[0] for r in students]
    for i in range(0, query.count()):
        obj = QSUBJECT.objects.get(pk=ids[i])
        obj.total = obj.test + obj.agn + obj.atd
        obj.agr = obj.exam + obj.total
        obj.grade = do_grades([obj.agr], cader(obj.tutor.Class))[0]
        obj.save()
    return redirect('position_updates', pk=pk)


#@login_required
def single_student_update(request, pk):#student
    obj = QSUBJECT.objects.get(pk=pk)
    if obj.tutor != None:
        obj.total = obj.test + obj.agn + obj.atd
        obj.agr = obj.exam + obj.total
        obj.grade = do_grades([obj.agr], cader(obj.tutor.Class))[0]
        obj.save()
        return redirect('position_updates', pk=obj.tutor.id)
    else:
        return redirect('home')
@login_required
def subject_position_updates(request, pk):#all
    query = QSUBJECT.objects.filter(tutor__exact=BTUTOR.objects.get(pk=pk))
    students = [x[:] for x in list(query.values_list('agr', 'id')) if x[0] != None]
    agr = [r[0] for r in students]###############news
    posi = do_positions(agr[:])
    ids = [r[1] for r in students]
    for i in range(0, len(agr)):
        objs = QSUBJECT.objects.get(pk=ids[i])
        objs.posi = posi[i]
        objs.save()
    return redirect('subject_view', pk=pk)
        
