# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:57:11 2020

@author: WarPeace101
"""

from CourseManagement import CourseManagement
from MovieManagement import MovieManagement
#controller for relevant layout to communicate with other layouts and computation models
class CourseInputController:
    def __init__(self):
        self.course_manager = CourseManagement() #manager that allows communication with course table in database
        self.movie_manager = MovieManagement()
    
    #adds course to courses table in database
    #params: string coursename, string description, int userID
    #returns 0 if a database error occurred and 1 if successfull and 2 if the course was already uploaded by the same user before
    def addCourse(self, coursename, description, userID, faculty, typeofCourse):
 
        try:
            exists = self.course_manager.CheckForCourseUser(coursename, userID)
        except:
            return 0 #Database error
        
        if(exists == 0):
           
                result = self.course_manager.AddToCourses(coursename, description, userID, faculty, typeofCourse)
                if(result == 1):
                    return 1 #sucessfully added course to database
                else:
                    print("failed to add course")
                    return 0 #database error
        else:
            return 2 #course already exists with user
        
    def getAllCourses(self):
        return self.course_manager.getAllCourses()
    
    def getCoursePerFaculty(self, faculty):
        return self.course_manager.getCoursePerFaculty(faculty)
    
    
    def EnrollStudent(self, courseId, userId, courseName):
       
        return self.course_manager.EnrollStudent(courseId, userId, courseName)