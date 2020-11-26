# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:54:51 2020

@author: ojaro
"""
from MainWidget import MainWidget
from Student import Student 
from Professor import Professor
from RegisterLayout import RegisterLayout
import UserManagement
from CourseManagement import CourseManagement

class SignInController:
    def __init__(self):
        self.Manager = UserManagement.UserManagement() #lazy init
        self.course_manager = CourseManagement()
    def AttemptSignIn(self,username: str, password: str)->str:
        #this is for dev reasons
        if(username == "aa" and password == "aa"):
            courses = []
            try:
                courses = self.course_manager.getCourses(0)
            except:
                pass
            
            user = Professor(0,courses)
            
            main_window = MainWidget(user)
            return "success"
        if (username=="" or password==""):
            return ("Error empty field(s)")
        else:
            model_result, entity, userID = self.Manager.CheckForUserPass(username, password)
            if(model_result == 1):
                courses = []
                try:
                    courses = self.course_manager.getCourses(userID)
                except:
                    return ("Database down, use aa")
            
                if(entity == 'student'):
                    user = Student(userID, courses)
                elif(entity == 'professor'):
                    user = Professor(userID, courses)
                

                main_window = MainWidget(user)
                return "success"
            else:
                return ("Username or Password Incorrect")
        
    def ToRegister(self):
             register_window = RegisterLayout()
             return ("success")
    
    