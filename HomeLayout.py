# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:43:35 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QGridLayout,QLabel,QWidget
from RecommendationEngine import RecommendationEngine

class HomeLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.temp_label = QLabel("Home tab clicked")
        self.__home_grid = QGridLayout()
        self.__home_grid.addWidget(self.temp_label)
        self.setLayout(self.__home_grid)
        
        # r_engine = RecommendationEngine(self.user_)
        # r_engine.WhatsHot()
        # r_engine.LoadRecommendations()