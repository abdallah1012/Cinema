# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:57:11 2020

@author: WarPeace101
"""
from User import User
from CourseManagement import CourseManagement

class CourseInputController:
    def __init__(self):
        self.course_manager = CourseManagement()
       
    def addCourse(self, coursename, description, userID):
        
        
        
        try:
            exists = self.course_manager.CheckForCourseUser(coursename, userID)
        except:
            return 0 #Database error
        
        if(exists == 0):
           
                result = self.course_manager.AddToCourses(coursename, description, userID)
                if(result == 1):
                    return 1 #sucessfully added course to database
                else:
                    print("failed to add course")
                    return 0 #database error
        else:
            return 2 #course already exists with user