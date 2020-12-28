# -*- coding: utf-8 -*-



from PyQt5.QtWidgets import QPushButton,QLineEdit,QLabel, QWidget, QFormLayout, QInputDialog, QComboBox, QVBoxLayout
from User import User
from PyQt5.QtCore import pyqtSignal
from CourseInputController import CourseInputController
from Student import Student
from Professor import Professor
#layout used to show user interface to add input for and submit a course to be added to the database
class CourseInputDialog(QWidget):
   loaddashlayout = pyqtSignal(int)
   refreshCourses_request =pyqtSignal()
   
   def __init__(self, user:User ,parent = None):
      super(CourseInputDialog, self).__init__(parent)
      self.controller = CourseInputController()
      self.user = user
      if(isinstance(user, Professor) == True):
          self.StartProf()
      elif(isinstance(user, Student) == True):
          self.StartStud()
      

#*****************************************************************************************************
      
   def StartStud(self):
      
      self.setWindowTitle("Enroll in a Course")
      layout = QVBoxLayout()
      self.cb = QComboBox()
      self.cb_courses = QComboBox()
      self.enroll_button = QPushButton("Enroll In Course")
      self.enroll_button.clicked.connect(lambda: self.enrollStudent())
      self.error_message = QLabel("")
                        
      self.info = self.controller.getAllCourses()
      self.item = []
      
      for courseID, faculty, courseName in self.info:
          if((str(faculty) in self.item) == False):
              self.cb.addItem(str(faculty))
              self.item.append(faculty)
          
      self.courses = self.controller.getCoursePerFaculty(self.cb.currentText())
      self.cb_courses.clear()
      self.courseIDs = []
      for courseIds, coursenames in self.courses:
          self.cb_courses.addItem(coursenames)
          self.courseIDs.append(courseIds)
          
      self.cb.currentIndexChanged.connect(self.selectionchange)
      self.cb_courses.currentIndexChanged.connect(self.selectionchangeCourses)
      layout.addWidget(self.cb)
      layout.addWidget(self.cb_courses)
      layout.addWidget(self.enroll_button)
      layout.addWidget(self.error_message)
      
      self.cb.setStyleSheet("QComboBox { background-color: white; }");
      self.cb_courses.setStyleSheet("QComboBox { background-color: white; }");
      self.setLayout(layout)
      

   def selectionchange(self,i):    
      for count in range(self.cb.count()):
         self.cb.itemText(count)
      
      self.courses = self.controller.getCoursePerFaculty(self.cb.currentText())
      self.cb_courses.clear()
      self.courseIDs = []
      for courseIds, coursenames in self.courses:
          self.cb_courses.addItem(coursenames)
          self.courseIDs.append(courseIds)
     
   def selectionchangeCourses(self, i):
       
       for count in range(self.cb_courses.count()):
         self.cb_courses.itemText(count)

   def enrollStudent(self):
       courseID = self.courseIDs[self.cb_courses.currentIndex()]
       result = self.controller.EnrollStudent(courseID, self.user.id, self.cb_courses.currentText())
       if(result == 0):
           self.error_message.setText("Database error Enrolling in course")
       elif(result == 1):
           
           self.refreshCourses_request.emit()
           self.loaddashlayout.emit(4)
           
        
        
#Student 
#*******************************************************************************************************
#Professor      
           
           
   def StartProf(self):
      
      
      self.layout = QFormLayout()
		
      self.le = QLineEdit()

      self.btn1 = QLabel("Course Name")

		
      self.le1 = QLineEdit()
      self.layout.addRow(self.btn1,self.le1)
      self.btn2 = QLabel("Description")
  
      self.le2 = QLineEdit()
      self.le2.setFixedWidth(300)
      self.le2.setFixedHeight(300)
      
      self.done = QPushButton("Done")
      self.done.clicked.connect(lambda:self.SubmitCourse())
      
      self.cancel = QPushButton("Cancel")
      self.cancel.clicked.connect(lambda: self.goBack())
      
      self.layout.addRow(self.btn2,self.le2)
      
      
      
      self.facultyIndicator = QLabel("Faculty")
      self.faculty = QLineEdit()
      
      self.typeIndicator = QLabel("Type")
      self.typeOfCourse = QLineEdit()
      self. layout.addRow(self.facultyIndicator,self.faculty)
      self.layout.addRow(self.typeIndicator,self.typeOfCourse)
      self.layout.addRow(self.cancel, self.done)
      
      
      self.setLayout(self.layout)
      self.setWindowTitle("Add Course")
      
      self.errorText = QLabel("")
      self.layout.addRow(self.errorText)
      
      
   
    #Contacts controller with proper input to add course to database
   def SubmitCourse(self):
       result = self.controller.addCourse(self.le1.text(), self.le2.text(), self.user.id, self.faculty.text(), self.typeOfCourse.text())
       if(result == 1):
#            self.errorText.setText("Course Added Successfully")
            
            self.refreshCourses_request.emit()
            self.loaddashlayout.emit(1)
            
       elif(result == 0):
            self.errorText.setText("Database Error")
       elif(result == 2):
            self.errorText.setText("Course Already Added Before")
       elif(result == 3):
            self.errorText.setText("Youtube Error")
       else:
            self.errorText.setText("Unknown Error") 
       

   def goBack(self):
       self.loaddashlayout.emit(0)