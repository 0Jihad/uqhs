# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 01:15:37 2019

@author: AdeolaOlalekan
"""
#from django.contrib.auth import views as auth_views detailView show_annual
from django.conf.urls import url
#, include student_name_edit, subject_per_name annual_agr detailView annual_agr subject_total annual_view annual_sheet
from.import result_views, model_loader, loggins, sign_up
urlpatterns = [
        url(r'home/$', loggins.home, name='home'),
        url(r'^generate/', loggins.Pdf.as_view(), name='pdf'), 
        url(r'^export_broadsheet/', loggins.export_broadsheet, name='export_broadsheet'),
        url(r'^upload_txt/(?P<pk>\d+)/', model_loader.upload_new_subject_scores, name='upload_txt'),
        url(r'^extract_name/subjects/(?P<pk>\d+)/', loggins.export_name_text, name='extract_name'),
        url(r'^export_all/subjects/(?P<pk>\d+)/', loggins.export_all, name='export_all'),
        url(r'^export/scores/subjects/(?P<pk>\d+)/', loggins.export_subject_scores, name='export_users_scores'),
        url('class_record_view', model_loader.broad_sheet, name='class_record_view'),
        url('broad_sheet_on_page', model_loader.broad_sheet_on_page, name='broad_sheet_on_page'),
        url('samples_down/', loggins.sample_down, name='samples_down'),
        url('samples_disp/', loggins.sample_disply, name='samples_disp'),
        url(r'logins/', loggins.loggin, name='logins'),
        url('log_out/', loggins.logout, name='log_out'),
        url('all_accounts/', loggins.all_users, name='all_accounts'),
        url('all_teachers/', loggins.all_teachers, name='all_teachers'),#annual_sheet
        url('confirm_deleting_a_user/(?P<pk>\d+)/', loggins.confirm_deleting_a_user, name='confirm_deleting_a_user'),
        url('delete_a_user/(?P<pk>\d+)/', loggins.delete_user, name='delete_a_user'),
        url('edit_accounts/(?P<pk>\d+)/', loggins.Users_update.as_view(), name='edit_accounts'),
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
        url('annual_sheet/(?P<pk>\d+)/', loggins.annual_view, name='annual_sheet'),
        url('position_updates/(?P<pk>\d+)/', result_views.subject_position_updates, name='position_updates'),
        
        url('pro_detail/(?P<pk>\d+)/', loggins.profiles, name='pro_detail'),
        url('detail_grade/(?P<pk_code>[\w\-]+)/', loggins.qsubject_on_grade, name='grade_list'),
        url('detail_annual_on_grade/(?P<pk_code>[\w\-]+)/', loggins.annual_on_grade, name='A_on_grade'),
        url('detail_broadsheet_on_grade/(?P<pk_code>[\w\-]+)/', loggins.broadsheet_on_grade, name='B_on_grade'),
        url('edith/(?P<pk>\d+)/', loggins.edit_user, name='edith'),
        url('admin_page/', loggins.admin_page, name='admin_page'),
        url('upload_photo/(?P<pk>\d+)/', loggins.new_profiles_pic, name='upload_photo'),
        url('one_subject_detail/(?P<pk>\d+)/', loggins.name_per_subject, name='one_subject_detail'),
        url('tutor_subjects_all_list/(?P<pk>\d+)/', loggins.all_list_tutor_subjects, name='tutor_subjects_all_list'),
        url('list_tutor_subjects/(?P<pk>\d+)/', loggins.list_tutor_subjects, name='list_tutor_subjects'),
        url('student_names/', loggins.Student_names_list, name='student_names'),
        url('student_on_all_subjects_list/(?P<pk>\d+)/', loggins.student_on_all_subjects_list, name='student_on_all_subjects_list'),
        url('all_student_subject_list/(?P<pk>\d+)/', loggins.all_student_subject_list, name='all_student_subject_list'),
        url('student_subject_list/(?P<pk>\d+)/', loggins.student_subject_list, name='student_subject_list'),
        url('passwords/(?P<pk>\d+)/', loggins.password1, name='passwords'),
        url('password/', loggins.password2, name='password'),
           
        url('my_post/post_list', loggins.my_post, name='my_post_list'),
        url('post/post_list', loggins.post_list, name='post_list'),
        url('post/(?P<pk>\d+)/', loggins.post_detail, name='post_detail'),
        url('post/new/', loggins.post_new, name='post_new'),
        url('post_edit/(?P<pk>\d+)/', loggins.post_edit.as_view(), name='post_edit'),
        url('drafts/', loggins.post_draft_list, name='post_draft_list'),#post approvals student_in_none 
        #url('post/publish/', loggins.post_publish, name='post_publish'),#review post uncomment for no review compute_annual
        url('post_remove/(?P<pk>\d+)/', loggins.delete_post, name='post_remove'),
        url('posts_publishing/(?P<pk>\d+)/publish/', loggins.posts_publishing, name='posts_publishing'),
        url(r'^student_subject_detail_one_subject/(?P<pk>\d+)/', loggins.student_subject_detail_one_subject, name='student_subject_detail_one_subject'),
        url(r'^student_subject_detail_all_subject/(?P<pk>\d+)/', loggins.student_subject_detail_all_subject, name='student_subject_detail_all_subject'),
        url(r'^student_name_edit/(?P<pk>\d+)/', loggins.student_name_edit, name='student_name_edit'),
        url('delete_warning/(?P<pk>\d+)/', loggins.confirm_deletion, name='delete_warning'),
        url(r'^delete_a_student/(?P<pk>\d+)/', loggins.confirmed_delete, name='delete'),
        url('yes_no/(?P<pk>\d+)/', loggins.yes_no, name='yes_no'),
        url('warning_delete/(?P<pk>\d+)/', loggins.confirm_deletions, name='warning_delete'),
        url(r'^deletes/(?P<pk>\d+)/', loggins.delete_all, name='deletes'),
        url(r'^term_summary/(?P<pk>\d+)/', loggins.term_summary, name='term_summary'),
        url(r'^(?P<pk>\d+)/', loggins.detailView, name='subject_view'),
        url(r'^_all/(?P<pk>\d+)/', loggins.detail_all, name='subject_view_all'),
        url(r'^results_junior_senior/(?P<pk>\d+)/', loggins.results_junior_senior, name='results_junior_senior'),
           #all_accounts
        url(r'^create_update_annual_records/(?P<pk>\d+)/$', model_loader.compute_annual, name='compute_annual'),
        url(r'^create_update_show_annual/(?P<pk>\d+)/$', model_loader.show_annual, name='show_annual'),
        url(r'^all_annual_view/(?P<pk>\d+)/$', loggins.all_annual_view, name='all_annual_view'),
        url(r'^annual/(?P<pk>\d+)/$', loggins.annual_view, name='annual_view'),
        url('broad_sheet_views/(?P<pk>\d+)/', model_loader.broad_sheet_views, name='broad_sheet_views'), 
        
        url(r'^search_tutors', loggins.teacher_accounts, name='search_tutors'),
        url(r'^all_terms/(?P<pk>\d+)/$', loggins.three_term_records, name='all_terms'),
        url('a_student_exist/(?P<pk>\d+)/$', model_loader.a_student_exist, name='a_student_exist'),
        url('new_student_name/', model_loader.new_student_name, name='new_student_name'),
        #
        #url('warning_delete_anu/(?P<pk>\d+)/$', loggins.confirm_deletion_anu, name='warning_delete_anu'),
        url('signup/', sign_up.Staff_SignUp.as_view(), name='signup'),
        url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        sign_up.activate, name='activate'), 
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        sign_up.reset, name='reset'),
        url('user/(?P<pk>\d+)/$', loggins.ProfileUpdate.as_view(), name='user_update'),
        url('', loggins.flexbox, name='flexing'),
               ]
