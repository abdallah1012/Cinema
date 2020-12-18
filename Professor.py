# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:20:16 2020

@author: ojaro
"""
from User import User

#professor class extending the user class which is used throughout running time
#to be used for user specific activities
class Professor(User):
    def __init__(self,ID:int,courses):
        super().__init__()
        self.id = ID #unique ID of user
        self.courses = courses #courses which the professor is giving