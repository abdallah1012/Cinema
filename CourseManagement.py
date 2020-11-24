# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:20:27 2020

@author: ojaro
"""
import pandas as pd
from sqlalchemy import create_engine

class CourseManagement:
    def __init__(self):   
       
        #change localhost to IP address and root to username of database
        #This was tested using wampserver
        self.database_connection = create_engine('mysql+mysqlconnector://root@localhost/cinemadb?'.format('root', '', 'localhost', 'cinemadb'))
    
    def getCourses(self, userID):
        sqlstmt = "SELECT courseName, courseID FROM courses WHERE professorID = '"+str(userID)+"'"
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        
        if(len(df) > 0):
            return df
        else:
            return 0     
    
    def CheckForCourseUser(self, coursename, user):
        sqlstmt = "SELECT courseID FROM courses WHERE coursename = '"+str(coursename)+"' AND professorID = '"+str(user)+"'"
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        print(sqlstmt)
        if(len(df) > 0):
            return 1 
        else:
            return 0 
        
    
    def AddToCourses(self, CourseName, Sylabbus, user):
        
        #try later to encrypt password
        sqlstmt = "INSERT INTO courses (courseName, professorID, syllabus) VALUES ('"+str(CourseName)+"', '"+str(user)+"', '"+str(Sylabbus)+"');"
        
        try:
            self.database_connection.execute(sqlstmt)
            return 1
        except:
            return 0