# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 01:15:37 2019

@author: AdeolaOlalekan
"""
#from django.contrib.auth import views as auth_views
from django.conf.urls import url
#, include student_name_edit, subject_per_name
from.import result_views, model_loader, loggins, sign_up
urlpatterns = [
        url(r'home/$', loggins.home, name='home'),
        url(r'^generate/anual/(?P<pk>\d+)/', result_views.annual_agr, name='anual'),
        url(r'^get_total/(?P<pk>\d+)/', result_views.subject_total, name='get_total'),
        url(r'^upload_txt/(?P<pk>\d+)/', model_loader.upload_new_subject_scores, name='upload_txt'),
        url(r'^extract_name/subjects/(?P<pk>\d+)/', loggins.export_name_text, name='extract_name'),
        url(r'^export/scores/subjects/(?P<pk>\d+)/', loggins.export_subject_scores, name='export_users_scores'),
        url(r'^export/scores/annual/(?P<pk>\d+)/', loggins.export_annual_scores, name='export_annual_scores'),
        url(r'logins/', loggins.loggin, name='logins'),
        url('log_out/', loggins.logout, name='log_out'),
        url('subject_class_term_filter/', loggins.subject_class_term_filter, name='subject_class_term_filter'),
        url('student_name_class_filter/', loggins.student_name_class_filter, name='student_name_class_filter'),
        url('tutor_class_filter/', loggins.tutor_class_filter, name='tutor_class_filter'),
        url('subject_home/(?P<pk_code>[\w\-]+)/', loggins.subject_home, name='subject_home'),
        url('student_in_none/', loggins.student_in_None, name='student_in_none'),
        url('create_subject/', loggins.create_subjects, name='create_subject'),
        url('tutor_summary/(?P<pk>\d+)/', result_views.tutor_model_summary, name='tutor_summary'),
        url('created_subject_list/(?P<pk>\d+)/', loggins.created_subjects, name='created_subject_list'),
        url('teacher/create/', model_loader.create_new_subject_teacher, name='teacher_create'),
        url('tutor/(?P<pk>\d+)/', loggins.Teacher_model_view.as_view(), name='tutor_update'),
        url('subject_updates_model/(?P<pk>\d+)/', loggins.Subject_model_view.as_view(), name='subject_updates_model'),
        url('ques_subject_updates/(?P<pk>\d+)/', loggins.manage_subject_updates, name='ques_subject_updates'),
        url('many_subject_updates/(?P<pk>\d+)/', result_views.many_student_updates, name='many_subject_updates'),
        url('subject_updates/(?P<pk>\d+)/', result_views.single_student_update, name='subject_updates'),
        url('position_updates/(?P<pk>\d+)/', result_views.subject_position_updates, name='position_updates'),
        url('edit_annual/(?P<pk>\d+)/', loggins.edit_annual.as_view(), name='edit_annual'),
        url('pro_detail/(?P<pk>\d+)/', loggins.profiles, name='pro_detail'),
        url('detail_grade/(?P<pk_code>[\w\-]+)/', loggins.group_by_grade, name='grade_list'),
        url('edith/(?P<pk>\d+)/', loggins.edit_user, name='edith'),
        url('admin_page/', loggins.admin_page, name='admin_page'),
        url('upload_photo/(?P<pk>\d+)/', loggins.new_profiles_pic, name='upload_photo'),
        url('one_subject_detail/(?P<pk>\d+)/', loggins.name_per_subject, name='one_subject_detail'),
        #url('scaders/', loggins.Subject_by_Cader_senior, name='scaders'), new
        url('list_tutor_subjects/(?P<pk>\d+)/', loggins.list_tutor_subjects, name='list_tutor_subjects'),
        url('student_names/', loggins.Student_names_list, name='student_names'),
        url('student_on_all_subjects_list/(?P<pk>\d+)/', loggins.student_on_all_subjects_list, name='student_on_all_subjects_list'),
        url('student_subject_list/(?P<pk>\d+)/', loggins.student_subject_list, name='student_subject_list'),
        url('passwords/', loggins.password, name='passwords'),
        url('renew_password/', sign_up.lost_password, name='renew_password'),
        url(r'^student_subject_detail_one_subject/(?P<pk>\d+)/', loggins.student_subject_detail_one_subject, name='student_subject_detail_one_subject'),
        url(r'^student_subject_detail_all_subject/(?P<pk>\d+)/', loggins.student_subject_detail_all_subject, name='student_subject_detail_all_subject'),
        url(r'^student_name_edit/(?P<pk>\d+)/', loggins.student_name_edit, name='student_name_edit'),
        url('delete_warning/(?P<pk>\d+)/', loggins.confirm_deletion, name='delete_warning'),
        url(r'^delete/(?P<pk>\d+)/', loggins.student_record_delete, name='delete'),
        url('warning_delete/(?P<pk>\d+)/', loggins.confirm_deletions, name='warning_delete'),
        url(r'^deletes/(?P<pk>\d+)/', loggins.delete_all, name='deletes'),
        url(r'^term_summary/(?P<pk>\d+)/', loggins.term_summary, name='term_summary'),
        
        url(r'^(?P<pk>\d+)/', loggins.detailView, name='subject_view'),
        url(r'^results_junior_senior/(?P<pk>\d+)/', loggins.results_junior_senior, name='results_junior_senior'),
        url(r'^annual/(?P<pk>\d+)/$', loggins.annual_view, name='annual_view'),
        url(r'^search_tutors', loggins.teacher_accounts, name='search_tutors'),
        url(r'^all_terms/(?P<pk>\d+)/$', loggins.three_term_records, name='all_terms'),
        url('user_example/', loggins.user_example, name='user_example'),
        url(r'^delete_anu/(?P<pk>\d+)/$', loggins.annual_record_delete, name='delete_anu'),
        url('warning_delete_anu/(?P<pk>\d+)/$', loggins.confirm_deletion_anu, name='warning_delete_anu'),
        url('signup/', sign_up.Staff_SignUp.as_view(), name='signup'),
        #url('ssignup/', sign_up.Student_signup, name='ssignup'),tutor_model_summary
        #url('new/(?P<pk>\d+)/$', sign_up.new, name='new'),
        url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        sign_up.activate, name='activate'), 
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        sign_up.reset, name='reset'),
        url('user/(?P<pk>\d+)/$', loggins.ProfileUpdate.as_view(), name='user_update'),
        url('', loggins.flexbox, name='flexing'),
               ]
