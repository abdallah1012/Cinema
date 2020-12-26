# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 19:13:27 2020

@author: WarPeace101
"""
import User
from MovieManagement import MovieManagement
class CourseMovieController:
    def __init__(self,user: User):
        self.manager = MovieManagement()
    
    def getCMovies(self, CID):
        return self.manager.getCourseMovies(CID)