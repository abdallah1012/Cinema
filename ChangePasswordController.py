#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 14:19:13 2020

@author: bbaajour
"""
from User import User
from UserManagement import UserManagement
from ProfileLayout import ProfileLayout

class ChangePasswordController():
    def __init__(self, user:User):
        self.Manager=UserManagement.UserManagement()
        self.user=user
        
    def goBack(self):
        profilelayout=ProfileLayout.ProfileLayout()
        profilelayout.show()
        return "succes"
    
    def changePassword(self, old_password, new_password):
        #if old password is correct
        #   if new password passes the test
        profilelayout=ProfileLayout.ProfileLayout()
        profilelayout.show()
        return "succes"
        #   else new password does not meet requirements return "Passwords must be 8 chacarers long and include at least 1 Captial letter"
        #else return "Old Password does not match"
        
        
    