# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:20:06 2020

@author: ojaro
"""

#Recommendation model used to find which movies should be recommended to the user
#and what movies are generally good --> "hot"
class RecommendationEngine:
    
    def __init__(self):
        pass
    
    def WhatsHot(self):
        pass
    #TODO:  Send query to MMS to retrieve list of "hottest" movies.
    #       Criteria can be highest number of views and highest ratings (TBD)
    
    def LoadRecommendations(self,ID: int):
        pass
    #TODO:  Send query to MMS to retrieve list of "Recommended" movies for currently signed in user
    