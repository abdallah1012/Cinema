# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:46:53 2020

@author: ojaro
"""

from RecommendationEngine import RecommendationEngine
from User import User
from MovieLayout import MovieLayout
import threading

class HomeController:
    def __init__(self,user:User):
        self.user = user
        self.r_engine = RecommendationEngine()
        self.r_engine.WhatsHot()
        self.r_engine.LoadRecommendations(self.user.id)
        
    def loadMovieWidget(self):
        self.movieLayout = MovieWidget()
        return self.movieLayout
        
      
        
#         self.movieLoad = threading.Thread(target=self.loadMovie, args=(main,)) 
#         self.movieLoad.start()
#         self.movieLoad.join()
    
    def loadMovie(self, main):      
        self.movie_widget = MovieWidget()
        main.vbox.addWidget(self.movie_widget)
        main.example_movie.hide()