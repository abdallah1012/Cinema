#ifndef USERMANAGEMENTSYSTEM_H
#define USERMANAGEMENTSYSTEM_H
#include <string>
using namespace std;

class UserManagementSystem
{
public:
    UserManagementSystem();
    string VerifySignInCred(string username,string password);
    ~UserManagementSystem();
};

#endif // USERMANAGEMENTSYSTEM_H
