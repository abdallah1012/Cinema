# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:43:35 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QGridLayout,QLabel,QWidget,QPushButton, QVBoxLayout, QMainWindow, QStackedLayout
from User import User
from HomeController import HomeController
from PyQt5.QtCore import pyqtSignal
from ImageSlider import ImageSlider

class HomeLayout(QWidget):
    _WatchMovie_ = pyqtSignal()
    def __init__(self,user:User):
        self.user = user
        super().__init__()
        self.controller = HomeController(user)        
        self.__home_grid = QGridLayout()
        self.recommended_for_you_label = QLabel("Recommended for you")
        self.whats_hot_label = QLabel("What's hot")
        
        self.recommended_display = ImageSlider()
        self.hot_display = ImageSlider()
        
        self.recommended_for_you = [] #list of recommended movies
        self.whats_hot = [] #list of popular movies
        
        
        
        self.example_movie = QPushButton("Example movie")        
        self.example_movie.clicked.connect(lambda:self._WatchMovie_.emit())
        self.stack = QStackedLayout()       
        self.movieLayout = None       
        self.__home_grid.addWidget(self.example_movie,5,1)
        self.vbox = QVBoxLayout()
        
        self.vboxRecommended = QVBoxLayout()
        self.vboxRecommended.addWidget(self.recommended_for_you_label)   
        self.vboxRecommended.addWidget(self.recommended_display)
        
        self.vboxhot = QVBoxLayout()
        self.vboxhot.addWidget(self.whats_hot_label)
        self.vboxhot.addWidget(self.hot_display)
        
       
        self.vbox.addLayout(self.__home_grid)
        self.vbox.addLayout(self.vboxRecommended)
        self.vbox.addLayout(self.vboxhot)
        self.vbox.addLayout(self.stack)
        
        print(self.stack)
    
        self.generateRecommended()
        self.generateHot()
        self.setLayout(self.vbox)
        
    
    def generateRecommended(self):
        self.images = self.controller.getRecommended()
        self.recommended_display.setImages(self.images)
        
    def generateHot(self):
        self.imageshot = self.controller.getHot()
        self.hot_display.setImages(self.images)
        
        #TODO: populate self.recommended_for_you list and add to GUI
        #TODO: populate self.whats_hot list and add to GUI
        

        