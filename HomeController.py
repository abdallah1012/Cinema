# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:46:53 2020

@author: ojaro
"""

from RecommendationEngine import RecommendationEngine
from User import User
from MovieLayout import MovieLayout
from MovieManagement import MovieManagement
import base64 

#controller for the relevant layout to communicate with other layouts and computation models
class HomeController:
    def __init__(self,user:User):
        self.user = user
        self.r_engine = RecommendationEngine()
        self.r_engine.WhatsHot()
        self.r_engine.LoadRecommendations(self.user.id)
        self.movie_manager = MovieManagement() #manager used to communicate with movies table in database
    
    #loads the movie widget
    def loadMovieWidget(self):
        self.movieLayout = MovieWidget()
        return self.movieLayout
        
      
        
#         self.movieLoad = threading.Thread(target=self.loadMovie, args=(main,)) 
#         self.movieLoad.start()
#         self.movieLoad.join()
    
    #loads movie (no longer in use)
    def loadMovie(self, main):      
        self.movie_widget = MovieWidget()
        main.vbox.addWidget(self.movie_widget)
        main.example_movie.hide()
      
    #talks to manager to get list of recommended movies
    def getRecommended(self):
        byteImages = self.movie_manager.getThumbNails()
        
        images = []
        for i in byteImages:
            
            images.append(i[0])
            
        return images
    
    #talks to manager to get list of hot movies
    def getHot(self):
        byteImages = self.movie_manager.getThumbNails()
        
        images = []
        for i in byteImages:
            
            images.append(i[0])
            
        return images