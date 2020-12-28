# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QWidget,QGridLayout,QLabel
from CourseController import CourseController

#course layout used to show relevant interfaces for user to view courses or add courses
#currently not being used
class CourseLayout(QWidget):
    def __init__(self, course_id: int):
        super().__init__()
        self.controller = CourseController()
        #TODO: populate GUI with controller results
        self.__course_grid = QGridLayout()
        self.__course_grid.addWidget(QLabel("course loaded -testing"))
        self.setLayout(self.__course_grid)
    