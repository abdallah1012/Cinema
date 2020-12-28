# -*- coding: utf-8 -*-

from CourseManagement import CourseManagement
from MovieManagement import MovieManagement
from User import User

#controller for relevant layout to communicate with other layouts and communication models
class DashboardController:
    def __init__(self,user: User):
        self.user = user
        self.course_manager = CourseManagement()
        self.movie_manager = MovieManagement()


        self.movies_in_progress = []
        
        self. statistics = None #statistics about movies and courses (only for professor)
        #TODO: load unfinished movies watched by user from MovieManagement
        #TODO: load courses for user from CourseManagement
        #TODO: load statitiscs if professor is signed in

        
        
        
        
        
        
        
        
        