# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:54:51 2020

@author: ojaro
"""
from enum import Enum

class UserPrivilege(Enum):
    STUDENT = 1
    PROFESSRO =2
    
class User:
    def AttemptSignIn(username: str, password: str)->str:
        if (username=="" or password==""):
            return "Error empty field(s)!"
        else:
            return "success student"
        
    