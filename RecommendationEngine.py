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
        tags=[]
        faculty = []
        typ=[]
        cids=[]
        for i,j in Courses:
            
            temp=self.manager.getCourseinfo(str(j))
            Movies=self.moviemanager.getCourseMovieID(str(j))
            if(len(Movies)!=0):
                tags.append(Movies[0][1])
                tags.append(Movies[0][2])
                tags.append(Movies[0][3])
          
            if(len(temp)!=0):
                cids.append(temp[0][0])
                faculty.append(temp[0][1])
                typ.append(temp[0][2])
        

        faculty=list(set(faculty))
        if(len(faculty)!=0):
            typ=list(set(typ))
         
            courseIDs=[]
            Rtags=[]
            Movierecommend=[]
            for i in typ:
                
                tem = (self.manager.getRecommendedCourses(i))
                
                for j in range(len(tem)):
                    if((tem[j][0] in cids)==False):
                        courseIDs.append(tem[j][0])
      
            for i in courseIDs:        
               recommend=self.moviemanager.getCourseMovieID(i)
               if(len(recommend)!=0):
                   Rtags.append(recommend[0][1])
                   Rtags.append(recommend[0][2])
                   Rtags.append(recommend[0][3])
                   for k in range(len(recommend)):
                       if((Rtags[k] in tags)==True):
                           Movierecommend.append(recommend[0][0])
                   if(len(Movierecommend)==0):
                       Movierecommend=recommend
        else:
            #reccommend randomly
            pass
                    
        
    #TODO:  Send query to MMS to retrieve list of "Recommended" movies for currently signed in user
    