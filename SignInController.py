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
        self.Manager = UserManagement.UserManagement() #lazy init
        
    def AttemptSignIn(self,username: str, password: str)->str:
        #this is for dev reasons
        if(username == "aa" and password == "aa"):
            user = Student(0)
            main_window = MainWidget(user)
            return "success"
        if (username=="" or password==""):
            return ("Error empty field(s)")
        else:
            model_result, entity, userID = self.Manager.CheckForUserPass(username, password)
            if(model_result == 1):
                if(entity == 'student'):
                    user = Student(userID)
                elif(entity == 'professor'):
                    user = Professor(userID)
                    
                main_window = MainWidget(user)
                return "success"
            else:
                return ("Username or Password Incorrect")
        
    def ToRegister(self):
             register_window = RegisterLayout()
             return ("success")
    
    