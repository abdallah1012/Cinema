#include <string>
#include <QtWidgets>
#pragma once
using namespace std;


class User
{
protected:
    string first_name_;
    string last_name_;
    QDate dob_;
    string username_;
    string password_;
    string email_;
public:
    static void SignIn(string username,string password);
};
