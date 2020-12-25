# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:35:54 2020

@author: ojaro
"""
from User import User
from UserManagement import UserManagement
from HomeLayout import HomeLayout
from PasswordChangeLayout import PasswordChangeLayout

#controller for the relevant layout to communicate with other layouts and computational models
class ProfileController():
    def __init__(self,user:User):
        self.Manager=UserManagement.UserManagement()
        self.user=user
    
    def goBack(self):
        #reinitialize user with the new edited variables (image and password might be altered)
        homelayout = HomeLayout.HomeLayout()
        homelayout.show()
        return "succes"
        
    def changePassword(self):
        passwordlayout=PasswordChangeLayout.PasswordChangeLayout(self.user)
        passwordlayout.show()
        return "succes"
    
    def editProfilePic(self, fname):
        #add SQL call that changes the image directory to the one chosen by the user
        return "success"
        
