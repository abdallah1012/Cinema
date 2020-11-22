# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:21:54 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QWidget,QGridLayout,QLabel
from CourseController import CourseController

class CourseLayout(QWidget):
    def __init__(self, course_id: int):
        super().__init__()
        self.controller = CourseController()
        #TODO: populate GUI with controller results
        self.__course_grid = QGridLayout()
        self.__course_grid.addWidget(QLabel("course loaded -testing"))
        self.setLayout(self.__course_grid)
    