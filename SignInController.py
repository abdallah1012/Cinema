# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:54:51 2020

@author: ojaro
"""
from MainWidget import MainWidget
from Student import Student 
from Professor import Professor
from RegisterLayout import RegisterLayout
import UserManagement

class SignInController:
    def __init__(self):
        self.Manager = UserManagement.UserManagement()
    def AttemptSignIn(self,username: str, password: str)->str:
        #this is for dev reasons
        if(username == "aa" and password == "aa"):
            user = Student(0)
            main_window = MainWidget(user)
            return "success"
        if (username=="" or password==""):
            return ("Error empty field(s)")
        else:
            #send request to UMS and receieve response
            #expecting user id
            #send request to MMS to receive recommendations
            
            result, entity = self.Manager.CheckForUserPass(username, password)
            if(result == 1):
                if(entity == 'student'):
                    user = Student(0)
                elif(entity == 'professor'):
                    user = Professor(0)
                    
                main_window = MainWidget(user)
                return "success"
            else:
                return ("Username or Password Incorrect")
        
    def ToRegister(self):
            
            register_window = RegisterLayout()
            return ("success")
    
        
    def CheckUser(self, username, password):
        pass
    