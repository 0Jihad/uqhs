from django.conf.urls import url
#, include student_name_edit, subject_per_name annual_agr detailView annual_agr subject_total annual_view annual_sheet edit_user
from.import views, loggins#, imports, posts, sign_up, explorer, creates, exports, utils, deletions, updates#, pdfs
urlpatterns = [
            #####EXPORTS #######IMPORTS#####      past_csvs                
            url('home_page/(?P<pk>\d+)/$', views.home_page, name='home_page'),
            url(r'home/$', views.home, name='home'),
            url(r'home_page_return/(?P<pk>\d+)/$', views.home_page_return, name='home_page_return'),
            
               
            url('', loggins.flexbox, name='flexing'),
                    
				]