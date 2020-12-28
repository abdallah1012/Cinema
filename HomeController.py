# -*- coding: utf-8 -*-


from RecommendationEngine import RecommendationEngine
from User import User
from MovieLayout import MovieLayout
from MovieManagement import MovieManagement

import base64 

#controller for the relevant layout to communicate with other layouts and computation models
class HomeController:
    def __init__(self,user:User):
        self.user = user
        #self.r_engine = RecommendationEngine()
        #self.r_engine.WhatsHot()
        #self.r_engine.LoadRecommendations(self.user.id)
        self.movie_manager = MovieManagement() #manager used to communicate with movies table in database
        self.recommender = RecommendationEngine()
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
        
        Movies=self.recommender.LoadRecommendations(self.user)
        byteImages = []
        for i in Movies:
            byteImages += self.movie_manager.getThumbNailsMovieID(i)
        if(isinstance(byteImages, int) == False):
            url = []
            images = []
            movieIDs = []
            titles = []
            for i in byteImages:
                movieIDs.append(i[2])
                images.append(i[0])
                url.append(i[1])
                titles.append(i[3])
        else:
            images =[]
            url = []
            movieIDs = []
            titles = []
        return images, url, movieIDs, titles
    
    #talks to manager to get list of hot movies
    def getHot(self):
        Movies= self.recommender.WhatsHot()
       
        byteImages = []
        for i in Movies:
            byteImages += self.movie_manager.getThumbNailsMovieID(i)
        
        if(isinstance(byteImages, int) == False):
            url = []
            images = []
            movieIDs = []
            titles = []
            for i in byteImages:
                movieIDs.append(i[2])
                images.append(i[0])
                url.append(i[1])
                titles.append(i[3])
        else:
            images =[]
            url = []
            movieIDs = []
            titles = []
        
        return images, url, movieIDs, titles