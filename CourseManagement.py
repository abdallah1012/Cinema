# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:20:27 2020

@author: ojaro
"""
import pandas as pd
from sqlalchemy import create_engine

#computation model
class CourseManagement:
    def __init__(self):   
       
        #change localhost to IP address and root to username of database
        #This was tested using wampserver
        self.database_connection = create_engine('mysql+mysqlconnector://root@localhost/cinemadb?'.format('root', '', 'localhost', 'cinemadb'))
    
    #gets all courses from database for specific professor
    #params: int userID
    #returns coursename and courseID in a list if successfull and 0 if failed
    def getCourses(self, userID):
        sqlstmt = "SELECT courseName, courseID FROM courses WHERE professorID = '"+str(userID)+"'"
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        
        if(len(df) > 0):
            return df
        else:
            return 0     
    
    #checks if user is giving this course (currently)
    #TODO: modify or do another function that checks if student is enrolled in course, same syntax, different table or change table attribute
    #params: string coursename, int user
    #returns 1 if found and 0 if not
    def CheckForCourseUser(self, coursename, user):
        sqlstmt = "SELECT courseID FROM courses WHERE coursename = '"+str(coursename)+"' AND professorID = '"+str(user)+"'"
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        #print(sqlstmt)
        if(len(df) > 0):
            return 1 
        else:
            return 0 
        
    #adds course to database under user's ID
    #params: string CourseName, string Syllabus, int user
    #returns 1 on successfull execution and 0 if failed
    def AddToCourses(self, CourseName, Sylabbus, user, faculty, typeofCourse):
        
        #try later to encrypt password
        sqlstmt = "INSERT INTO courses (courseName, professorID, syllabus, faculty, type) VALUES ('"+str(CourseName)+"', '"+str(user)+"', '"+str(Sylabbus)+"', '"+str(faculty)+"', '"+str(typeofCourse)+"');"
        
        try:
            self.database_connection.execute(sqlstmt)
            return 1
        except:
            return 0