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
        
    
    def CheckForCourseUser(self, coursename, user):
        sqlstmt = "SELECT entity FROM courses WHERE coursename = '"+str(coursename)+"' AND user = '"+str(user)+"'"
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        if(len(df) > 0):
            return 1 , df[0][0]
        else:
            return 0 , ''
        
    
    def AddToCourses(self, CourseName, PreRequisites, Sylabbus, user):
        
        #try later to encrypt password
        sqlstmt = "INSERT INTO courses VALUES ('"+str(CourseName)+"', '"+str(PreRequisites)+"', '"+str(Sylabbus)+"', '"+str(user)+"');"
        try:
            self.database_connection.execute(sqlstmt)
            return 1
        except:
            return 0