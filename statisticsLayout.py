# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QLabel, QFormLayout
from statisticsController import statisticsController
class statisticsLayout(QWidget):

    def __init__(self, views, desc, likes):
        super().__init__()
        layout = QFormLayout()
        self.controller = statisticsController()
        self.numofviews = views
        self.desc = desc
        self.numoflikes = likes
        self.setStyleSheet(open('main.css').read())
        self.description = QLabel("Description: " + str(self.desc))	
        self.views = QLabel("Number of Views: " + str(self.numofviews))     
        self.likes = QLabel("Number of likes: " + str(self.numoflikes))
        
        
        layout.addRow(self.description)
        layout.addRow(self.views)
        layout.addRow(self.likes)
        
        self.setLayout(layout)
        self.setWindowTitle("Movie Statistics")
    
          
