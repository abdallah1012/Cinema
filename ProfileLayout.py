# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:42:30 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QGridLayout,QWidget,QLabel
class ProfileLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.__profile_grid = QGridLayout()
        self.temp_label = QLabel("Profile tab clicked")
        self.__profile_grid.addWidget(self.temp_label)
        self.setLayout(self.__profile_grid)