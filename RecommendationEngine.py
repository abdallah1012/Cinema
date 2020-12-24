# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:20:06 2020

@author: ojaro
"""

#Recommendation model used to find which movies should be recommended to the user
#and what movies are generally good --> "hot"
import User
from CourseManagement import CourseManagement
from MovieManagement import MovieManagement
class RecommendationEngine:
    
    
    def __init__(self):
        self.manager = CourseManagement()
        self.moviemanager = MovieManagement()
    
    def WhatsHot(self):
        pass
    #TODO:  Send query to MMS to retrieve list of "hottest" movies.
    #       Criteria can be highest number of views and highest ratings (TBD)
    
    def LoadRecommendations(self,user: User):
        Courses=user.courses
        faculty = []
        typ=[]
        cids=[]
        for i,j in Courses:
            
            temp=self.manager.getCourseinfo(str(j))
          
            if(len(temp)!=0):
                cids.append(temp[0][0])
                faculty.append(temp[0][1])
                typ.append(temp[0][2])
        

        faculty=list(set(faculty))
        if(len(faculty)!=0):
            typ=list(set(typ))
            print("hereis typ")
            print(typ)
            courseIDs=[]
            
            recommend=[]
            for i in typ:
                
                tem = (self.manager.getRecommendedCourses(i))
                print("tem")
                print(tem)
                for j in range(len(tem)):
                    if((tem[j][0] in cids)==False):
                        courseIDs.append(tem[j][0])
            print("courseids")
            print(courseIDs)
            for i in courseIDs:        
               recommend.append(self.moviemanager.getCourseMovieID(i))
            print(recommend)
            
        else:
            #reccommend randomly
            pass
                    
        
    #TODO:  Send query to MMS to retrieve list of "Recommended" movies for currently signed in user
    