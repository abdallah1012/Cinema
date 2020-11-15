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
        self.recommended_for_you = QLabel("Recommended for you")
        self.whats_hot = QLabel("What's hot")
        
        self.__home_grid.addWidget(self.recommended_for_you, 2, 0)
        self.__home_grid.addWidget(self.whats_hot, 2, 0)

        self.setLayout(self.__home_grid)
        
        self.r_engine = RecommendationEngine()
        self.r_engine.WhatsHot()
        self.r_engine.LoadRecommendations(self.user.id)