# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QGridLayout,QPushButton,QLineEdit,QLabel, QWidget, QStackedLayout, QRadioButton, \
QFormLayout, QInputDialog, QFileDialog
from PyQt5.QtWidgets import QApplication
from User import User
from MovieInputController import MovieInputController
from PyQt5.QtCore import pyqtSignal

#layout class for visual interface responsible for showing the user the appropriate items
#to add a movie to the database and enter his input
class MovieInputDialog(QWidget):
   goback_request = pyqtSignal(int)
   
   def __init__(self, user:User, courseID, parent = None):
      super(MovieInputDialog, self).__init__(parent)

      self.user = user

      layout = QFormLayout()
      self.courseID = courseID
#      self.btn = QPushButton("Choose Course from list")
#      self.btn.clicked.connect(self.getItem)	
#      self.le = QLabel()
#      layout.addRow(self.btn,self.le)
      
      
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
      
      self.tag1_ind = QLabel("First Tag")
      self.tag2_ind = QLabel("Second Tag")
      self.tag3_ind = QLabel("Third Tag")
      self.style_ind = QLabel("Style")
      
      self.tag1 = QLineEdit()
      self.tag2 = QLineEdit()
      self.tag3 = QLineEdit()
      self.style = QLineEdit()
      
      
      
     
      
      layout.addRow(self.tag1_ind, self.tag1)
      layout.addRow(self.tag2_ind, self.tag2)
      layout.addRow(self.tag3_ind, self.tag3)
      layout.addRow(self.style_ind, self.style)
      layout.addRow(self.cancel, self.done)
      
      layout.addRow(self.errorText)
      
      self.setLayout(layout)
      self.setWindowTitle("Add Movie")

      self.controller = MovieInputController()
 
    #submits movie details to controller to handle adding it to the database and uses output to 
    #show appropriate error message
   def submitMovie(self):
        courseID = self.courseID
#        print(courseName)
#        for i in self.user.courses:       
#            if (str(i[0]) == str(courseName)):
#                courseID = i[1]
#                break
        #self.movieproperties index 0 is the url path and 1 is the thumbnail path
        result = self.controller.addMovie(self.le1.text(), courseID,  self.le2.text(), self.user.id, self.movieLabel.text(), self.thumbLabel.text(), self.tag1.text(), self.tag2.text(), self.tag3.text(), self.style.text())
        
        if(result == 1):
            self.goback_request.emit(self.courseID)
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
       self.goback_request.emit(self.courseID)
      
      
    #gets courses that the professor gives, since movies are under courses
    #adds movies to class member "item"
#   def getItem(self):
#      item = []
#      for i in self.user.courses:
#          item.append(i[0])
#      item, ok = QInputDialog.getItem(self, "Select Course", "List of Courses You Give: ", item, 0, False)
#			
#      if ok and item:
#         self.le.setText(item)

    #asks user to locate thumbnail they want to use from their device and saves the path
   def getThumb(self):
       self.thumbPath = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image Files (*.gif *.png *.jpg)")
       self.thumbLabel.setText(self.thumbPath[0])
       
     #asks user to locate movies they want to use from their device and saves the path       
   def getMovie(self):
        self.moviePath = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Video files (*.avi *.mp4 *.flv)")
        self.movieLabel.setText(self.moviePath[0])
