# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:50:27 2020

@author: WarPeace101
"""
import sys
from PyQt5.QtWidgets import QGridLayout,QPushButton,QLineEdit,QLabel, QWidget, QStackedLayout, QRadioButton, \
QFormLayout, QInputDialog, QFileDialog
from PyQt5.QtWidgets import QApplication
from User import User
from MovieInputController import MovieInputController
from PyQt5.QtCore import pyqtSignal

class MovieInputDialog(QWidget):
   loaddashlayout = pyqtSignal(int)
   
   def __init__(self, user:User, parent = None):
      super(MovieInputDialog, self).__init__(parent)

      self.user = user

      layout = QFormLayout()
      
      self.btn = QPushButton("Choose Course from list")
      self.btn.clicked.connect(self.getItem)	
      self.le = QLabel()
      layout.addRow(self.btn,self.le)
      
      
      self.btn1 = QLabel("Movie Name")	
      self.le1 = QLineEdit()
      self.le1.setFixedWidth(250)
      layout.addRow(self.btn1,self.le1)
      self.btn2 = QLabel("Description")

		
      self.moviePath = ""
      self.thumbPath = ""
     
      self.le2 = QLineEdit()
      self.le2.setFixedWidth(250)
      self.le2.setFixedHeight(200)
      
      self.done = QPushButton("Done")
      self.done.clicked.connect(lambda: self.submitMovie())
      
      self.cancel = QPushButton("Cancel")
      self.cancel.clicked.connect(lambda: self.goBack())
      
      layout.addRow(self.btn2,self.le2)
      
      self.Moviebtn = QPushButton("Browse")
      self.Moviebtn.clicked.connect(self.getMovie)
      self.movieLabel = QLabel("Choose your Movie")
      layout.addRow(self.Moviebtn, self.movieLabel)
      
      self.thumbbtn = QPushButton("Browse")
      self.thumbbtn.clicked.connect(self.getThumb)
      self.thumbLabel = QLabel("Choose your Thumbnail (Optional)")
      layout.addRow(self.thumbbtn, self.thumbLabel)
      
      self.errorText = QLabel("")
      
      
      layout.addRow(self.cancel, self.done)
      
      layout.addRow(self.errorText)
      
      self.setLayout(layout)
      self.setWindowTitle("Add Movie")

      self.controller = MovieInputController()
      
   def submitMovie(self):
        courseName = self.le.text()
        courseID = ""
        print(courseName)
        for i in self.user.courses:       
            if (str(i[0]) == str(courseName)):
                courseID = i[1]
                break
        #self.movieproperties index 0 is the url path and 1 is the thumbnail path
        result = self.controller.addMovie(self.le1.text(), courseID,  self.le2.text(), self.user.id, 
                                               self.movieLabel.text(), self.thumbLabel.text())
        
        if(result == 1):
            self.loaddashlayout.emit(2)
        elif(result == 0):
            self.errorText.setText("Database Error")
        elif(result == 2):
            self.errorText.setText("Movie Already Added Before")
        elif(result == 3):
            self.errorText.setText("Can't read Movie or Youtube Error")
        elif(result == 4):
            self.errorText.setText("Can't Read thumbnail")
        else:
            self.errorText.setText("Unknown Error") 
        
   
   def goBack(self):
       self.loaddashlayout.emit(0)
      
      
		
   def getItem(self):
      item = []
      for i in self.user.courses:
          item.append(i[0])
      item, ok = QInputDialog.getItem(self, "Select Course", "List of Courses You Give: ", item, 0, False)
			
      if ok and item:
         self.le.setText(item)

   def getThumb(self):
       self.thumbPath = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image Files (*.gif *.png *.jpg)")
       self.thumbLabel.setText(self.thumbPath[0])
       
   def getMovie(self):
        self.moviePath = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Video files (*.avi *.mp4 *.flv)")
        self.movieLabel.setText(self.moviePath[0])
