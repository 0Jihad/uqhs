from django.contrib import admin

from .models import ASUBJECTS, BTUTOR, CNAME, QSUBJECT, ANNUAL, TERM, Edit_User, RESULT_GRADE, OVERALL_ANNUAL

#admin.site.register(studen_scores)#
########################################################
# Define the admin class
class subject_main(admin.ModelAdmin):
    list_display = ('student_name', 'logged_in', 'test', 'agn', 'atd', 'total', 'exam', 'agr', 'grade', 'posi', 'cader', 'tutor')
    fields = [('student_name', 'gender', 'logged_in', 'tutor'), ('test', 'agn', 'atd', 'total', 'exam', 'agr'), ('grade', 'posi')]#, 'subject']
@admin.register(BTUTOR)
class model_teacher(admin.ModelAdmin):
    list_display = ('model_in','accounts', 'cader', 'teacher_name', 'subject', 'Class', 'term', 'model_summary', 'session')
    fields = ['cader', 'model_in','accounts', 'teacher_name', 'subject', 'Class', 'term', 'graded', 'model_summary', 'session']

@admin.register(TERM)
class model_term(admin.ModelAdmin):
    list_display = ('student_name', 'class_in', 'subject', 'first', 'second', 'third')
    fields = ['student_name', 'class_in', 'subject', 'first', 'second', 'third']

@admin.register(OVERALL_ANNUAL)
class model_qsubject(admin.ModelAdmin):
    list_display = ('student_name','class_in', 'eng', 'mat', 'bus', 'bst', 'yor', 'nva', 'irs', 'prv', 'ict', 'agr', 'his', 'Agr', 'Avr', 'grade', 'posi')
    fields = [('student_name','class_in'), ('eng', 'mat', 'bus', 'bst', 'yor', 'nva', 'irs', 'prv', 'ict', 'agr', 'his'), ('Agr', 'Avr', 'grade', 'posi')]

@admin.register(RESULT_GRADE)
class model_Graded(admin.ModelAdmin):
    list_display = ('subject', 'identifier', 'grade_A', 'grade_C', 'grade_P', 'grade_F', 'grade_A1', 'grade_B2', 'grade_B3', 'grade_C4', 'grade_C5', 'grade_C6', 'grade_D7', 'grade_E8', 'grade_F9', 'remark')
    fields = ['identifier', 'subject', ('grade_A1', 'grade_B2', 'grade_B3'), ('grade_C4', 'grade_C5', 'grade_C6'), ('grade_D7', 'grade_E8', 'grade_F9'), ('grade_A', 'grade_C', 'grade_P', 'grade_F'), 'remark']   

@admin.register(ANNUAL)
class model_annual(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'first', 'second', 'third', 'anual', 'agr', 'grade', 'anu_posi', 'subject_by', 'subject')
    fields = ['student_name', ('first', 'second', 'third', 'anual'), ('agr', 'grade', 'anu_posi'), ('subject_by', 'subject')]
@admin.register(CNAME)
class model_names(admin.ModelAdmin):
    list_display = ('student_name', 'id', 'created', 'updated')
@admin.register(Edit_User)
class model_profile(admin.ModelAdmin):
    list_display = ('user', 'account_id', 'photo', 'bio', 'phone', 'city', 'country', 'organization', 'location', 'birth_date', 'department')
    fields = ['user', 'account_id', 'photo', 'bio', 'phone', 'city', 'country', 'organization', 'location', 'birth_date', 'department', 'email_confirmed']
#admin.site.register(RESULT_GRADE)
admin.site.register(ASUBJECTS)
admin.site.register(QSUBJECT, subject_main)#second_term
# Register your models here.
