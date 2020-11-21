# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:46:53 2020

@author: ojaro
"""
from RecommendationEngine import RecommendationEngine
from User import User
from MovieWidget import MovieWidget
class HomeController:
    def __init__(self,user:User):
        self.user = user
        self.r_engine = RecommendationEngine()
        self.r_engine.WhatsHot()
        self.r_engine.LoadRecommendations(self.user.id)
        
    def loadMovieWidget(self):
        self.movie_widget = MovieWidget()
#        self.movie_widget.show()
#        self.movie_widget.resize(640,480)