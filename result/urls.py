from django.conf.urls import url
#, include student_name_edit, subject_per_name annual_agr detailView annual_agr subject_total annual_view annual_sheet edit_user
from.import views, imports, loggins, posts, sign_up, explorer, creates, exports, utils, deletions, updates
urlpatterns = [
            #####EXPORTS #######IMPORTS##### pro_detail updates
            url(r'home/$', views.home, name='home'),
            url('samples_down/', exports.sample_down, name='samples_down'),
            url('samples_disp/', exports.sample_disply, name='samples_disp'),
            url(r'^generate/pdf', exports.broadsheet_in_pdf.as_view(), name='broadsheets'),
            url(r'^generate/', exports.terms_in_pdf.as_view(), name='pdf'), 
            url(r'^export_broadsheet/', exports.export_broadsheet, name='export_broadsheet'),
            url(r'^upload_txt/(?P<pk>\d+)/', imports.upload_new_subject_scores, name='upload_txt'),
            url('a_student_exist/(?P<pk>\d+)/$', imports.upload_a_student_subject, name='a_student_exist'),
            url('new_student_name/(?P<pk>\d+)/$', imports.upload_a_name, name='new_student_name'),
            url(r'^extract_name/subjects/(?P<pk>\d+)/', exports.export_name_text, name='extract_name'),
            url(r'^export_all/subjects/(?P<pk>\d+)/', exports.export_third_scores, name='export_all'),
            url(r'^export/scores/subjects/(?P<pk>\d+)/', exports.export_subject_scores, name='export_users_scores'),
             #####EXPLORER BSHEET############ 
            	####UTILS#####AND SIGNUP
            url('signup/', sign_up.Staff_SignUp.as_view(), name='signup'),
            url('tutor_summary/utils/(?P<pk>\d+)/', utils.tutor_model_summary, name='tutor_summary'),
            url('tutor_summary/(?P<pk>\d+)/', utils.tutor_model_summary, name='tutor_summary'),
         			 #####VIEWS##### annual_view
            url(r'searchs', views.searchs, name='searchs'),
            url(r'uniqueness/(?P<pk>\d+)/', views.uniqueness, name='uniqueness'),
            url(r'all_search_lists/(?P<pk>\d+)/', views.all_search_lists, name='all_search_lists'),
            url('subject_home/(?P<pk_code>[\w\-]+)/', views.subject_home, name='subject_home'),
            url('student_in_none/', views.student_in_None, name='student_in_none'),  
            url('subject_class_term_filter/', views.subject_class_term_filter, name='subject_class_term_filter'), 
            url('student_name_class_filter/', views.student_name_class_filter, name='student_name_class_filter'), 
            url(r'^(?P<pk>\d+)/', views.detailView, name='subject_view'),
            url(r'^_all/(?P<pk>\d+)/', views.detail_all, name='subject_view_all'),
            url('student_in_none/', views.student_in_None, name='student_in_none'),       
            url('annual_sheet/(?P<pk>\d+)/', views.annual_view, name='annual_view'),
            url(r'^all_annual_view/(?P<pk>\d+)/$', views.all_annual_view, name='all_annual_view'),
            url('detail_grade/(?P<pk_code>[\w\-]+)/', views.qsubject_on_grade, name='grade_list'),
            url('detail_annual_on_grade/(?P<pk_code>[\w\-]+)/', views.annual_on_grade, name='A_on_grade'),
            url('detail_broadsheet_on_grade/(?P<pk_code>[\w\-]+)/', views.broadsheet_on_grade, name='B_on_grade'),
            url('student_names/', views.Student_names_list, name='student_names'),
            url('student_on_all_subjects_list/(?P<pk>\d+)/', views.student_on_all_subjects_list, name='student_on_all_subjects_list'),
            url('all_student_subject_list/(?P<pk>\d+)/', views.all_student_subject_list, name='all_student_subject_list'),
            url('student_subject_list/(?P<pk>\d+)/', views.student_subject_list, name='student_subject_list'),
            url('all_teachers/', views.all_teachers, name='all_teachers'),#annual_sheet
            url(r'^search_tutors', views.teacher_accounts, name='search_tutors'),
            url(r'^results_junior_senior/(?P<pk>\d+)/', views.results_junior_senior, name='results_junior_senior'),
            url(r'^student_subject_detail_one_subject/(?P<pk>\d+)/', views.student_subject_detail_one_subject, name='student_subject_detail_one_subject'),
            url(r'^student_subject_detail_all_subject/(?P<pk>\d+)/', views.student_subject_detail_all_subject, name='student_subject_detail_all_subject'),
            #url(r'^all_accounts_on_page/(?P<pk>\d+)/', views. all_accounts_on_page, name='all_accounts_on_page'),
            url(r'^broad_sheet_viees/(?P<pk>\d+)/', views.broad_sheet_views, name='broad_sheet_views'),
            url(r'^create_update_show_annual/(?P<pk>\d+)/$', views.show_annual, name='show_annual'),     
            			 #####CREATES#####
            url(r'create_subjects/', creates.create_subjects, name='create_subject'),
            url(r'created_subjects/(?P<pk>\d+)/', creates.created_subjects, name='created_subject_list'),
            url(r'create_new_teacher/', creates.create_new_subject_teacher, name='teacher_create'),
            #####LOGGINS#####
            url(r'logins/', loggins.loggin, name='logins'),
            url('log_out/', loggins.logout, name='log_out'),
            url('admin_page/', loggins.admin_page, name='admin_page'),
            url('passwords/(?P<pk>\d+)/', loggins.password1, name='passwords'),
            url('password/', loggins.password2, name='password'),
            url('InputTypeError/', loggins.InputTypeError, name='InputTypeError'),
            url('all_accounts/', loggins.all_users, name='all_accounts'),
            
            url(r'^create_update_annual_records/ explorer/ (?P<pk>\d+)/$', explorer.explor_annual, name='compute_annual'),
            url('class_record_view/ explorer/ ', explorer.broad_sheet, name='class_record_view'),
            url('pre_broad_sheet/ explorer/ ', explorer.pre_broad_sheet, name='pre_broad_sheet'), 
              #####POSTS%###### 
            url('my_post/post_list', posts.my_post, name='my_post_list'),
            url('post/post_list', posts.post_list, name='post_list'),
            url('post/(?P<pk>\d+)/', posts.post_detail, name='post_detail'),
            url('post/new/', posts.post_new, name='post_new'),
            url('post_edit/(?P<pk>\d+)/', posts.post_edit.as_view(), name='post_edit'),
            url('drafts/', posts.post_draft_list, name='post_draft_list'),#post approvals student_in_none new_student_name
            #url('post_remove/(?P<pk>\d+)/', posts.delete_post, name='post_remove'),
            url('posts_publishing/(?P<pk>\d+)/publish/', posts.posts_publishing, name='posts_publishing'),
              ####DELETE%###### 
            url('delete_warning/ deletions/ (?P<pk>\d+)/', deletions.confirm_deletion, name='delete_warning'),
            url(r'^delete_a_student/ deletions/ (?P<pk>\d+)/', deletions.confirmed_delete, name='delete'),
            url('yes_no/ deletions/ (?P<pk>\d+)/', deletions.yes_no, name='yes_no'),
            url('warning_delete/ deletions/ (?P<pk>\d+)/', deletions.confirm_deletions, name='warning_delete'),
            url(r'^deletes/ deletions/ (?P<pk>\d+)/', deletions.delete_all, name='deletes'), 
            url('confirm_deleting_a_user/ deletions/ (?P<pk>\d+)/', deletions.confirm_deleting_a_user, name='confirm_deleting_a_user'),
            url('delete_a_user/ deletions/ (?P<pk>\d+)/', deletions.delete_user, name='delete_a_user'),
            url('post_remove/ deletions/ (?P<pk>\d+)/', deletions.delete_post, name='post_remove'),
            			 #####UPDATES%######
            url('edit_accounts/ updates/ (?P<pk>\d+)/', updates.Users_update.as_view(), name='edit_accounts'),
            url('tutor/updates/(?P<pk>\d+)/', updates.Teacher_model_view.as_view(), name='tutor_update'),
            url('subject_updates_model/ updates/ (?P<pk>\d+)/', updates.Subject_model_view.as_view(), name='subject_updates_model'),
            url('ques_subject_updates/ updates/ (?P<pk>\d+)/', updates.manage_subject_updates, name='ques_subject_updates'),
            url('many_subject_updates/ updates/ (?P<pk>\d+)/', updates.many_student_updates, name='many_subject_updates'),
            url('subject_updates/ updates/ (?P<pk>\d+)/', updates.single_student_update, name='subject_updates'),
            
            url('pro_detail/updates/(?P<pk>\d+)/', updates.profiles, name='pro_detail'),####
            url('user/updates/(?P<pk>\d+)/$', updates.ProfileUpdate.as_view(), name='user_update'),#####
            url('upload_photo/ updates/ (?P<pk>\d+)/', updates.profile_picture, name='upload_photo'),#####
            url(r'^Cname_edit/updates/(?P<pk>\d+)/$', updates.Cname_edit.as_view(), name='Cname_edit'),####
            url('position_updates/updates/(?P<pk>\d+)/', updates.subject_position_updates, name='position_updates'),
            
               
            url('', loggins.flexbox, name='flexing'),
                    
				]