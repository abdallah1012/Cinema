# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:43:35 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QGridLayout,QLabel,QWidget,QPushButton, QVBoxLayout, QMainWindow, QStackedLayout
from User import User
from HomeController import HomeController
from PyQt5.QtCore import pyqtSignal


class HomeLayout(QWidget):
    _WatchMovie_ = pyqtSignal()
    def __init__(self,user:User):
        self.user = user
        super().__init__()
        self.controller = HomeController(user)
        
        self.__home_grid = QGridLayout()
        self.recommended_for_you_label = QLabel("Recommended for you")
        self.whats_hot_label = QLabel("What's hot")
        self.recommended_for_you = [] #list of recommended movies
        self.whats_hot = [] #list of popular movies
        self.__home_grid.addWidget(self.recommended_for_you_label, 2, 0)
        self.__home_grid.addWidget(self.whats_hot_label, 3, 0)
        self.example_movie = QPushButton("Example movie")
        
        self.example_movie.clicked.connect(lambda:self._WatchMovie_.emit())
        
        self.stack = QStackedLayout()
        
        self.movieLayout = None
        
        self.__home_grid.addWidget(self.example_movie,4,1)
        

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.__home_grid)
        self.vbox.addLayout(self.stack)
        
        print(self.stack)
        
        self.setLayout(self.vbox)
        
      

        
        
        
        #TODO: populate self.recommended_for_you list and add to GUI
        #TODO: populate self.whats_hot list and add to GUI
        
        
        
        
        
        