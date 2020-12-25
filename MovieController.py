# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 16:44:05 2020

@author: ojaro
"""

from MovieManagement import MovieManagement
class MovieController:
    def __init__(self,url):
        self.url = url
        self.manager =MovieManagement()
        self.incrementViews()
    
    
    def incrementViews (self):
        self.manager.incrementViewsByURL(self.url)