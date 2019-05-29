from django.db import models
from django.urls import reverse 
import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
################################################################################################

class ASUBJECTS(models.Model):
    code = tuple([('English', 'English'), ('Mathematics', 'Mathematics'), ('Civic Education', 'Civic Education'), ('Electrical', 'Electrical'), ('Yoruba', 'Yoruba'), ('Agric. Sc.', 'Agric. Sc.'), ('Garment Making', 'Garment Making'), ('Pre-Vocation', 'Pre-Vocation'), ('Information Technology', 'Information Technology'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Geography', 'Geography'), ('Government', 'Government'), ('Account', 'Account'), ('Arabic', 'Arabic'), ('Islamic Studies', 'Islamic Studies'), ('Litrature', 'Litrature'), ('Commerce', 'Commerce'), ('Economics', 'Economics'), ('Business Studies', 'Business Studies'), ('Basic Science and Technology', 'Basic Science and Technology'), ('Catering', 'Catering'), ('National Value', 'National Value'), ('Furthe Mathematics', 'Furthe Mathematics'), ('others', 'others')] )
    name = models.CharField(max_length=30, choices= code, blank=True, null=True, default='English',)
    model_in = models.CharField(max_length=8, default='subject', blank=True, null=True)
    class Meta:
          ordering = ('name',)
    
    def __str__(self):
         return self.name

class RESULT_GRADE(models.Model):
   identifier = models.IntegerField(null=True, blank=True, default='0')
   model_in = models.CharField(max_length=6, default='grades', blank=True, null=True)
   code = tuple([('English', 'English'), ('Mathematics', 'Mathematics'), ('Civic Education', 'Civic Education'), ('Electrical', 'Electrical'), ('Yoruba', 'Yoruba'), ('Agric. Sc.', 'Agric. Sc.'), ('Garment Making', 'Garment Making'), ('Pre-Vocation', 'Pre-Vocation'), ('Information Technology', 'Information Technology'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Geography', 'Geography'), ('Government', 'Government'), ('Account', 'Account'), ('Arabic', 'Arabic'), ('Islamic Studies', 'Islamic Studies'), ('Litrature', 'Litrature'), ('Commerce', 'Commerce'), ('Economics', 'Economics'), ('Business Studies', 'Business Studies'), ('Basic Science and Technology', 'Basic Science and Technology'), ('Catering', 'Catering'), ('National Value', 'National Value'), ('Furthe Mathematics', 'Furthe Mathematics'), ('others', 'others')] )
   subject = models.CharField(max_length=30, choices= code, blank=True, null=True, default='English',)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, help_text='loggon-account:move account here')
    teacher_name = models.CharField(max_length=30, blank=True, null=True)#, help_text='subject_teacher')
    subject = models.ForeignKey(ASUBJECTS, on_delete=models.SET_NULL, null=True, blank=True)
    class_status = (('JSS 1', 'jss_one'), ('JSS 2', 'jss_two'), ('JSS 3', 'jss_three'), ('SS 1', 'sss_one'), ('SS 2', 'sss_two'), ('SS 3', 'sss_three'))
    Class = models.CharField(max_length=30, choices=class_status, blank=True, null=True)
    term_status = (('1st Term', 'first term'), ('2nd Term', 'second term'), ('3rd Term', 'third term'))
    term = models.CharField(max_length=30, choices=term_status, blank=True, null=True)#, help_text='subject term',)
    graded = models.ForeignKey(RESULT_GRADE, on_delete=models.CASCADE, blank=True, null=True, help_text='Grade Counts')
    model_summary = models.CharField(max_length=1000, default='tutor', blank=True, null=True)
    model_in = models.CharField(max_length=8, default='qsubject', blank=True, null=True)
    males = models.IntegerField(null=True, blank=True, default='0')
    females = models.IntegerField(null=True, blank=True, default='0')
    cader = models.CharField(max_length=1, blank=True, null=True)
    session = models.CharField(max_length=8, default='18/19', blank=True, null=True)
    class Meta:
          ordering = ('id',) # helps in alphabetical listing. Sould be a tuple
    #def __str__(self):
         #return self.model_in+" : "+self.user#+" : "+self.subject_class+" : "+self.subject_term
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.Class}:{self.subject}:{self.term}'
    
class CNAME(models.Model):
    student_name = models.CharField(max_length=30, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(editable=False, blank=True, null=True,)
    subject_code = models.IntegerField(blank=True, null=True, default='0',)
    model_summary = models.CharField(max_length=200, default='student_names', blank=True, null=True)
    Class = models.CharField(max_length=200, default='None', blank=True, null=True)
    class Meta:
          ordering = ('student_name',) # helps in alphabetical listing. Sould be a tuple
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}:{self.student_name}'
    def save(self):
        if not self.id:
            self.created = datetime.date.today()
        self.updated = datetime.datetime.today()
        super(CNAME, self).save()

   
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
     logged_in = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, help_text='subject_teacher')
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
        
class QUEST_MODEL(models.Model):#step5-subject 
     #user_account = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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
     logged_in = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, help_text='subject_teacher')
     created = models.DateTimeField(auto_now_add=True) 
     updated = models.DateTimeField(editable=False, blank=True, null=True,)
     tutor = models.ForeignKey(BTUTOR, on_delete=models.CASCADE, blank=True, null=True, help_text='terms')
     cader = models.CharField(max_length=1, blank=True, null=True)
     model_in = models.CharField(max_length=8, default='qsubject', blank=True, null=True)
     def save(self):
        if not self.id:
            self.created = datetime.date.today()
        self.updated = datetime.datetime.today()
        super(QUEST_MODEL, self).save()
################################################################################################         
class ANNUAL(models.Model):
    logged_in = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, help_text='subject_teacher')
    student_name = models.ForeignKey(CNAME, on_delete=models.SET_NULL, null=True)#
    first = models.FloatField(max_length=4, blank=True, null=True)
    second = models.FloatField(max_length=4, blank=True, null=True)
    third = models.FloatField(max_length=4, blank=True, null=True)
    anual = models.FloatField(max_length=10, blank=True, null=True)#
    agr = models.FloatField(max_length=10, blank=True, null=True)
    grade = models.CharField(max_length=5, blank=True, null=True)
    anu_posi = models.CharField(max_length=5, blank=True, null=True)
    subject_by = models.ForeignKey(BTUTOR, on_delete=models.CASCADE, blank=True, null=True, help_text='subject_teacher')
    subject =  models.ForeignKey(ASUBJECTS, on_delete=models.SET_NULL, null=True)
    term = models.CharField(max_length=15, default='None', blank=True, null=True)
    model_in = models.CharField(max_length=15, default='None', blank=True, null=True)
    class Meta:
          ordering = ('student_name_id',) # helps in alphabetical listing. Sould be a tuple
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}:{self.subject_by.user}'
    def get_absolute_url(self):
        """Returns the url to access a detail record for this student."""
        return reverse('annualmodel-detail', args=[str(self.id)])
   
class TOTAL(models.Model):
    logged_in = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, help_text='Logged-in-user')
    subject_by = models.ForeignKey(BTUTOR, on_delete=models.CASCADE, blank=True, null=True, help_text='subject_teacher')
    subject =  models.ForeignKey(ASUBJECTS, on_delete=models.SET_NULL, null=True)#
    subject_scores = models.FloatField(max_length=9, blank=True, null=True)
    subject_pert = models.FloatField(max_length=9, blank=True, null=True)
    term_status = (('1st Term', 'first term'), ('2nd Term', 'second term'), ('3rd Term', 'third term'))
    term = models.CharField(max_length=30, choices=term_status, blank=True, null=True, help_text='subject term',)
    model_in = models.CharField(max_length=6, default='total', blank=True, null=True)
    class Meta:
          ordering = ('term',) # helps in alphabetical listing. Sould be a tuple
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}:{self.subject_by.user}'
    def get_absolute_url(self):
        """Returns the url to access a detail record for this student."""
        return reverse('totalmodel-detail', args=[str(self.id)])

class Edit_User(models.Model):
   def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit*459*571:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
   user = models.OneToOneField(User, on_delete=models.CASCADE,  blank=True, null=True, related_name='profile')
   last_name = models.CharField(max_length=20, blank=True)
   first_name = models.CharField(max_length=20, blank=True)
   photo = models.ImageField(upload_to='static/result/', validators=[validate_image], null=True, blank=True)
   bio = models.TextField(blank=True)
   phone = models.CharField(max_length=20, blank=True)
   city = models.CharField(max_length=15, blank=True)
   country = models.CharField(max_length=10, blank=True)
   organization = models.CharField(max_length=10, blank=True)
   location = models.CharField(max_length=30, blank=True)
   birth_date = models.DateField(null=True, blank=True, help_text='Date format: MM/DD/YYYY')
   section_status = (('Sc', 'Sciences'), ('SSc', 'Social Sciences'), ('Art', 'Arts and Humanities'))
   department = models.CharField(max_length=30, choices=section_status, blank=True, null=True)
   account_status = (('Student', 'Student'), ('Staff', 'Staff'))
   account = models.CharField(max_length=30, choices=account_status, blank=True, null=True)
   email_confirmed = models.BooleanField(default=False, help_text='True/False')
   model_in = models.CharField(max_length=15, default='user_profile', blank=True, null=True)
       
   def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}:{self.user.username}'
   class Meta:
          ordering = ('account',)
   def get_absolute_url(self):
        return reverse('pro_detail', args=[str(self.id)])

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

