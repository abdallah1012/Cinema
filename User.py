# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:54:51 2020

@author: ojaro
"""
from enum import Enum
from MainWindow import MainWindow

class UserPrivilege(Enum):
    STUDENT = 1
    PROFESSOR =2
    
class User:
    def AttemptSignIn(username: str, password: str)->str:
        if (username=="" or password==""):
            return ("failure")
        else:
            #send request to UMS and receieve response
            #expecting user id
            main_window = MainWindow(UserPrivilege.PROFESSOR,0)
            
            return ("success")
    
    def __init__(self):
        pass
        
    