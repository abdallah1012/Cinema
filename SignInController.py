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

#Controller responsible for the communication of the relevant layout with other controllers
#or computation models
class SignInController:
    def __init__(self):
        self.Manager = UserManagement.UserManagement() #manager for communication with the user table
        self.course_manager = CourseManagement() #manager for communication with the course table
    
    #Attempts signing in by checking for username password combo (aa,aa username password is an exception for dev purposes)
    #params: string username, string password
    #if successfull it returns "success" for the layout to interpret
    def AttemptSignIn(self,username: str, password: str)->str:
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
        
    #responsible for opening the registration layout
    #returns "success" for the layout to interpret (closes the sign in layout)
    def ToRegister(self):
             register_window = RegisterLayout()
             return ("success")
    
    