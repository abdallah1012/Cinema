# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:50:27 2020

@author: WarPeace101
"""

import sys
from PyQt5.QtWidgets import QGridLayout,QPushButton,QLineEdit,QLabel, QWidget, QStackedLayout, QRadioButton, \
QFormLayout, QInputDialog
from PyQt5.QtWidgets import QApplication


class CourseInputDialog(QWidget):
   
   def __init__(self, parent = None):
      super(CourseInputDialog, self).__init__(parent)
		
      layout = QFormLayout()
#      self.btn = QPushButton("Choose from list")
#      self.btn.clicked.connect(self.getItem)
		
      self.le = QLineEdit()
#      layout.addRow(self.btn,self.le)
      self.btn1 = QLabel("Course Name")
#      self.btn1.clicked.connect(self.gettext)
		
      self.le1 = QLineEdit()
      layout.addRow(self.btn1,self.le1)
      self.btn2 = QLabel("Description")
#      self.btn2.clicked.connect(self.getint)
		
      
     
      self.le2 = QLineEdit()
      self.le2.setFixedWidth(300)
      self.le2.setFixedHeight(300)
      
      self.done = QPushButton("Done")
      
      layout.addRow(self.btn2,self.le2)
      layout.addRow(self.done)
      self.setLayout(layout)
      self.setWindowTitle("Add Course")
      
      
		
#   def getItem(self):
#      items = ("C", "C++", "Java", "Python")
#		
#      item, ok = QInputDialog.getItem(self, "select input dialog", 
#         "list of languages", items, 0, False)
#			
#      if ok and item:
#         self.le.setText(item)
#			
#   def gettext(self):
#      text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
#		
#      if ok:
#         self.le1.setText(str(text))
#			
#   def getint(self):
#      num,ok = QInputDialog.getInt(self,"integer input dualog","enter a number")
#		
#      if ok:
#         self.le2.setText(str(num))
         
#def main(): 
#   app = QApplication(sys.argv)
#   ex = CourseInputDialog()
#   ex.show()
#   sys.exit(app.exec_())
#	
#if __name__ == '__main__':
#   main()