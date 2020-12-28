# -*- coding: utf-8 -*-


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
        Moviess = self.moviemanager.getWhatHot()
       
        Moviess = [i[0] for i in Moviess]
        
        return Moviess
            
        
    #TODO:  Send query to MMS to retrieve list of "hottest" movies.
    #       Criteria can be highest number of views and highest ratings (TBD)
    
    def LoadRecommendations(self,user: User):
        Courses=user.courses
        
        tags=[]
        faculty = []
        typ=[]
        cids=[]
        if(isinstance(Courses, int)==True):
            Courses = []
        for i,j in Courses:
            
            temp=self.manager.getCourseinfo(str(j))
            Movies=self.moviemanager.getCourseMovieID(str(j))
            if(len(Movies)!=0):
                for k in range(len(Movies)):
                    tags.append(Movies[k][1])
                    tags.append(Movies[k][2])
                    tags.append(Movies[k][3])
          
            if(len(temp)!=0):
                cids.append(temp[0][0])
                faculty.append(temp[0][1])
                typ.append(temp[0][2])
        

        faculty=list(set(faculty))
        if(len(faculty)!=0):
            typ=list(set(typ))
         
            courseIDs=[]
            
            Movierecommend=[]
            for i in typ:
                
                tem = (self.manager.getRecommendedCourses(i))
                print("hree", tem)
                for j in range(len(tem)):
                    if((tem[j][0] in cids)==False):
                        courseIDs.append(tem[j][0])
            
            for i in courseIDs:        
               recommend=self.moviemanager.getCourseMovieID(i)
               
               if(len(recommend)!=0):
                   
                   for k in range(len(recommend)):
                       if((recommend[k][1] in tags)==True or (recommend[k][2] in tags) == True or (recommend[k][3])==True ):
                           Movierecommend.append(recommend[k][0])
                   if(len(Movierecommend)==0):
                       Movierecommend=[ids for ids, tag1, tag2, tag3 in recommend]
               else:
                   return self.WhatsHot()
            
            return Movierecommend
                    
        else:
            return self.WhatsHot()
            
                    
        
    #TODO:  Send query to MMS to retrieve list of "Recommended" movies for currently signed in user
    