# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:02:46 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QWidget
from User import UserPrivilege

class MainWindow(QWidget):
    def __init__(self,privilege: UserPrivilege):
        super().__init__()
        self.setWindowTitle('Main Window')
        if privilege==UserPrivilege.STUDENT:
            self.LoadStudentMenu()
        else:
            self.LoadProfMenu()

        self.show()
        
    def LoadStudentMenu(self):
        print("Student menu")
    def LoadProfMenu():
        print("Professor menu")
        