#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 14:19:13 2020

@author: bbaajour
"""
from User import User
from UserManagement import UserManagement
#from ProfileLayout import ProfileLayout

class ChangePasswordController():
    def __init__(self, user:User):
        self.Manager=UserManagement()
        self.user=user
        
#    def goBack(self):
#        profilelayout=ProfileLayout()
#        profilelayout.show()
#        return "success"
#    
    def changePassword(self, old_password, new_password):
        #if old password is correct
        #   if new password passes the test
        
        try:
            result, entity, userid = self.Manager.CheckForUserPass(self.user.username, old_password)
            if(result == 1):
                self.Manager.changePass(self.user.id, new_password)
                return 1 #success
            else:
                return 2 #wrong password
                
        except:
            return 0 #database failed
        
        
        
        
    