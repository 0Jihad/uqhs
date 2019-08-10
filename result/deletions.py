from .models import QSUBJECT, BTUTOR, Post#, OVERALL_ANNUAL, TERM, SESSION
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required#, @permission_required

@login_required
def confirm_deleting_a_user(request, pk):
    qry = get_object_or_404(User, pk=pk)
    return render(request, 'result/confirm_delete_a_user.html', {'qry' : qry, 'pk': pk}) 
@login_required
def yes_no(request, pk):#delete single candidate
    qry = get_object_or_404(User, pk=pk)
    return render(request, 'result/yes_no.html', {'qry' : qry, 'pk': pk})
@login_required  
def delete_user(request, pk):#delete single candidate
    get_object_or_404(User, pk=pk).delete()
    return redirect('all_accounts')

@login_required
def confirm_deletion(request, pk):#sort for a deletion confirmation
    qry = get_object_or_404(QSUBJECT, pk=pk)
    return render(request, 'result/confirm_delete_a_student.html', {'qry' : qry, 'pk': pk})
@login_required
def confirmed_delete(request, pk):#Yes delete
    get_object_or_404(QSUBJECT, pk=pk).delete()
    return redirect('student_in_none')

@login_required
def confirm_deletions(request, pk):#sort for many deletions confirmations
    qry = get_object_or_404(BTUTOR, pk=pk)
    qery =  QSUBJECT.objects.filter(tutor__term__exact=qry.term, tutor__Class__exact=qry.Class, tutor__subject__exact=qry.subject, tutor__exact = qry)
    return render(request, 'result/confirm_deletes_a_class.html', {'qery' : qery, 'pk': pk, 'qry' : qry})
@login_required
def delete_all(request, pk):#Yes deletes
    qry = get_object_or_404(BTUTOR, pk=pk)
    QSUBJECT.objects.filter(tutor__term__exact=qry.term, tutor__Class__exact=qry.Class, tutor__subject__exact=qry.subject, tutor__exact = qry).delete()
    qry.delete()
    return redirect('home')

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('my_post_list')