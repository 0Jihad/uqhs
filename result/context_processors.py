# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 05:45:36 2019

@author: AdeolaOlalekan
"""
from result.models import Edit_User 
def logon_images(request):
    if request.user.is_authenticated:
        logon_image = Edit_User.objects.filter(user=request.user)
        return {'logo':logon_image}