# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:42:30 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QGridLayout,QWidget,QLabel
from User import User
from ProfileController import ProfileController


#Layout for the profile interface
#TODO: show relevant details for the user
class ProfileLayout(QWidget):
    def __init__(self,user:User):
        super().__init__()
        self.__profile_grid = QGridLayout()
        self.__profile_grid.addWidget(QLabel("profile loaded - testing"))
        self.user = user
        self.controller = ProfileController(self.user)
        self.setLayout(self.__profile_grid)
        