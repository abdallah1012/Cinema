# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout,QLabel,QWidget,QPushButton, QVBoxLayout, QMainWindow, QStackedLayout, QListWidget,QListWidgetItem
import User
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtGui import QIcon, QPixmap
from ClickableThumbnail import ClickableThumbnail
from MovieManagement import MovieManagement
import base64 
from CourseMovieController import CourseMovieController
from Student import Student
from Professor import Professor
class CourseMovieLayout(QWidget):
    goback_request = pyqtSignal(int)
    new_movie_request = pyqtSignal(int)
    _WatchMovie_ = pyqtSignal(str, int)
    def __init__(self,user:User, courseID):
        super().__init__()
        self.list_widget = QListWidget()
        self.user = user
        self.courseID = courseID
        self.controller = CourseMovieController(self.user)
#        self.list_widget.setFlow(QListView.LeftToRight) 
        self.list_widget.setIconSize(QSize(190, 190))
        self.list_widget.hasAutoScroll()
        
        self.list_widget.setAutoFillBackground( False )
        self.items_title = self.user.courses
        self.Manager= MovieManagement()
   
        self.error = QLabel()
            
        
        

        self.movies = self.controller.getCMovies(self.courseID)
        self.titles = []
        self.thumbnails = []
        self.urls = []
        self.movieIDs = []
        if(len(self.movies) != 0):
            for i, j, k, w in self.movies:
                self.titles.append(i)
                self.thumbnails.append(j)
                self.urls.append(k)
                self.movieIDs.append(w)
            self.setImages(self.thumbnails, self.urls, self.titles, self.movieIDs)    
        else:
            self.error.setText("Course Has No Movies")
           
        self.back = QPushButton("Back")
        self.back.clicked.connect(lambda: self.BACK())
        self.vbox = QVBoxLayout()
        
        self.vbox.addWidget(self.list_widget)
        
        self.vbox.addWidget(self.error)
        self.vbox.addWidget(self.back)
       
        if(isinstance(self.user, Professor) == True):
            self.add_movie = QPushButton("Add Movie")
            self.add_movie.clicked.connect(lambda:self.new_movie_request.emit(self.courseID))
            self.vbox.addWidget(self.add_movie)
            
        self.setLayout(self.vbox)
        
        
        
        self.list_widget.itemPressed.connect(lambda: self.MovieIsClicked())
        

    def MovieIsClicked(self):
        self._WatchMovie_.emit(self.list_widget.selectedItems()[0].url, self.list_widget.selectedItems()[0].movieID)
        
    def BACK(self):
        self.goback_request.emit(3)
        
    def setImages(self, images, urls, titles, movieIDs):
        
        self.list_widget.clear()
        self.items = []
        
        for i in range(len(images)):
                self.items.append(ClickableThumbnail(urls[i], movieIDs[i]))
                self.items[i].setText(titles[i])
                self.list_widget.addItem(self.items[i])
                pm = QPixmap()
                pm.loadFromData(base64.b64decode(images[i]))
                ic = QIcon()
                ic.addPixmap(pm)
                if(ic.isNull() == False):
                    self.items[i].setIcon(ic)
                
        