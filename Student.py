# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:54:40 2020

@author: ojaro
"""
from User import User

#Student class which keeps the attributes of a student throughout running time after signing in
class Student(User):
    def __init__(self,ID:int,courses):
        super().__init__()
        self.id = ID #students ID from the users table
        self.courses = courses #courses which the student is enrolled in