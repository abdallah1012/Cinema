# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:20:16 2020

@author: ojaro
"""
from User import User

class Professor(User):
    def __init__(self,ID:int,courses):
        super().__init__()
        self.id = ID
        self.courses = courses