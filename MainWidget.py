# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QStackedLayout, QHBoxLayout, QFrame, QMainWindow, QAction, QMessageBox
from User import User
from HomeLayout import HomeLayout
from DashboardLayout import DashboardLayout
from ProfileLayout import ProfileLayout
from MovieLayout import MovieLayout
from CourseInputDialog import CourseInputDialog
from MovieInputDialog import MovieInputDialog
from CourseMovieLayout import CourseMovieLayout
from ChangePasswordLayout import ChangePasswordLayout
from Student import Student
from Professor import Professor
from MainWidgetController import MainWidgetController
#Main widget/window used to show all layouts that represent the visual interface that the user will face throughout runtime
class MainWidget(QMainWindow):
    
    def __init__(self, user:User):
        super().__init__()
        
        self.mainWidget = QWidget()
        
        
        
        self.setMinimumSize(500,500)
        self.user = user
        self.controller = MainWidgetController(self.user)
        self.setStyleSheet(open('main.css').read())
        self.dashboard_button = QPushButton("Dashboard")
        self.dashboard_button.setFixedWidth(150)
        self.dashboard_button.clicked.connect(lambda success:self.LoadDashboardLayout(success))
        self.dashboard_button.setObjectName("dashboard_button")
        
        self.home_button = QPushButton("Home")
        self.home_button.setFixedWidth(150)
        self.home_button.clicked.connect(lambda:self.LoadHomeLayout())
        self.home_button.setObjectName("home_button")
        
        self.profile_button = QPushButton("Profile")
        self.profile_button.setFixedWidth(150)
        self.profile_button.clicked.connect(lambda success:self.LoadProfileLayout(success))
        self.profile_button.setObjectName("profile_button")
                
        
        self.grid = QGridLayout()

        #self.topbar = QFrame()
        self.upperLayout = QHBoxLayout()
        
        self.upperLayout.addWidget(self.dashboard_button)
        self.upperLayout.addWidget(self.home_button)
        self.upperLayout.addWidget(self.profile_button)
        
        self.upperExternal = QFrame()    
        self.upperExternal.setLayout(self.upperLayout)
        
       #print(self.user.courses)
       
        self.home_layout = None
        self.dashboard_layout = None
        self.profile_layout = None
        self.course_layout = None
        self.new_course_layout = None
        self.movie_layout = None
        self.addmovie_layout = None
        self.CourseMovies_layout = None
        self.changepass_layout = None
        
        self.stack = QStackedLayout()
        
        self.grid.addWidget(self.upperExternal,1,1)
        self.grid.addLayout(self.stack,2,1)
        
        self.mainWidget.setLayout(self.grid)
        self.setCentralWidget(self.mainWidget)
        self.LoadHomeLayout()
#        self.Recommender=RecommendationEngine()
#        self.Recommender.LoadRecommendations(self.user)
        exit = QAction("&Exit", self)
        exit.triggered.connect(self.closeEvent)
        
        
        self.show()
    
    def closeEvent(self, event):
        
        self.silence()
        close = QMessageBox()
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        
        if close == QMessageBox.Yes:        
            event.accept()
        else:
            event.ignore()
    
    
    #HomeLayoout----------------------------------------------------------------------------------
    #Sets homelayout as default layout
    def LoadHomeLayout(self):
        self.setWindowTitle("Home")
        if self.home_layout == None:
            self.home_layout = HomeLayout(self.user)
            self.home_layout._WatchMovie_.connect(lambda url, M_ID:self.LoadMovieLayout(url, M_ID))
            self.stack.addWidget(self.home_layout)
        self.stack.setCurrentWidget(self.home_layout)
        self.silence()
    
    #sets movielayout as default layout
    def LoadMovieLayout(self, url, movieID):
        self.setWindowTitle("Movie")
        if self.movie_layout!=None:
            self.stack.removeWidget(self.movie_layout)
            del self.movie_layout
            
        self.movie_layout = MovieLayout(url, movieID, self.user)
        self.stack.addWidget(self.movie_layout)
        self.stack.setCurrentWidget(self.movie_layout) 
 
    
    
    

    #DashBoardLayout----------------------------------------------------------------------------------
    #sets dashboard layout as default layout
    def LoadDashboardLayout(self, success):
        if self.dashboard_layout!=None:
            self.stack.removeWidget(self.dashboard_layout)
            del self.dashboard_layout
       
        self.setWindowTitle("Dashboard")
        
        self.dashboard_layout = DashboardLayout(self.user)
        self.dashboard_layout.new_course_request.connect(self.LoadCourseLayout)
        
        self.dashboard_layout.openCourse_request.connect(lambda x: self.LoadCourseMovies(x))
        self.stack.addWidget(self.dashboard_layout)
            
        self.stack.setCurrentWidget(self.dashboard_layout)
        self.silence()
        
        if(success == 1):
            self.dashboard_layout.message.setText("Successfully Submitted Course")
            self.course_layout = None
        elif(success == 2):
            self.dashboard_layout.message.setText("Successfully Submitted Movie")
            self.addmovie_layout = None
        elif(success == 3):
            pass
        elif(success == 4):
            self.dashboard_layout.message.setText("Successfully Enrolled in Course")
            self.course_layout = None
    
    #sets course layout as default layout (upload courses)
    def LoadCourseLayout(self):
        self.setWindowTitle("Add Course")
        if self.course_layout == None and isinstance(self.user, Professor) == True:
            self.course_layout = CourseInputDialog(self.user)
            self.course_layout.loaddashlayout.connect(lambda success:self.LoadDashboardLayout(success)) 
            
            self.stack.addWidget(self.course_layout)
        elif self.course_layout == None and isinstance(self.user, Student) == True:
            self.course_layout = CourseInputDialog(self.user)
            self.course_layout.loaddashlayout.connect(lambda success:self.LoadDashboardLayout(success))       
            self.stack.addWidget(self.course_layout)
#        self.course_layout.refreshDash.connect(self.)
        self.course_layout.refreshCourses_request.connect(self.RefreshProfile)
        self.stack.setCurrentWidget(self.course_layout)
    
    #sets dash movie layout as default layout (upload movie)
    def LoadDashMovieLayout(self, courseID):
        self.setWindowTitle("Add Movie")
        if self.addmovie_layout!=None:
            self.stack.removeWidget(self.addmovie_layout)
            del self.addmovie_layout
               
        self.addmovie_layout = MovieInputDialog(self.user, courseID)
        self.addmovie_layout.goback_request.connect(lambda C_ID:self.LoadCourseMovies(C_ID))
        self.stack.addWidget(self.addmovie_layout)
        self.stack.setCurrentWidget(self.addmovie_layout)
    
    def LoadCourseMovies(self, courseID):
        self.setWindowTitle("Course Movies")
        if self.CourseMovies_layout!=None:
            self.stack.removeWidget(self.CourseMovies_layout)
            del self.CourseMovies_layout
        self.CourseMovies_layout = CourseMovieLayout(self.user, courseID)
        self.CourseMovies_layout.new_movie_request.connect(lambda C_ID: self.LoadDashMovieLayout(C_ID))
        self.CourseMovies_layout.goback_request.connect(lambda success:self.LoadDashboardLayout(success))
        self.CourseMovies_layout._WatchMovie_.connect(lambda url, M_ID:self.LoadMovieLayout(url, M_ID))
        self.stack.addWidget(self.CourseMovies_layout)
            
        self.stack.setCurrentWidget(self.CourseMovies_layout)

 
    
    
    #ProfileLayout---------------------------------------------------------------------------------------------
    #sets profile layout as default layout
    def LoadProfileLayout(self, success):
        self.setWindowTitle("Profile")
        if self.profile_layout != None:
            self.stack.removeWidget(self.profile_layout)
            del self.profile_layout
            
        self.profile_layout = ProfileLayout(self.user)
        self.profile_layout.changePass_request.connect(lambda : self.LoadChangePassLayout())
        self.profile_layout.changeImage_request.connect(lambda image: self.ChangeImage(image))
        if(success == 1):
            self.profile_layout.errorMessage.setText("Password Changed Successfully")
        
        
        self.stack.addWidget(self.profile_layout)
        self.stack.setCurrentWidget(self.profile_layout)
        self.silence()
        
    def LoadChangePassLayout(self):
        self.setWindowTitle("Change Password")
        if self.changepass_layout == None:
            self.changepass_layout = ChangePasswordLayout(self.user)
            self.changepass_layout.goback_request.connect(lambda success:self.LoadProfileLayout(success))    
            self.stack.addWidget(self.changepass_layout)
            
        self.stack.setCurrentWidget(self.changepass_layout)

    #-----------------------------------------------------------------------------------------------------------
    #stops movie from running in background (movie cleanup)
    def silence(self):
        if(self.movie_layout != None):
            self.movie_layout.Stop()
            
    def RefreshProfile(self):
        self.user.courses = self.controller.refresh()
        
        
    def ChangeImage(self, image):
        self.user.courses = image
        
        

        