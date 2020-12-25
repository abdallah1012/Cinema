# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:54:40 2020

@author: ojaro
"""
from User import User

#Student class which keeps the attributes of a student throughout running time after signing in
class Student(User):
    def __init__(self,ID:int,courses,first_name,last_name,username,image):
        super().__init__()
        self.id = ID #students ID from the users table
        self.courses = courses #courses which the student is enrolled in
        self.first_name=first_name #first name of the student
        self.last_name=last_name #last name of the student
        self.username=username #username of the student
        self.image=image
        
        #credentials of the student are cached to minimize SQL calls