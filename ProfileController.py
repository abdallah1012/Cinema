# -*- coding: utf-8 -*-

from User import User
from UserManagement import UserManagement

#controller for the relevant layout to communicate with other layouts and computational models
class ProfileController():
    def __init__(self,user:User):
        self.Manager = UserManagement()
        self.user=user
    
    
    def editProfilePic(self, fname):
        #add SQL call that changes the image directory to the one chosen by the user
        return self.Manager.giveUserImage(self.user.id, fname)
        
