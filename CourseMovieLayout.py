# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:58:35 2020

@author: 
"""
from PyQt5.QtWidgets import QGridLayout,QLabel,QWidget,QPushButton, QVBoxLayout, QMainWindow, QStackedLayout, QListWidget,QListWidgetItem
import User
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtGui import QIcon, QPixmap
from ClickableThumbnail import ClickableThumbnail
from MovieManagement import MovieManagement
import base64 
class CourseMovieLayout(QWidget):
    goback_request = pyqtSignal(int)
    
    def __init__(self,user:User, courseID):
        super().__init__()
        self.list_widget = QListWidget()
        self.user = user
        self.courseID = courseID
#        self.list_widget.setFlow(QListView.LeftToRight) 
        self.list_widget.setIconSize(QSize(190, 190))
        self.list_widget.hasAutoScroll()
        
        self.list_widget.setAutoFillBackground( False )
        self.items_title = self.user.courses
        self.Manager= MovieManagement()
   
        self.error = QLabel()
            
        self.movies=self.Manager.getCourseMovies(self.courseID)
        self.titles = []
        self.thumbnails = []
        self.urls = []
        if(len(self.movies) != 0):
            for i, j, k in self.movies:
                self.titles.append(i)
                self.thumbnails.append(j)
                self.urls.append(k)
            self.setImages(self.thumbnails, self.urls, self.titles)    
        else:
            self.error.setText("Course Has No Movies")
           
        self.back = QPushButton("Back")
        self.back.clicked.connect(lambda: self.BACK())
        self.vbox = QVBoxLayout()
        
        self.vbox.addWidget(self.list_widget)
        
        self.vbox.addWidget(self.error)
        self.vbox.addWidget(self.back)
        self.setLayout(self.vbox)

    def BACK(self):
        self.goback_request.emit(3)
        
    def setImages(self, images, urls, titles):
        
        self.list_widget.clear()
        self.items = []
        
        for i in range(len(images)):
                self.items.append(ClickableThumbnail(urls[i]))
                self.items[i].setText(titles[i])
                self.list_widget.addItem(self.items[i])
                pm = QPixmap()
                pm.loadFromData(base64.b64decode(images[i]))
                ic = QIcon()
                ic.addPixmap(pm)
                if(ic.isNull() == False):
                    self.items[i].setIcon(ic)
                
        