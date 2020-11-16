# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:43:35 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QGridLayout,QLabel,QWidget
from RecommendationEngine import RecommendationEngine
from User import User

class HomeLayout(QWidget):
    def __init__(self,user:User):
        self.user = user
        super().__init__()
        self.__home_grid = QGridLayout()
        self.recommended_for_you_label = QLabel("Recommended for you")
        self.whats_hot_label = QLabel("What's hot")
        self.recommended_for_you = [] #list of recommended movies
        self.whats_hot = [] #list of popular movies
        self.__home_grid.addWidget(self.recommended_for_you_label, 2, 0)
        self.__home_grid.addWidget(self.whats_hot_label, 3, 0)

        self.setLayout(self.__home_grid)
        
        self.r_engine = RecommendationEngine()
        self.r_engine.WhatsHot()
        self.r_engine.LoadRecommendations(self.user.id)
        #TODO: populate self.recommended_for_you list and add to GUI
        #TODO: populate self.whats_hot list and add to GUI
        
        