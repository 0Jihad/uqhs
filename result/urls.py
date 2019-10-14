from django.conf.urls import url
#, include student_name_edit, subject_per_name annual_agr detailView annual_agr subject_total annual_view annual_sheet edit_user
from.import loggins, #views, imports, posts, sign_up, explorer, creates, exports, utils, deletions, updates#, pdfs
urlpatterns = [
            
            #####LOGGINS#####(?P<studentclass>\w+)/(?P<doctype>[\w-]+)/$
            url(r'logins/', loggins.loggin, name='logins'),
            url('log_out/', loggins.logout, name='log_out'),
            url('admin_page/', loggins.admin_page, name='admin_page'),
            url('passwords/(?P<pk>\d+)/', loggins.password1, name='passwords'),
            url('password/', loggins.password2, name='password'),
            url('InputTypeError/', loggins.InputTypeError, name='InputTypeError'),
            url('all_accounts/', loggins.all_users, name='all_accounts'),
            
            
               
            url('', loggins.flexbox, name='flexing'),
                    
				]