# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:20:16 2020

@author: ojaro
"""
from User import User

class Professor(User):
    def __init__(self,ID:int):
        super().__init__(ID)
        self.id = ID