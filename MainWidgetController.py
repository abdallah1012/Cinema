# -*- coding: utf-8 -*-

import User
from UserManagement import UserManagement
from CourseManagement import CourseManagement
from Student import Student
from Professor import Professor

class MainWidgetController():
    def __init__(self, user:User):
        self.user = user
        self.Manager = UserManagement() #manager for communication with the user table
        self.course_manager = CourseManagement() #manager for communication with the course table
    
    def refresh(self):

        if(isinstance(self.user, Student)==True):
            return self.course_manager.getCoursesStudent(self.user.id)   
            
        elif(isinstance(self.user, Professor)==True):
            return self.course_manager.getCourses(self.user.id)
        
        
        