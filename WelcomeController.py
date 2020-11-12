# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:54:51 2020

@author: ojaro
"""
from MainWindow import MainWindow
from Student import Student 
from Professor import Professor
    
class WelcomeController:
    def __init__(self):
        pass
    def AttemptSignIn(self,username: str, password: str)->str:
        if (username=="" or password==""):
            return ("failure")
        else:
            #send request to UMS and receieve response
            #expecting user id
            #send request to MMS to receive recommendations
            std = Student(0)
            main_window = MainWindow(std)
            return ("success")
    
        
        
    