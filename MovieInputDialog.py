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


class MovieInputDialog(QWidget):
   
   def __init__(self, courses, parent = None):
      super(MovieInputDialog, self).__init__(parent)

      self.courses = courses

      layout = QFormLayout()
      
      self.btn = QPushButton("Choose Course from list")
      self.btn.clicked.connect(self.getItem)	
      self.le = QLabel()
      layout.addRow(self.btn,self.le)
      
      
      self.btn1 = QLabel("Movie Name")
#      self.btn1.clicked.connect(self.gettext)
		
      self.le1 = QLineEdit()
      layout.addRow(self.btn1,self.le1)
      self.btn2 = QLabel("Description")
#      self.btn2.clicked.connect(self.getint)
		
      self.moviePath = ""
      self.thumbPath = ""
     
      self.le2 = QLineEdit()
      self.le2.setFixedWidth(300)
      self.le2.setFixedHeight(300)
      
      self.done = QPushButton("Done")
      
      
      
      layout.addRow(self.btn2,self.le2)
      
      self.Moviebtn = QPushButton("Browse")
      self.Moviebtn.clicked.connect(self.getMovie)
      self.movieLabel = QLabel("Choose your Movie")
      layout.addRow(self.Moviebtn, self.movieLabel)
      
      self.thumbbtn = QPushButton("Browse")
      self.thumbbtn.clicked.connect(self.getThumb)
      self.thumbLabel = QLabel("Choose your Thumbnail (Optional)")
      layout.addRow(self.thumbbtn, self.thumbLabel)
      
      layout.addRow(self.done)
      self.setLayout(layout)
      self.setWindowTitle("Add Movie")
      
      
      
      
		
   def getItem(self):
      item = []
      for i in self.courses:
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
