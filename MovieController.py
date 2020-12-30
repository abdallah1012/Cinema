# -*- coding: utf-8 -*-

from MovieManagement import MovieManagement
from statisticsLayout import statisticsLayout
class MovieController:
    def __init__(self,url):
        self.url = url
        self.manager =MovieManagement()
        self.incrementViews()
    
    
    def incrementViews (self):
        self.manager.incrementViewsByURL(self.url)
        
    def submitComment(self, movieID, comment, user):
        return self.manager.submitComment(movieID, comment, user)
    
    def getComments(self, movieID):
        return self.manager.getComments(movieID)
    
    def LikeMovie(self, movieID, userID):
        return self.manager.addLike(movieID, userID)
    
    def removieLike(self, movieID, userID):
        return self.manager.deleteLike(movieID, userID)
    
    def getLikeStatus(self, movieID, userID):
        return self.manager.getLikeStatus(movieID, userID)
    
    def isMovieForUser(self, movieID, userID):
        return self.manager.isMovieForUser(movieID, userID)
    
    def openStatsLayout(self, views, desc, likes):
        stats = statisticsLayout(views, desc, likes)
        return stats