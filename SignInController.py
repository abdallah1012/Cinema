# -*- coding: utf-8 -*-

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
            
            userInfo = self.Manager.getUserInfo(0)
            
            if(len(userInfo[0][3]) != 0):
                user = Professor(0, courses, userInfo[0][1], userInfo[0][2], userInfo[0][0], userInfo[0][3])
            else:
                user = Professor(0, courses, userInfo[0][1], userInfo[0][2], userInfo[0][0], [])
                
            main_window = MainWidget(user)
            return "success"
        if (username=="" or password==""):
            return ("Error empty field(s)")
        else:
            model_result, entity, userID = self.Manager.CheckForUserPass(username, password)
            if(model_result == 1):
                courses = []
                try:
                    if(entity == "professor"):
                        courses = self.course_manager.getCourses(userID)
                    elif(entity == "student"):
                        courses = self.course_manager.getCoursesStudent(userID)
                except:
                    return ("Database down, use aa")
                
                userInfo = self.Manager.getUserInfo(userID)
                
				
                if((userInfo[0][3]) != None):
                    if(entity == 'student'):
                        user = Student(userID, courses, userInfo[0][1], userInfo[0][2], userInfo[0][0], userInfo[0][3])
                    elif(entity == 'professor'):
                        user = Professor(userID, courses, userInfo[0][1], userInfo[0][2], userInfo[0][0], userInfo[0][3])
                else:
                    if(entity == 'student'):
                        user = Student(userID, courses, userInfo[0][1], userInfo[0][2], userInfo[0][0], [])
                    elif(entity == 'professor'):
                        user = Professor(userID, courses, userInfo[0][1], userInfo[0][2], userInfo[0][0], [])

                main_window = MainWidget(user)
                return "success"
            else:
                return ("Username or Password Incorrect")
        
    #responsible for opening the registration layout
    #returns "success" for the layout to interpret (closes the sign in layout)
    def ToRegister(self):
             register_window = RegisterLayout()
             return ("success")
    
    