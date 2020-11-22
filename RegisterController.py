# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:34:50 2020

@author: WarPeace101
"""

from sqlalchemy import create_engine
import pandas as pd
import WelcomeWidget
import UserManagement

class RegisterController:
    def __init__(self):   
       
        #change localhost to IP address and root to username of database
        #This was tested using wampserver
        self.Manager = UserManagement.UserManagement()
        
    
    def CheckUserExists(self, username):
        
        result = self.Manager.CheckForUsername(username)    
        return result
    
    def RegisterUser(self, username, firstname, lastname, password, user):
        
        result = self.Manager.AddToUsers(username, firstname, lastname, password, user)
        return result
        
    
    def goBack(self):
        
        
        Signin = WelcomeWidget.WelcomeWidget()
        Signin.show()
        
        return "success"
        
        
        
        
        
        
        