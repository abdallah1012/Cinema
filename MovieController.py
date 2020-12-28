# -*- coding: utf-8 -*-

from MovieManagement import MovieManagement
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