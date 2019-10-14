from django.conf.urls import url
#, include student_name_edit, subject_per_name annual_agr detailView annual_agr subject_total annual_view annual_sheet edit_user
from.import views#, imports, loggins, posts, sign_up, explorer, creates, exports, utils, deletions, updates#, pdfs
urlpatterns = [
            #####EXPORTS #######IMPORTS#####          past_csvs           
            url('home_page/(?P<pk>\d+)/$', views.home_page, name='home_page'),
            url(r'home/$', views.home, name='home'),
            url(r'home_page_return/(?P<pk>\d+)/$', views.home_page_return, name='home_page_return'),
                     			 #####VIEWS##### annual_view student_subject_list student_in_none 
            url(r'searchs', views.searchs, name='searchs'),
            url(r'uniqueness/(?P<pk>\d+)/', views.uniqueness, name='uniqueness'),
            url('subject_home/(?P<pk>\d+)/(?P<cl>\d+)/', views.subject_home, name='subject_home'),
            #  
             
            #url('student_name_class_filter/', views.student_name_class_filter, name='student_name_class_filter'), 
            url(r'^(?P<pk>\d+)/(?P<md>\d+)/', views.detailView, name='subject_view'),######################
            url(r'^_all/(?P<pk>\d+)/(?P<md>\d+)/', views.all_View, name='subject_view_all'),####################
            url('student_in_none/', views.student_in_None, name='student_in_none'),       
            url('detail_grade/(?P<pk_code>[\w\-]+)/', views.qsubject_on_grade, name='grade_list'),
            url('detail_annual_on_grade/(?P<pk_code>[\w\-]+)/', views.annual_on_grade, name='A_on_grade'),
            #url('detail_broadsheet_on_grade/(?P<pk_code>[\w\-]+)/', views.broadsheet_on_grade, name='B_on_grade'),
            url('student_names/(?P<pk>\d+)/', views.Student_names_list, name='student_names'),
            url('student_on_all_subjects_list/(?P<pk>\d+)/', views.student_on_all_subjects_list, name='student_on_all_subjects_list'),
            url('all_student_subject_list/(?P<pk>\d+)/', views.all_student_subject_list, name='all_student_subject_list'),
            url('student_subject_list/(?P<pk>\d+)/', views.student_subject_list, name='student_subject_list'),
            url('all_teachers/', views.all_teachers, name='all_teachers'),#annual_sheet
            url(r'^subject/transfers', views.teacher_accounts, name='transfers'),
            url(r'^results_junior_senior/(?P<pk>\d+)/', views.results_junior_senior, name='results_junior_senior'),
            url(r'^once_results_junior_senior/(?P<pk>\d+)/', views.once_results_junior_senior, name='once_results_junior_senior'),
            url(r'^student_subject_detail_one_subject/(?P<pk>\d+)/', views.student_subject_detail_one_subject, name='student_subject_detail_one_subject'),
            url(r'^student_subject_detail_all_subject/(?P<pk>\d+)/', views.student_subject_detail_all_subject, name='student_subject_detail_all_subject'),
            url(r'^genders_scores/(?P<pk_code>[\w\-]+)/', views.genders_scores, name='males_scores'),
            url('search_results/(?P<pk>\d+)/', views.search_results, name='search_results'),
            #url(r'annual_view_females/(?P<pk>\d+)/', views.annual_view_females, name='annual_view_females'),
            url(r'annual_view_genders/(?P<pk_code>[\w\-]+)/', views.annual_view_genders, name='annual_view_males'),
            url(r'^broad_sheet_viees/(?P<pk>\d+)/', views.broad_sheet_views, name='broad_sheet_views'),
            #url(r'^create_update_show_annual/(?P<pk>\d+)/$', views.show_annual, name='show_annual'),    broadsheet_on_grade teacher_create
            			 #####CREATES##### 
            
               
            #url('', loggins.flexbox, name='flexing'),
                    
				]