

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 08:25:37 2019

@author: AdeolaOlalekan
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BTUTOR, CNAME, ASUBJECTS, Edit_User, QSUBJECT, Post
from django.core.files.images import get_image_dimensions

class subjectforms(forms.ModelForm):
    class Meta:
        model = ASUBJECTS
        fields = ( 'name',)#, 'subject_teacher',)
        
class teacherform(forms.ModelForm):
    class Meta:
        model = BTUTOR
        fields = ('user', 'subject', 'Class', 'term', 'teacher_name',)
        
        
class student_names(forms.ModelForm):
    class Meta:
        model = CNAME
        fields = ('student_name',)
        
class login_form(forms.Form):
    username = forms.CharField(max_length=8)#, help_text="Just type 'renew'")
    password1 = forms.CharField(widget=forms.PasswordInput)#
    
    def clean_data(self):
        data = self.cleaned_data['username']
        data = self.cleaned_data['password1']
        return data

class new_password(forms.Form):
    email = forms.CharField(max_length=254)#, help_text="Just type 'renew'")
    def clean_email(self):
        data = self.cleaned_data['email']
        return data
###############################################################################  
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Edit_User
        fields = ('first_name', 'last_name', 'bio', 'phone', 'city', 'country', 'organization', 'location', 'birth_date', 'department', 'photo',)
        exclude = ['user']
        
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required for a valid signup!')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password1']
        if commit:
            user.save()
        return user

class SSignUpForm(forms.Form):
    username = forms.CharField(max_length=254)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(max_length=254)
    def clean_data(self):
        data = self.cleaned_data['username']
        data = self.cleaned_data['password1']
        data = self.cleaned_data['password2']
        data = self.cleaned_data['email']
        return data
    def save(self, commit=True):
        user = super(SSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password1']
        if commit:
            user.save()
        return user
          
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Edit_User
        fields = ('photo',)
    def clean_avatar(self):
        avatar = self.cleaned_data['photo']

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar
    
 

class subject_class_term_Form(forms.ModelForm):
    class Meta:
        model = BTUTOR
        fields = ('subject','Class', 'term',)
        
class name_class_Form(forms.ModelForm):
    class Meta:
        model = QSUBJECT
        fields = ('student_name','Class',)
        
class tutor_class_Form(forms.ModelForm):
    class Meta:
        model = QSUBJECT
        fields = ('tutor','cader',)
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Account_Username', 'subject', 'text') 
        
class a_student_form_new(forms.ModelForm):
    class Meta:
        model = QSUBJECT
        fields = ('student_name','test', 'agn','atd', 'exam','tutor', 'Class',)
        

class student_name(forms.ModelForm):
    class Meta:
        model = CNAME
        fields = ('student_name','Class',)
#class student_name(forms.Form):
    #student_name = forms.DateField(help_text="Enter student Name")
    #def clean_renewal_date(self):
        #data = self.cleaned_data['student_name']
        #return data
    
