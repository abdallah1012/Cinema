# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:37:37 2020

@author: ojaro
"""
from CourseManagement import CourseManagement
from MovieManagement import MovieManagement
from Course import Course
from User import User
from source import uploadToYoutube

class DashboardController:
    def __init__(self,user: User):
        self.user = user
        self.course_manager = CourseManagement()
        self.movie_manager = MovieManagement()
       
        
        courses = self.course_manager.getCourses(self.user)

        if(courses != 0):
            self.courses = courses #enrolled courses for student, owned courses for professor
        else:
            self.courses = []
        
        self.movies_in_progress = []
        
        self. statistics = None #statistics about movies and courses (only for professor)
        #TODO: load unfinished movies watched by user from MovieManagement
        #TODO: load courses for user from CourseManagement
        #TODO: load statitiscs if professor is signed in
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
        


    def addMovie(self, moviename, courseID, description, userID, url, thumbnail):
        try:      
            exists = self.movie_manager.CheckForMovieUser(moviename, userID)
        except:         
            return 0 #Database error
        
        try:
            videoid = uploadToYoutube(url)
        except:
            return 3 #youtube error
        
        if(exists == 0):         
                result = self.movie_manager.addMovie(moviename, courseID, description, userID, "https://youtu.be/" + videoid['id'])
                if(result == 1):
                    return 1 #sucessfully added course to database
                else:
                    print("failed to add course")
                    return 0 #database error
        else:
            return 2 #course already exists with user