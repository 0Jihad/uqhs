# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 05:10:08 2019

@author: AdeolaOlalekan
"""

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm, new_password, Sign_Up_Type, SSignUpForm
from django.shortcuts import render, redirect
from .tokens import account_activation_token
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views import generic
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.http import HttpResponse#, HttpResponseRedirect
#from django.core.mail import send_mail
#send_mail('noreply', 'body of the message', 'adeolaolalekan1431@yahoo.com', ['adeolaolalekan01831@gmail.com', 'adeolaolalekan1831@outlook.com'])
class Staff_SignUp(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('registration:logins')
    form_valid_message = 'User has been created successfully!'
    form_invalid_message = 'Something wrong'
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                fd = form.cleaned_data
                username = fd['username']
                email = fd['email']
                password1 = fd['password1']
                password2 = fd['password2']
                password = None
                if password1 == password2:
                    password = password1
                if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    userObj = User.objects.create_user(username=username, email=email, password=password)
                    userObj.is_active = False
                    userObj.save()
                    profile = userObj.profile
                    profile.bio = 'new!'
                    profile.account = ['', 'Student', 'Staff']
                    profile.save()
                    current_site = get_current_site(request)
                    mail_subject = 'Activate your blog account.'
                    message = render_to_string('registration/account_activation_email.html', {
                        'user': User,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(userObj.pk)).decode(),
                        'token': account_activation_token.make_token(userObj),
                    })
                    to_email = form.cleaned_data.get('email')
                    email = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
                    email.send()
                    # user = authenticate(username=username, password=password)
                    # login(request, user)
    
                    return render(request, 'registration/account_activation_sent.html')
                else:
                    return HttpResponse("This Email Already exists, Use another email address please!")
    
        else:
            form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('new', pk=user.id)
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
    
def reset(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('passwords')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
    
def lost_password(request):
    if request.method == 'POST':
        form = new_password(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data.get('email') 
            nill = User.objects.filter(email = to_email).count()
            if nill != 0:
                userObj = User.objects.get(email = to_email)
                userObj.is_active = False
                userObj.save()             
                current_site = get_current_site(request)
                mail_subject = 'Follow the link to Reset Your Password.'
                message = render_to_string('result/re_acc_active_email.html', {
                'user': User,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(userObj.pk)).decode(),
                'token': account_activation_token.make_token(userObj),
                })
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return render(request, 'registration/account_re_activation_sent.html')
            else:
                return HttpResponse("This Email does NOT exists, Use corect email address please!")           
    else:
        form = new_password()
    return render(request, 'registration/get_email.html', {'form': form})
###############################################################################

