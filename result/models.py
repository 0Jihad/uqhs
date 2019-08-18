from django.db import models
from django.urls import reverse 
import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
################################################################################################'18/19'
class ASUBJECTS(models.Model):
    code = tuple([('English', 'English'), ('Mathematics', 'Mathematics'), ('Civic Education', 'Civic Education'), ('Electrical', 'Electrical'), ('Yoruba', 'Yoruba'), ('Agric. Sc.', 'Agric. Sc.'), ('Garment Making', 'Garment Making'), ('Pre-Vocation', 'Pre-Vocation'), ('Information Technology', 'Information Technology'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Geography', 'Geography'), ('Government', 'Government'), ('Account', 'Account'), ('Arabic', 'Arabic'), ('Islamic Studies', 'Islamic Studies'), ('Litrature', 'Litrature'), ('Commerce', 'Commerce'), ('Economics', 'Economics'), ('Business Studies', 'Business Studies'), ('Basic Science and Technology', 'Basic Science and Technology'), ('Catering', 'Catering'), ('National Value', 'National Value'), ('Furthe Mathematics', 'Furthe Mathematics'), ('History', 'History')] )
    name = models.CharField(max_length=30, choices= code, blank=True, null=True, default='English',)
    model_in = models.CharField(max_length=8, default='subject', blank=True, null=True)
    class Meta:
          ordering = ('name',)
    
    def __str__(self):
         return self.name

class SESSION(models.Model):
    code = tuple([('2019', '2018/2019'), ('2020', '2019/2020'), ('2021', '2020/2021'), ('2022', '2021/2022'), ('2023', '2022/2023'), ('2024', '2023/2024'), ('2025', '2024/2025'), ('2026', '2025/2026'), ('2027', '2026/2027'), ('2028', '2027/2028'), ('2029', '2028/2029'), ('2030', '2029/2030'), ('2031', '2030/2031'), ('2032', '2031/2032'), ('2033', '2032/2033'), ('2034', '2033/2034'), ('2035', '2034/2035'), ('2036', '2035/2036'), ('2037', '2036/2037'), ('2038', '2037/2038'), ('2039', '2038/2039'), ('2040', '2039/2040'), ('2041', '2040/2041'), ('2042', '2041/2042'), ('2043', '2042/2043'), ('2044', '2043/2044'), ('2045', '2044/2045'), ('2046', '2045/2046'), ('2047', '2046/2047'), ('2048', '2047/2048')])
    new = models.CharField(max_length=30, choices= code, blank=True, null=True, default='2019',)
    
    def __str__(self):
         return self.new
     
    class Meta:
        db_table = "school_session"
        verbose_name = "session"
        verbose_name_plural = "sessions"


class RESULT_GRADE(models.Model):
   identifier = models.IntegerField(null=True, blank=True, default='0')
   model_in = models.CharField(max_length=6, default='grades', blank=True, null=True)
   code = tuple([('English', 'English'), ('Mathematics', 'Mathematics'), ('Civic Education', 'Civic Education'), ('Electrical', 'Electrical'), ('Yoruba', 'Yoruba'), ('Agric. Sc.', 'Agric. Sc.'), ('Garment Making', 'Garment Making'), ('Pre-Vocation', 'Pre-Vocation'), ('Information Technology', 'Information Technology'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Geography', 'Geography'), ('Government', 'Government'), ('Account', 'Account'), ('Arabic', 'Arabic'), ('Islamic Studies', 'Islamic Studies'), ('Litrature', 'Litrature'), ('Commerce', 'Commerce'), ('Economics', 'Economics'), ('Business Studies', 'Business Studies'), ('Basic Science and Technology', 'Basic Science and Technology'), ('Catering', 'Catering'), ('National Value', 'National Value'), ('Furthe Mathematics', 'Furthe Mathematics'), ('History', 'History')] )
   subject = models.CharField(max_length=30, choices= code, blank=True, null=True, default='BroadSheet',)
   grade_A = models.IntegerField(null=True, blank=True, default='0')
   grade_C = models.IntegerField(null=True, blank=True, default='0')
   grade_P = models.IntegerField(null=True, blank=True, default='0')
   grade_F = models.IntegerField(null=True, blank=True, default='0')
   grade_A1 = models.IntegerField(null=True, blank=True, default='0')
   grade_B2 = models.IntegerField(null=True, blank=True, default='0')
   grade_B3 = models.IntegerField(null=True, blank=True, default='0')
   grade_C4 = models.IntegerField(null=True, blank=True, default='0')
   grade_C5 = models.IntegerField(null=True, blank=True, default='0')
   grade_C6 = models.IntegerField(null=True, blank=True, default='0')
   grade_D7 = models.IntegerField(null=True, blank=True, default='0')
   grade_E8 = models.IntegerField(null=True, blank=True, default='0')
   grade_F9 = models.IntegerField(null=True, blank=True, default='0')
   remark = models.BooleanField(default=False, help_text='True/False')
       
   def __str__(self):
         return self.subject+" : "+self.model_in
   class Meta:
          ordering = ('subject',)
          
   def get_absolute_url(self):
        """Returns the url to access a result_grade updates."""
        return reverse('result_grade_update', args=[str(self.id)])
    
     
class BTUTOR(models.Model):
    accounts = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, help_text='loggon-account:move account here', related_name='btutor')
    teacher_name = models.CharField(max_length=50, blank=True, null=True, help_text='Subject Teacher')###
    subject = models.ForeignKey(ASUBJECTS, on_delete=models.SET_NULL, null=True, blank=True, help_text='Select subject')
    class_status = (('JSS 1', 'jss_one'), ('JSS 2', 'jss_two'), ('JSS 3', 'jss_three'), ('SS 1', 'sss_one'), ('SS 2', 'sss_two'), ('SS 3', 'sss_three'))
    Class = models.CharField(max_length=30, choices=class_status, blank=True, null=True, help_text='Select subject class')
    term_status = (('1st Term', 'first term'), ('2nd Term', 'second term'), ('3rd Term', 'third term'))
    term = models.CharField(max_length=30, choices=term_status, blank=True, null=True, help_text='Select subject term')#, help_text='subject term',)
    graded = models.ForeignKey(RESULT_GRADE, on_delete=models.CASCADE, blank=True, null=True, help_text='Grade Counts')
    model_summary = models.CharField(max_length=1000, default='tutor', blank=True, null=True)
    model_in = models.CharField(max_length=8, default='qsubject', blank=True, null=True)
    males = models.IntegerField(null=True, blank=True, default='0', help_text='Enter number of male in class')
    females = models.IntegerField(null=True, blank=True, default='0', help_text='Enter number of female in class')
    cader = models.CharField(max_length=1, blank=True, null=True, help_text='Senior/Junior')
    session = models.CharField(max_length=5, blank=True, null=True, help_text='Must be 4 didits {2016}')###
    teacher_in = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='my_account', help_text= 'Class Teachers')
    class_teacher_id = models.CharField(max_length=200, blank=True, null=True, help_text='Class teacher id')
    created = models.DateTimeField(max_length=200, default=str(datetime.date.today()))
    updated = models.DateTimeField(editable=False, blank=True, null=True,)
    class Meta:
          ordering = ('id',) # helps in alphabetical listing. Sould be a tuple
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.accounts.username}:{self.Class}:{self.subject}:{self.term}'
    
    def save(self):
        if not self.id:
            self.created = datetime.date.today()
        self.teacher_name = f'{self.accounts.profile.title}{self.accounts.profile.last_name} : {self.accounts.profile.first_name}'
        self.updated = datetime.datetime.today()
        super(BTUTOR, self).save()
        
    def get_absolute_url(self):
        """Returns the url to access a result_grade updates."""
        return reverse('uniqueness', args=[str(self.id)])
   
    
    
    
class CNAME(models.Model):
    student_name = models.CharField(max_length=30, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(editable=False, blank=True, null=True,)
    subject_code = models.IntegerField(blank=True, null=True, default='0',)
    model_summary = models.CharField(max_length=200, default='student_names', blank=True, null=True)
    class_status = (('JSS 1', 'jss_one'), ('JSS 2', 'jss_two'), ('JSS 3', 'jss_three'), ('SS 1', 'sss_one'), ('SS 2', 'sss_two'), ('SS 3', 'sss_three'))
    Class = models.CharField(max_length=30, choices=class_status, blank=True, null=True)
    class Meta:
          ordering = ('student_name',) # helps in alphabetical listing. Sould be a tuple
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.student_name}'
    def save(self):
        if not self.id:
            self.created = datetime.date.today()
        self.updated = datetime.datetime.today()
        super(CNAME, self).save()
    def get_absolute_url(self):
        """Returns the url to access a detail record for this student."""
        return reverse('student_names')

   
class QSUBJECT(models.Model):#step5-subject 
     student_name = models.ForeignKey(CNAME, on_delete=models.SET_NULL, null=True)#
     test = models.FloatField(max_length=4, blank=True, null=True)
     agn = models.FloatField(max_length=4, blank=True, null=True)
     atd = models.FloatField(max_length=4, blank=True, null=True)
     total = models.FloatField(max_length=4, blank=True, null=True)
     exam = models.FloatField(max_length=4, blank=True, null=True)
     agr = models.FloatField(max_length=4, blank=True, null=True)
     grade = models.CharField(max_length=5, blank=True, null=True)
     posi = models.CharField(max_length=5, blank=True, null=True)
     gender = models.CharField(max_length=10, blank=True, null=True, help_text='sex',)#
     logged_in = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, help_text='subject_teacher', related_name='logins')
     created = models.DateTimeField(auto_now_add=True) 
     updated = models.DateTimeField(editable=False, blank=True, null=True,)
     tutor = models.ForeignKey(BTUTOR, on_delete=models.CASCADE, blank=True, null=True)
     cader_options = (('s', 'Senior'), ('j', 'Junior'))
     cader = models.CharField(max_length=1, choices=cader_options, blank=True, null=True)
     model_in = models.CharField(max_length=8, default='qsubject', blank=True, null=True)
     annual_scores = models.CharField(max_length=100, blank=True, null=True)
     ###Just for searching
     class_status = (('JSS 1', 'jss_one'), ('JSS 2', 'jss_two'), ('JSS 3', 'jss_three'), ('SS 1', 'sss_one'), ('SS 2', 'sss_two'), ('SS 3', 'sss_three'))
     Class = models.CharField(max_length=30, choices=class_status, blank=True, null=True)
     #qteacher = user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, help_text='select class teache', related_name='qsubject')
     class Meta:
          ordering = ('student_name_id',) # helps in alphabetical listing. Sould be a tuple
     def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}:{self.student_name}:{str(self.tutor.subject)[:3]}:{self.tutor.Class}:{self.tutor.term}'
     def get_absolute_url(self):
        """Returns the url to access a detail record for this student."""
        return reverse('subject_updates', args=[str(self.id)])
     def save(self):
        if not self.id:
            self.created = datetime.date.today()
        self.updated = datetime.datetime.today()
        super(QSUBJECT, self).save()
        

################################################################################################         
class ANNUAL(models.Model):
    student_name = models.ForeignKey(CNAME, on_delete=models.SET_NULL, null=True)#
    first = models.ForeignKey(QSUBJECT, on_delete=models.SET_NULL, null=True, related_name = 'annual_first')
    second = models.ForeignKey(QSUBJECT, on_delete=models.SET_NULL, null=True, related_name = 'annual_second')
    third = models.ForeignKey(QSUBJECT, on_delete=models.SET_NULL, null=True, related_name = 'annual_third')
    summary = models.CharField(max_length=40, blank=True, null=True)
    anual = models.FloatField(max_length=10, blank=True, null=True)#
    Agr = models.FloatField(max_length=10, blank=True, null=True)
    Grade = models.CharField(max_length=5, blank=True, null=True)
    Posi = models.CharField(max_length=5, blank=True, null=True)
    subject_by = models.ForeignKey(BTUTOR, on_delete=models.CASCADE, blank=True, null=True, help_text='subject_teacher')
    subject =  models.ForeignKey(ASUBJECTS, on_delete=models.SET_NULL, null=True)
    
    
    class Meta:
          ordering = ('student_name_id',) # helps in alphabetical listing. Sould be a tuple
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}:{self.student_name.student_name}'
    def get_absolute_url(self):
        """Returns the url to access a detail record for this student."""
        return reverse('annualmodel-detail', args=[str(self.id)])
    #def save(self):
    #    self.summary = str(self.first.agr)+','+str(self.second.agr)+','+str(self.third.agr)
     #   super(ANNUAL, self).save()



class OVERALL_ANNUAL(models.Model):
    student_name = models.ForeignKey(CNAME, on_delete=models.SET_NULL, null=True)
    class_status = (('JSS 1', 'jss_one'), ('JSS 2', 'jss_two'), ('JSS 3', 'jss_three'), ('SS 1', 'sss_one'), ('SS 2', 'sss_two'), ('SS 3', 'sss_three'))
    class_in = models.CharField(max_length=30, choices=class_status, blank=True, null=True)
    eng = models.ForeignKey(ANNUAL, on_delete=models.SET_NULL, null=True, blank=True, related_name='eng')
    mat = models.ForeignKey(ANNUAL, on_delete=models.SET_NULL, null=True, blank=True, related_name='mat')
    agr = models.ForeignKey(ANNUAL, on_delete=models.SET_NULL, null=True, blank=True, related_name='agr')
    bus =  models.ForeignKey(ANNUAL, on_delete=models.SET_NULL, null=True, blank=True, related_name='bus')
    bst = models.ForeignKey(ANNUAL, on_delete=models.SET_NULL, null=True, blank=True, related_name='bst')
    yor = models.ForeignKey(ANNUAL, on_delete=models.SET_NULL, null=True, blank=True, related_name='yor')
    nva = models.ForeignKey(ANNUAL, on_delete=models.SET_NULL, null=True, blank=True, related_name='nva')
    irs = models.ForeignKey(ANNUAL, on_delete=models.SET_NULL, null=True, blank=True, related_name='irs')
    prv =  models.ForeignKey(ANNUAL, on_delete=models.SET_NULL, null=True, blank=True, related_name='prv')
    ict = models.ForeignKey(ANNUAL, on_delete=models.SET_NULL, null=True, blank=True, related_name='arb')
    acc = models.ForeignKey(ANNUAL, on_delete=models.SET_NULL, null=True, blank=True, related_name='acc')
    his = models.ForeignKey(ANNUAL, on_delete=models.SET_NULL, null=True, blank=True, related_name='his')
    AGR = models.FloatField(max_length=8, blank=True, null=True, default='0')
    AVR = models.FloatField(max_length=8, blank=True, null=True, default='0')
    GRD = models.CharField(max_length=8, null=True, blank=True, default='0')
    POS = models.CharField(max_length=8, null=True, blank=True, default='0')
    teacher_in = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='all_subject')
    session = models.CharField(max_length=5, blank=True, null=True, help_text='Must be 4 didits {2016}')
    
    class Meta:
          ordering = ('class_in',) # helps in alphabetical listing. Sould be a tuple
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}:{self.student_name.student_name}:{self.class_in}:{self.teacher_in.username}'

class Edit_User(models.Model):
   def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit*459*571:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
   user = models.OneToOneField(User, on_delete=models.CASCADE,  blank=True, null=True, related_name='profile')
   status = (('Mr.', 'Mr'), ('Mrs.', 'Mrs'), ('Sir.', 'Senior officer'), ('Ma.', 'Madam'), ('Mall.', 'Mallam'), ('Ust.', 'Ustadh'), ('Alh.', 'Alhaj'), ('Dr.', 'Doctor'), ('Engr.', 'Engineer'))
   title = models.CharField(max_length=15, choices=status, null=True, help_text='Select title to address you.', default= 'Mr.')
   last_name = models.CharField(max_length=20, null=True, help_text='(Surname)-Required')
   first_name = models.CharField(max_length=20, null=True, help_text='(Other names)-Required')
   photo = models.ImageField(upload_to='static/result/images/', validators=[validate_image], null=True)
   image = models.CharField(max_length=30, null=True, blank=True,)
   bio = models.TextField(blank=True, help_text='Your summarised biography',  default= 'I am a professional science teacher, currently working with the aboved named School. If you plan on changing the font face and its color only once on a web page, you need to change its attributes in the element tag. Using the style attribute, you may specify the font face and color with font-family, color, and the font size with font-size, as shown in the example below.')
   phone = models.CharField(max_length=20, blank=True, help_text='Hotline')
   city = models.CharField(max_length=15, blank=True, help_text='Your town in the state of origin', default= 'Ibadan')
   country = models.CharField(max_length=10, blank=True, default= 'Nigeria', help_text='Nationality')
   organization = models.CharField(max_length=10, blank=True, help_text='Oganization affliated with', default= 'IIRO')
   location = models.CharField(max_length=30, blank=True, help_text='Current location')
   birth_date = models.DateField(null=True, blank=True, help_text='Date format: MM/DD/YYYY')
   section_status = (('Sc', 'Sciences'), ('SSc', 'Social Sciences'), ('Art', 'Arts and Humanities'))
   department = models.CharField(max_length=30, choices=section_status, blank=True, null=True)
   account_id = models.CharField(max_length=30, default = 0, blank=True, null=True)
   email_confirmed = models.BooleanField(default=False, help_text='True/False')
   class_status = (('JSS 1', 'jss_one'), ('JSS 2', 'jss_two'), ('JSS 3', 'jss_three'), ('SS 1', 'sss_one'), ('SS 2', 'sss_two'), ('SS 3', 'sss_three'))
   class_in = models.CharField(max_length=15, choices=class_status, blank=True, null=True, help_text='Select class in charge', default= None)
       
   def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}:{self.user.username}'
   class Meta:
          ordering = ('account_id',)
   
   def save(self, *args, **kwargs):
        self.image = 'result/images/'+str(self.user.username)+'.jpg'
        self.photo.name = self.user.username + '.jpg'
        self.user.last_name = self.last_name
        self.user.first_name = self.first_name
        if self.user.email != None and self.user.last_name != None or self.user.first_name != None:
            self.email_confirmed = True
        super(Edit_User, self).save(*args, **kwargs)

   def get_absolute_url(self):
        return reverse('pro_detail', args=[str(self.user.id)])
    
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Edit_User.objects.create(user=instance)
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Edit_User.objects.create(user=instance)
    instance.profile.save()

class Post(models.Model):
    Account_Username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(max_length=1000)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
 
    def __str__(self):
        return self.title

   
       