# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:37:37 2020

@author: ojaro
"""
from CourseManagement import CourseManagement
from MovieManagement import MovieManagement
from Course import Course
from User import User

class DashboardController:
    def __init__(self,user: User):
        self.user = user
        self.course_manager = CourseManagement()
        self.courses = [] #enrolled courses for student, owned courses for professor
        
        
        self.movies_in_progress = []
        
        self. statistics = None #statistics about movies and courses (only for professor)
        #TODO: load unfinished movies watched by user from MovieManagement
        #TODO: load courses for user from CourseManagement
        #TODO: load statitiscs if professor is signed in
        