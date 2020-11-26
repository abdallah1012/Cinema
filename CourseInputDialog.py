# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:50:27 2020

@author: WarPeace101
"""


from PyQt5.QtWidgets import QGridLayout,QPushButton,QLineEdit,QLabel, QWidget, QStackedLayout, QRadioButton, \
QFormLayout, QInputDialog
from User import User
from PyQt5.QtCore import pyqtSignal
from CourseInputController import CourseInputController

class CourseInputDialog(QWidget):
   loaddashlayout = pyqtSignal(int)
   
   def __init__(self, user:User ,parent = None):
      super(CourseInputDialog, self).__init__(parent)
      
      self.user = user
      
      layout = QFormLayout()
		
      self.le = QLineEdit()

      self.btn1 = QLabel("Course Name")

		
      self.le1 = QLineEdit()
      layout.addRow(self.btn1,self.le1)
      self.btn2 = QLabel("Description")
  
      self.le2 = QLineEdit()
      self.le2.setFixedWidth(300)
      self.le2.setFixedHeight(300)
      
      self.done = QPushButton("Done")
      self.done.clicked.connect(lambda:self.SubmitCourse())
      
      self.cancel = QPushButton("Cancel")
      self.cancel.clicked.connect(lambda: self.goBack())
      
      layout.addRow(self.btn2,self.le2)
      layout.addRow(self.cancel, self.done)
      self.setLayout(layout)
      self.setWindowTitle("Add Course")
      
      self.errorText = QLabel("")
      layout.addRow(self.errorText)
      
      self.controller = CourseInputController()
      
   def SubmitCourse(self):
       result = self.controller.addCourse(self.le1.text(), self.le2.text(), self.user.id)
       if(result == 1):
#            self.errorText.setText("Course Added Successfully")
            self.loaddashlayout.emit(1)
       elif(result == 0):
            self.errorText.setText("Database Error")
       elif(result == 2):
            self.errorText.setText("Course Already Added Before")
       elif(result == 3):
            self.errorText.setText("Youtube Error")
       else:
            self.errorText.setText("Unknown Error") 
       

   def goBack(self):
       self.loaddashlayout.emit(0)