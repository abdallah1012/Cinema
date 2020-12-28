# -*- coding: utf-8 -*-

import User
from MovieManagement import MovieManagement
class CourseMovieController:
    def __init__(self,user: User):
        self.manager = MovieManagement()
    
    def getCMovies(self, CID):
        return self.manager.getCourseMovies(CID)