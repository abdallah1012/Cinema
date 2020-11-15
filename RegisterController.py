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
        
        sqlstmt = "SELECT * FROM users WHERE username = '"+str(username)+"'"
       
        result = self.Manager.CheckForUsername(sqlstmt)    
        return result
    
    def RegisterUser(self, username, firstname, lastname, password, user):
        #try later to encrypt password
        
        sqlstmt = "INSERT INTO users VALUES ('"+str(username)+"', '"+str(firstname)+"', '"+str(lastname)+"', '"+str(password)+"', '"+str(user)+"');"
        
        result = self.Manager.AddToUsers(sqlstmt)
        return result
        
    
    def goBack(self):
        
        
        Signin = WelcomeWidget.WelcomeWidget()
        Signin.show()
        
        return "success"
        
        
        
        
        
        
        