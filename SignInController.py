# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:54:51 2020

@author: ojaro
"""
from MainWidget import MainWidget
from Student import Student 
from Professor import Professor
from RegisterLayout import RegisterLayout

class SignInController:
    def __init__(self):
        pass
    def AttemptSignIn(self,username: str, password: str)->str:
        if (username=="" or password==""):
            return ("Error empty field(s)")
        else:
            #send request to UMS and receieve response
            #expecting user id
            #send request to MMS to receive recommendations
            user = Student(0)
            main_window = MainWidget(user)
            return ("success")
        
    def ToRegister(self):
            
            register_window = RegisterLayout()
            return ("success")
    
        
    def CheckUser(self, username, password):
        pass
    