#include "User.h"

string User::SignIn(string username,string password){
    if (username=="" || password == "")
        return "Empty username or password";
    else{
        UserManagementSystem * UMS = new UserManagementSystem();
        string result = UMS->VerifySignInCred(username,password);
        delete UMS;
        return result;
    }
}
