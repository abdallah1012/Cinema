# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:54:40 2020

@author: ojaro
"""
from User import User


class Student(User):
    def __init__(self,ID:int,courses):
        super().__init__()
        self.id = ID
        self.courses = courses