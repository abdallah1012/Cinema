 # -*- coding: utf-8 -*-




import WelcomeWidget
import UserManagement

#Controller responsible for the relevant layout's communication with other models and layouts
class RegisterController:
    def __init__(self):   
       
        #change localhost to IP address and root to username of database
        #This was tested using wampserver
        self.Manager = UserManagement.UserManagement() #manager to communicate with the user table
        
    #checks if username already exists
    #params: string username
    #returns output of manager's checkforusername function, 1 if username exists and 0 if it doesn't
    def CheckUserExists(self, username):
        
        result = self.Manager.CheckForUsername(username)    
        return result
    
    #adds row to "users" table
    #params: string username, string firstname, string lastname, string password, string user
    #returns output of manager's addtousers function, 1 if successfull and 0 if failed
    def RegisterUser(self, username, firstname, lastname, password, user):
        
        result = self.Manager.AddToUsers(username, firstname, lastname, password, user)
        return result
        
    #returns user to sign in layout
    #returns "success" for register's layout to emit signal to close itself
    def goBack(self):
        
        
        Signin = WelcomeWidget.WelcomeWidget()
        Signin.show()
        
        return "success"
        
        
        
        
        
        
        