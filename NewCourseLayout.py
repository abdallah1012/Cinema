# -*- coding: utf-8 -*-


from NewCourseController import NewCourseController
from PyQt5.QtWidgets import QWidget, QGridLayout,QLabel

#Create Course Layout
#TODO: NO LONGER IN USE
class NewCourseLayout(QWidget):
    def __init__(self,user_id:int):
        super().__init__()
        self.__new_course_grid = QGridLayout()
        self.__new_course_grid.addWidget(QLabel("Requesting to enroll/create course - testing"),1,1)
        self.setLayout(self.__new_course_grid)
        #TODO: check if user is student or professor
        # professor creates a course
        # student enrolls in a course
        # invoke corresponding controller function
        controller = NewCourseController(user_id)